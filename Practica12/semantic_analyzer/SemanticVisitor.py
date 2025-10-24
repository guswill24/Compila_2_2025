# semantic_analyzer/SemanticVisitor.py
from generated.IfElseLangVisitor import IfElseLangVisitor
from generated.IfElseLangParser import IfElseLangParser
from .SymbolTable import SymbolTable, Symbol

class SemanticVisitor(IfElseLangVisitor):
    def __init__(self):
        self.table = SymbolTable()

    # Visitar una declaración para POBLAR la tabla
    def visitDeclaration(self, ctx:IfElseLangParser.DeclarationContext):
        var_name = ctx.ID().getText()
        type_name = ctx.type_().getText()
        self.table.insert(var_name, Symbol(var_name, type_name))
        return self.visitChildren(ctx)

    # Visitar una asignación para VERIFICAR que la variable existe
    def visitAssignment(self, ctx:IfElseLangParser.AssignmentContext):
        var_name = ctx.ID().getText()
        symbol = self.table.lookup(var_name)

        # Regla Semántica: La variable debe existir para poder asignarle un valor
        if symbol is None:
            print(f"Error Semántico: La variable '{var_name}' no ha sido declarada.")
        
        # Continuar recorriendo el árbol (visitamos la expresión)
        return self.visitChildren(ctx)

    # Visitar un ID en una expresión para VERIFICAR que existe
    # (Asumimos una regla en la gramática como: expr: ID)
    def visitExpr(self, ctx:IfElseLangParser.ExprContext):
        if ctx.NUMBER():
            return 'int'
        
        if ctx.ID():
            var_name = ctx.ID().getText()
            symbol = self.table.lookup(var_name)
            # ESTA ES LA LÓGICA QUE DEBE SALTAR
            if symbol is None:
                # Imprimimos el error aquí
                print(f"Error Semántico: La variable '{var_name}' no ha sido declarada.")
                return 'error_type'
            return symbol.type
    # Aquí irían más lógicas para otros tipos de expresiones (suma, etc.)

# El método para visitar una asignación ahora COMPARA tipos
    def visitAssignment(self, ctx:IfElseLangParser.AssignmentContext):
        # 1. Obtener el nombre y símbolo de la variable de la izquierda (ej: 'a')
        var_name = ctx.ID().getText()
        symbol = self.table.lookup(var_name)

        if symbol is None:
            print(f"Error Semántico: La variable '{var_name}' a la que se intenta asignar no ha sido declarada.")
            return None

        # 2. Visitar la expresión de la derecha (ej: 'temp')
        # Esto ejecutará visitExpr sobre 'temp', lo cual imprimirá el error correcto
        expr_type = self.visit(ctx.expr())
        
        # 3. (Lógica de la Clase 3) Verificar compatibilidad de tipos
        if expr_type != 'error_type' and symbol.type != expr_type:
            print(f"Error Semántico: No se puede asignar tipo '{expr_type}' a variable '{var_name}' de tipo '{symbol.type}'.")
            
        return None

# Usamos los scopes en las estructuras de bloque
    def visitIfStatement(self, ctx:IfElseLangParser.IfStatementContext):
        # Visitar la condición (se evalúa en el ámbito actual)
        self.visit(ctx.condition())

        # Entrar en un nuevo ámbito para el bloque THEN
        self.table.enter_scope()
        self.visit(ctx.statement(0)) # Asumiendo que el primer bloque de statements es el 'then'
        self.table.exit_scope()

        # Si hay un bloque ELSE
        if ctx.ELSE():
            self.table.enter_scope()
            self.visit(ctx.statement(1)) # El segundo bloque es el 'else'
            self.table.exit_scope()
        
        return None # No necesitamos visitar más hijos desde aquí