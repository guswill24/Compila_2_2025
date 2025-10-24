import sys
from antlr4 import *
from generated.CSVLexer import CSVLexer
from generated.CSVParser import CSVParser
from generated.CSVListener import CSVListener

# -----------------------------------------------------------------------------
# CLASES DE LA LÓGICA DE NEGOCIO Y ANÁLISIS
# -----------------------------------------------------------------------------

# Esta clase representa nuestra Representación Intermedia (RI) para una fila.
# Es una estructura de datos validada y con tipos correctos.
class ValidatedRow:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"ValidatedRow(data={self.data})"

# El Listener original que realiza el análisis semántico y genera la RI.
class Loader(CSVListener):
    def __init__(self):
        self.intermediate_representation = []
        self.header = []
        self.currentRowFieldValues = []

    # FASE 3: ANÁLISIS SEMÁNTico Y GENERACIÓN DE RI
    def exitHeader(self, ctx:CSVParser.HeaderContext):
        self.header = list(self.currentRowFieldValues)
        self.currentRowFieldValues = []

    def enterRow(self, ctx:CSVParser.RowContext):
        self.currentRowFieldValues = []

    def exitRow(self, ctx:CSVParser.RowContext):
        if ctx.parentCtx.getRuleIndex() == CSVParser.RULE_header:
            return

        # ---- INICIO ANÁLISIS SEMÁNTICO ----
        if len(self.currentRowFieldValues) != len(self.header):
            line = ctx.start.line
            print(f"Error Semántico (Línea {line}): La fila tiene {len(self.currentRowFieldValues)} columnas, se esperaban {len(self.header)}. Fila omitida.")
            return
        # ---- FIN ANÁLISIS SEMÁNTICO ----
        
        # ---- INICIO GENERACIÓN DE RI ----
        row_dict = {}
        for i, val in enumerate(self.currentRowFieldValues):
            key = self.header[i]
            if isinstance(val, str):
                cleaned_val = val.strip()
                if key == "Cantidad":
                    cleaned_val = cleaned_val.replace('$', '').replace(',', '')
                row_dict[key] = cleaned_val
            else:
                row_dict[key] = val
        
        self.intermediate_representation.append(ValidatedRow(row_dict))
        # ---- FIN GENERACIÓN DE RI ----

    def exitText(self, ctx:CSVParser.TextContext):
        self.currentRowFieldValues.append(ctx.getText())

    def exitString(self, ctx:CSVParser.StringContext):
        text = ctx.getText()[1:-1].replace('""', '"')
        self.currentRowFieldValues.append(text)

    def exitEmpty(self, ctx:CSVParser.EmptyContext):
        self.currentRowFieldValues.append("")

# -----------------------------------------------------------------------------
# CLASE DIDÁCTICA PARA VISUALIZAR EL RECORRIDO
# -----------------------------------------------------------------------------

# 🔊 Este es el "Listener Locuaz" que imprime cada paso del recorrido.
class VerboseListener(CSVListener):
    def __init__(self):
        self.indentation_level = 0

    def _indent(self):
        return "  " * self.indentation_level

    def enterEveryRule(self, ctx):
        rule_name = type(ctx).__name__.replace('Context', '')
        print(f"{self._indent()}➡️ Entrando a: {rule_name}")
        self.indentation_level += 1

    def exitEveryRule(self, ctx):
        self.indentation_level -= 1
        rule_name = type(ctx).__name__.replace('Context', '')
        print(f"{self._indent()}⬅️ Saliendo de: {rule_name}")


# -----------------------------------------------------------------------------
# FUNCIÓN PRINCIPAL
# -----------------------------------------------------------------------------

def main(argv):
    # FASE 1: ANÁLISIS LÉXICO
    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = CSVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # FASE 2: ANÁLISIS SINTÁCTICO
    parser = CSVParser(stream)
    tree = parser.csvFile()

    # --- Ejecución del Listener Didáctico (VerboseListener) ---
    print("--- 🚶‍♂️ Visualización del Recorrido del Árbol ---")
    verbose_listener = VerboseListener()
    walker = ParseTreeWalker()
    walker.walk(verbose_listener, tree)
    
    print("\n" + "="*50 + "\n") # Separador visual

    # --- Ejecución del Listener Original (Loader) ---
    print("--- ⚙️ Resultado del Análisis y Generación de RI ---")
    loader = Loader()
    walker.walk(loader, tree) # Se puede reutilizar el mismo walker

    # Imprimir errores semánticos detectados por el Loader
    # (El Loader ya imprime los errores durante el recorrido)

    # Imprimir el resultado final
    print("--- Representación Intermedia Generada ---")
    for row in loader.intermediate_representation:
        print(row)

if __name__ == '__main__':
    main(sys.argv)