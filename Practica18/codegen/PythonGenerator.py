# codegen/PythonGenerator.py
class PythonCodeGenerator:
    def __init__(self):
        self.code_lines = []
        self.indent_level = 0
        
    def generate_from_tac(self, tac_instructions):
        """Genera código Python desde TAC"""
        self.emit("# Código generado automáticamente")
        self.emit("def main():")
        self.indent()
        
        # Declarar todas las variables usadas
        self.declare_variables(tac_instructions)
        self.emit("")
        
        # Traducir cada instrucción TAC
        for inst in tac_instructions:
            self.translate_instruction(inst)
            
        self.emit("return 0")
        self.dedent()
        self.emit("")
        self.emit("if __name__ == '__main__':")
        self.emit("    main()")
        
        return '\n'.join(self.code_lines)
    
    def translate_instruction(self, instruction):
        """Traduce una instrucción TAC a Python"""
        op = instruction['op']
        
        if op in ['+', '-', '*', '/', '<', '>', '<=', '>=', '==', '!=']:
            # t1 = a + b → t1 = a + b
            self.emit(f"{instruction['result']} = {instruction['arg1']} {op} {instruction['arg2']}")
            
        elif op == '=':
            # x = y → x = y
            self.emit(f"{instruction['result']} = {instruction['arg1']}")
            
        elif op == 'if_false_goto':
            # if_false t1 goto L1 → if not t1: goto L1 (manejado con flag)
            self.emit(f"if not {instruction['arg1']}:")
            self.indent()
            
        elif op == 'goto':
            # goto L1 → (usar excepciones o restructurar)
            self.emit(f"# goto {instruction['result']}")
            
        elif op.endswith(':'):
            # L1: → # L1:
            self.dedent_if_needed()
            self.emit(f"# {op}")
            
        elif op == 'CALL':
            # CALL func 2 → result = func(arg1, arg2)
            func_name = instruction['arg1']
            num_args = int(instruction['arg2']) if instruction['arg2'] else 0
            
            if instruction['result']:
                self.emit(f"{instruction['result']} = {func_name}()")
            else:
                self.emit(f"{func_name}()")
                
        elif op == 'RETURN':
            # RETURN value → return value
            if instruction['arg1']:
                self.emit(f"return {instruction['arg1']}")
            else:
                self.emit("return")
                
        elif op == 'PRINT':
            # PRINT value → print(value)
            self.emit(f"print({instruction['arg1']})")
    
    def declare_variables(self, instructions):
        """Declara todas las variables temporales y de usuario"""
        variables = set()
        
        for inst in instructions:
            if inst['result'] and not inst['result'].endswith(':'):
                variables.add(inst['result'])
            if inst['arg1'] and inst['arg1'].isidentifier():
                variables.add(inst['arg1'])
            if inst['arg2'] and inst['arg2'].isidentifier():
                variables.add(inst['arg2'])
        
        for var in sorted(variables):
            if var.startswith('t'):  # Variables temporales
                self.emit(f"{var} = 0")
            else:  # Variables de usuario
                self.emit(f"{var} = 0")
    
    def emit(self, line):
        """Emite una línea con indentación apropiada"""
        indent = "    " * self.indent_level
        self.code_lines.append(indent + line)
    
    def indent(self):
        self.indent_level += 1
    
    def dedent(self):
        if self.indent_level > 0:
            self.indent_level -= 1