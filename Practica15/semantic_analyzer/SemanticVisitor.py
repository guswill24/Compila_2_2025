# semantic_analyzer/SemanticVisitor.py
from generated.IfElseLangVisitor import IfElseLangVisitor
from generated.IfElseLangParser import IfElseLangParser
from .SymbolTable import SymbolTable, Symbol

class SemanticVisitor(IfElseLangVisitor):
    def __init__(self):
        self.table = SymbolTable()
        # NUEVO: Atributo para rastrear la función actual y validar los 'return'.
        self.current_function = None

    # Visitante para la declaración de variables.
    def visitDeclaration(self, ctx:IfElseLangParser.DeclarationContext):
        var_name = ctx.ID().getText()
        type_name = ctx.type_().getText()
        # Creamos un Símbolo con categoría 'variable'.
        symbol = Symbol(name=var_name, type=type_name, category='variable')
        
        # Insertar en la tabla de símbolos del ámbito actual.
        self.table.insert(var_name, symbol)

        # Si hay una expresión de inicialización, la validamos.
        if ctx.expr():
            expr_type = self.visit(ctx.expr())
            if expr_type != 'error_type' and expr_type is not None and symbol.type != expr_type:
                print(f"Error Semántico: No se puede asignar tipo '{expr_type}' a la variable '{var_name}' de tipo '{symbol.type}' en su declaración.")
        
        return None # No necesitamos propagar nada.

    # --- NUEVO: Visitante para la declaración de funciones ---
    def visitFunctionDecl(self, ctx:IfElseLangParser.FunctionDeclContext):
        func_name = ctx.ID().getText()
        return_type = ctx.type_().getText()
        
        # 1. Procesar parámetros
        param_symbols = []
        if ctx.paramList():
            for param_ctx in ctx.paramList().param():
                param_name = param_ctx.ID().getText()
                param_type = param_ctx.type_().getText()
                param_symbols.append(Symbol(name=param_name, type=param_type, category='variable'))

        # 2. Crear el símbolo de la función
        func_symbol = Symbol(name=func_name, type=return_type, category='function', params=param_symbols)
        
        # 3. Insertar la función en el ámbito PADRE (actual)
        self.table.insert(func_name, func_symbol)

        # 4. Guardar referencia a la función actual para validar retornos
        self.current_function = func_symbol
        
        # 5. Entrar en un nuevo ámbito para el cuerpo de la función
        self.table.enter_scope()

        # 6. Definir los parámetros como variables en el nuevo ámbito
        for param in param_symbols:
            self.table.insert(param.name, param)
        
        # 7. Visitar el cuerpo de la función
        self.visitChildren(ctx.block()) # Visitamos el bloque del cuerpo de la función

        # 8. Salir del ámbito de la función
        self.table.exit_scope()
        
        # 9. Limpiar la referencia a la función actual
        self.current_function = None
        
        return None

    # --- NUEVO: Visitante para la llamada a funciones ---
    def visitFuncCallExpr(self, ctx:IfElseLangParser.FuncCallExprContext):
        func_name = ctx.ID().getText()
        symbol = self.table.lookup(func_name)

        # Comprobación 1: ¿Existe el símbolo?
        if symbol is None:
            print(f"Error Semántico: La función '{func_name}' no ha sido declarada.")
            return 'error_type'
        
        # Comprobación 2: ¿Es realmente una función?
        if symbol.category != 'function':
            print(f"Error Semántico: El identificador '{func_name}' no es una función, no se puede llamar.")
            return 'error_type'
        
        # Comprobación 3: ¿Coincide el número de argumentos?
        provided_args = ctx.argList().expr() if ctx.argList() else []
        expected_params = symbol.params
        if len(provided_args) != len(expected_params):
            print(f"Error Semántico: La función '{func_name}' esperaba {len(expected_params)} argumentos, pero recibió {len(provided_args)}.")
            return 'error_type'
            
        # Comprobación 4: ¿Coinciden los tipos de los argumentos?
        for i, arg_expr in enumerate(provided_args):
            arg_type = self.visit(arg_expr)
            param_type = expected_params[i].type
            if arg_type != param_type:
                print(f"Error Semántico: En la llamada a '{func_name}', el argumento {i+1} es de tipo '{arg_type}', pero se esperaba '{param_type}'.")
                return 'error_type'
        
        # Si todo está bien, el tipo de esta expresión es el tipo de retorno de la función.
        return symbol.type

    # --- NUEVO: Visitante para la sentencia de retorno ---
    def visitReturnStatement(self, ctx:IfElseLangParser.ReturnStatementContext):
        # Comprobación 1: ¿Estamos dentro de una función?
        if self.current_function is None:
            print("Error Semántico: La sentencia 'return' solo puede aparecer dentro de una función.")
            return None
        
        # Comprobación 2: ¿El tipo de retorno coincide?
        return_type = self.visit(ctx.expr())
        expected_type = self.current_function.type
        
        if return_type != expected_type:
            print(f"Error Semántico: La función '{self.current_function.name}' debe retornar un valor de tipo '{expected_type}', pero se encontró '{return_type}'.")
        
        return None
        
    # --- VISITANTES EXISTENTES (CON PEQUEÑAS MEJORAS) ---

    def visitAssignment(self, ctx:IfElseLangParser.AssignmentContext):
        var_name = ctx.ID().getText()
        symbol = self.table.lookup(var_name)

        if symbol is None:
            print(f"Error Semántico: La variable '{var_name}' no ha sido declarada.")
            return None
        
        if symbol.category == 'function':
             print(f"Error Semántico: No se puede asignar un valor a la función '{var_name}'.")
             return None

        expr_type = self.visit(ctx.expr())
        if expr_type != 'error_type' and expr_type is not None and symbol.type != expr_type:
            print(f"Error Semántico: No se puede asignar tipo '{expr_type}' a la variable '{var_name}' de tipo '{symbol.type}'.")
        return None

    def visitIdExpr(self, ctx:IfElseLangParser.IdExprContext):
        var_name = ctx.ID().getText()
        symbol = self.table.lookup(var_name)
        if symbol is None:
            print(f"Error Semántico: La variable '{var_name}' no ha sido declarada.")
            return 'error_type'

        if symbol.category == 'function':
            print(f"Error Semántico: No se puede usar la función '{var_name}' como una variable en una expresión.")
            return 'error_type'
        return symbol.type

    # REFACTORIZADO: visitIfStatement ahora es mucho más simple gracias a la regla 'block'.
    def visitIfStatement(self, ctx:IfElseLangParser.IfStatementContext):
        self.visit(ctx.condition())
        
        # Visitar el bloque 'then' (primer bloque)
        self.table.enter_scope()
        self.visit(ctx.block(0))
        self.table.exit_scope()

        # Si existe un bloque 'else', visitarlo
        if ctx.ELSE():
            self.table.enter_scope()
            self.visit(ctx.block(1)) # El bloque 'else' es el segundo
            self.table.exit_scope()

        return None
        
    def visitNumberExpr(self, ctx:IfElseLangParser.NumberExprContext):
        return 'int'

    def visitStringExpr(self, ctx:IfElseLangParser.StringExprContext):
        return 'string'

    def visitComparisonExpr(self, ctx:IfElseLangParser.ComparisonExprContext):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))
        if left_type != right_type:
            print(f"Error Semántico: Comparación entre tipos incompatibles ({left_type} vs {right_type}).")
            return 'error_type'
        return 'int'

    # SOLUCIONADO: visitArithmeticExpr ahora soporta la concatenación de strings.
    def visitArithmeticExpr(self, ctx:IfElseLangParser.ArithmeticExprContext):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))

        if left_type == 'error_type' or right_type == 'error_type':
            return 'error_type'

        # Permitir int + int
        if left_type == 'int' and right_type == 'int':
            return 'int'
        
        # Permitir string + string (concatenación)
        if left_type == 'string' and right_type == 'string':
            return 'string'

        # Cualquier otra combinación es un error.
        print(f"Error Semántico: El operador '{ctx.op.text}' no se puede aplicar a los tipos '{left_type}' y '{right_type}'.")
        return 'error_type'

    def visitParenExpr(self, ctx:IfElseLangParser.ParenExprContext):
        return self.visit(ctx.expr())

