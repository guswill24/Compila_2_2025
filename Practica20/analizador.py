# analizador.py
from antlr4 import *
from generated.CSVLexer import CSVLexer
from generated.CSVParser import CSVParser
from generated.CSVListener import CSVListener
import json

class AnalizadorCSV(CSVListener):
    def __init__(self, header):
        self.header = header
        self.rows = []
        # Estructuras para las tareas semánticas
        self.month_counts = {}
        self.seen_rows = set()
        self.malformed_quantity_rows = []
        self.duplicate_rows_count = 0

    # Este método se llama al salir de CADA fila (excepto la cabecera)
    def exitRow(self, ctx:CSVParser.RowContext):
        # Se ignora la cabecera, que se procesa por separado
        if ctx.parentCtx.getRuleIndex() == CSVParser.RULE_header:
            return

        # 1. Construir el diccionario de la fila actual
        # (Esto asume que se tiene una lógica para recolectar los campos de la fila actual.
        # En este ejemplo, el texto se extrae directamente)
        current_fields = [field.getText() for field in ctx.field()]
        row_dict = dict(zip(self.header, current_fields))

        # TAREA 1: Detectar filas repetidas
        # En esta parte se convierte los valores del diccionario en una tupla para poder añadirla a un 'set'
        row_tuple = tuple(row_dict.values())
        if row_tuple in self.seen_rows:
            self.duplicate_rows_count += 1
            return
        self.seen_rows.add(row_tuple)

        # TAREA 2: Contar cuántas veces aparece cada mes
        mes = row_dict.get("Mes")
        if mes:
            self.month_counts[mes] = self.month_counts.get(mes, 0) + 1

        # TAREA 3: Detectar campos 'Cantidad' vacíos o mal formateados
        cantidad_str = row_dict.get("Cantidad", "").replace('"', '').replace(',', '')
        if not cantidad_str: # Campo vacío
            self.malformed_quantity_rows.append((ctx.start.line, "vacío"))
        else:
            try:
                # Intentar convertir a número. Si falla, está mal formateado.
                float(cantidad_str)
            except ValueError:
                self.malformed_quantity_rows.append((ctx.start.line, cantidad_str))
        
        # Guardar la fila si es válida para la siguiente fase
        self.rows.append(row_dict)

    # TAREA 4: Crear un diccionario {"Mes": total_montos}
    def generar_resumen_mensual(self):
        resumen = {}
        for row in self.rows:
            mes = row.get("Mes")
            cantidad_str = row.get("Cantidad", "0").replace('"', '').replace(',', '')
            
            try:
                monto = float(cantidad_str)
                if mes:
                    resumen[mes] = resumen.get(mes, 0) + monto
            except ValueError:
                # Ignoramos las filas con montos mal formateados que ya detectamos
                continue
        return resumen
# ... (debajo de la clase AnalizadorCSV)

def main():
    # Cargar el archivo CSV
    input_stream = FileStream("datos.csv", encoding="utf-8")
    
    # Crear el Lexer y el Parser
    lexer = CSVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSVParser(stream)
    
    # Leer la cabecera primero para poder usarla en el Listener
    header_ctx = parser.header()
    header = [field.getText() for field in header_ctx.row().field()]
    parser.reset() # Reiniciar el parser para leer el archivo desde el principio
    
    # Iniciar el análisis completo
    tree = parser.csvFile()
    
    # Crear nuestro listener personalizado con la cabecera
    analizador = AnalizadorCSV(header)
    
    # Recorrer el árbol con el listener
    walker = ParseTreeWalker()
    walker.walk(analizador, tree)
    
    # --- IMPRESIÓN DE RESULTADOS ---
    print("--- FASE SEMÁNTICA: Resultados del Análisis ---")
    print(f"✔️ Conteo de apariciones por mes: {json.dumps(analizador.month_counts, indent=2)}")
    print(f"✔️ Filas duplicadas encontradas: {analizador.duplicate_rows_count}")
    print("✔️ Filas con campo 'Cantidad' mal formateado o vacío:")
    if not analizador.malformed_quantity_rows:
        print("   Ninguna.")
    else:
        for linea, valor in analizador.malformed_quantity_rows:
            print(f"   - Línea {linea}: valor '{valor}'")

    print("\n--- FASE DE CÓDIGO INTERMEDIO: Resumen Generado ---")
    resumen_mensual = analizador.generar_resumen_mensual()
    print(f"✔️ Diccionario de totales por mes: {json.dumps(resumen_mensual, indent=2)}")


if __name__ == '__main__':
    main()