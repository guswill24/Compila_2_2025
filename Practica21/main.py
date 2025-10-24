import sys
from antlr4 import *
from generated.CSVLexer import CSVLexer
from generated.CSVParser import CSVParser
from generated.CSVListener import CSVListener

# Esta clase representa nuestra Representación Intermedia (RI) para una fila.
# Es una estructura de datos validada y con tipos correctos.
class ValidatedRow:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"ValidatedRow(data={self.data})"

class Loader(CSVListener):
    def __init__(self):
        self.intermediate_representation = []
        self.header = []
        self.currentRowFieldValues = []

    # FASE 3: ANÁLISIS SEMÁNTICO Y GENERACIÓN DE RI
    def exitHeader(self, ctx:CSVParser.HeaderContext):
        self.header = list(self.currentRowFieldValues)
        self.currentRowFieldValues = []

    def enterRow(self, ctx:CSVParser.RowContext):
        self.currentRowFieldValues = []

    def exitRow(self, ctx:CSVParser.RowContext):
        # La cabecera ya fue procesada y almacenada, no necesita más análisis.
        if ctx.parentCtx.getRuleIndex() == CSVParser.RULE_header:
            return

        # ---- INICIO ANÁLISIS SEMÁNTICO ----
        # Regla 1: El número de columnas debe coincidir con la cabecera.
        if len(self.currentRowFieldValues) != len(self.header):
            line = ctx.start.line
            print(f"Error Semántico (Línea {line}): La fila tiene {len(self.currentRowFieldValues)} columnas, se esperaban {len(self.header)}. Fila omitida.")
            return
        # ---- FIN ANÁLISIS SEMÁNTICO ----
        
        # ---- INICIO GENERACIÓN DE RI ----
        # Limpiar y transformar datos antes de crear la RI
        row_dict = {}
        for i, val in enumerate(self.currentRowFieldValues):
            key = self.header[i]
            # Limpieza simple como parte de la generación de RI
            if isinstance(val, str):
                cleaned_val = val.strip()
                # Lógica de conversión de tipos (ej. para 'Cantidad')
                if key == "Cantidad":
                    cleaned_val = cleaned_val.replace('$', '').replace(',', '')
                row_dict[key] = cleaned_val
            else:
                row_dict[key] = val
        
        # Crear una instancia de nuestra RI y añadirla a la lista.
        self.intermediate_representation.append(ValidatedRow(row_dict))
        # ---- FIN GENERACIÓN DE RI ----

    def exitText(self, ctx:CSVParser.TextContext):
        self.currentRowFieldValues.append(ctx.getText())

    def exitString(self, ctx:CSVParser.StringContext):
        text = ctx.getText()[1:-1].replace('""', '"')
        self.currentRowFieldValues.append(text)

    def exitEmpty(self, ctx:CSVParser.EmptyContext):
        self.currentRowFieldValues.append("")

def main(argv):
    # FASE 1: ANÁLISIS LÉXICO
    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = CSVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # FASE 2: ANÁLISIS SINTÁCTICO
    parser = CSVParser(stream)
    tree = parser.csvFile()

    # FASE 3: ANÁLISIS SEMÁNTICO Y GENERACIÓN DE RI
    loader = Loader()
    walker = ParseTreeWalker()
    walker.walk(loader, tree)

    # El resultado es la Representación Intermedia
    print("--- Representación Intermedia Generada ---")
    for row in loader.intermediate_representation:
        print(row)

if __name__ == '__main__':
    main(sys.argv)