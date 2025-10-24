
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener 

from generated.IfElseLangLexer import IfElseLangLexer
from generated.IfElseLangParser import IfElseLangParser
from semantic_analyzer.SemanticVisitor import SemanticVisitor
# Actualización para incluir generación de código
from codegen.PythonGenerator import PythonCodeGenerator
from codegen.VMGenerator import SimpleVM
from codegen.AssemblyGenerator import AssemblyGenerator
from codegen.DirectInterpreter import TACInterpreter

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Lanza una excepción para detener la ejecución de inmediato
        raise Exception(f"Error de sintaxis en la línea {line}:{column} - {msg}")

def main():
    try:
        input_stream = FileStream("input.txt", encoding='utf-8')
        lexer = IfElseLangLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(MyErrorListener()) # Ahora Python sabe qué es MyErrorListener

        stream = CommonTokenStream(lexer)
        parser = IfElseLangParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(MyErrorListener())

        tree = parser.program()
        print("Análisis sintáctico completado sin errores.")

        visitor = SemanticVisitor() 
        visitor.visit(tree)
        print("Análisis semántico completado.") 

        # --- Imprimir el Código Intermedio (IR) ---
        print("\n--- Código Intermedio (TAC) Generado ---")
        print(visitor.ir)
        # --------------------------------------------------
    # NUEVA SECCIÓN: GENERACIÓN DE CÓDIGO FINAL
        print("\n" + "="*50)
        print("GENERACIÓN DE CÓDIGO FINAL")
        print("="*50)
        
        # 1. Generar código Python
        python_gen = PythonCodeGenerator()
        python_code = python_gen.generate_from_tac(visitor.ir.instructions)
        print("\n--- Código Python Generado ---")
        print(python_code)
        
        # Guardar código Python
        with open("output_program.py", "w") as f:
            f.write(python_code)
        print("\n✓ Código Python guardado en 'output_program.py'")
        
        # 2. Generar pseudo-ensamblador
        asm_gen = AssemblyGenerator()
        assembly_code = asm_gen.generate(visitor.ir.instructions)
        print("\n--- Pseudo-Ensamblador Generado ---")
        print(assembly_code)
        
        # 3. Ejecutar con máquina virtual
        print("\n--- Ejecución en Máquina Virtual ---")
        vm = SimpleVM()
        vm.load_program(visitor.ir.instructions)
        vm.execute()
        print("Variables finales:", vm.memory)
        
        # 4. Interpretación directa
        print("\n--- Interpretación Directa de TAC ---")
        interpreter = TACInterpreter()
        interpreter.interpret(visitor.ir.instructions)
        print("Variables finales:", interpreter.variables)
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()