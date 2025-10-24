# codegen/DirectInterpreter.py
class TACInterpreter:
    def __init__(self):
        self.variables = {}
        self.call_stack = []
        self.program_counter = 0
        
    def interpret(self, tac_instructions):
        """Interpreta TAC directamente"""
        self.instructions = tac_instructions
        self.program_counter = 0
        
        # Crear mapa de etiquetas
        self.labels = {}
        for i, inst in enumerate(tac_instructions):
            if inst['op'].endswith(':'):
                self.labels[inst['op'][:-1]] = i
        
        # Ejecutar programa
        while self.program_counter < len(self.instructions):
            self.execute_instruction(self.instructions[self.program_counter])
            
    def execute_instruction(self, instruction):
        """Ejecuta una instrucción TAC"""
        op = instruction['op']
        
        if op == '+':
            val1 = self.get_variable_value(instruction['arg1'])
            val2 = self.get_variable_value(instruction['arg2'])
            self.variables[instruction['result']] = val1 + val2
            
        elif op == '-':
            val1 = self.get_variable_value(instruction['arg1'])
            val2 = self.get_variable_value(instruction['arg2'])
            self.variables[instruction['result']] = val1 - val2
            
        elif op == '*':
            val1 = self.get_variable_value(instruction['arg1'])
            val2 = self.get_variable_value(instruction['arg2'])
            self.variables[instruction['result']] = val1 * val2
            
        elif op == '/':
            val1 = self.get_variable_value(instruction['arg1'])
            val2 = self.get_variable_value(instruction['arg2'])
            self.variables[instruction['result']] = val1 / val2 if val2 != 0 else 0
            
        elif op == '=':
            value = self.get_variable_value(instruction['arg1'])
            self.variables[instruction['result']] = value
            
        elif op == 'if_false_goto':
            condition = self.get_variable_value(instruction['arg1'])
            if not condition:
                self.program_counter = self.labels[instruction['result']]
                return
                
        elif op == 'goto':
            self.program_counter = self.labels[instruction['result']]
            return
            
        elif op == 'PRINT':
            value = self.get_variable_value(instruction['arg1'])
            print(f"OUTPUT: {value}")
            
        elif op.endswith(':'):
            # Etiqueta - no hacer nada
            pass
            
        self.program_counter += 1
    
    def get_variable_value(self, name):
        """Obtiene valor de variable o literal"""
        if name.isdigit() or (name.startswith('-') and name[1:].isdigit()):
            return int(name)
        elif '.' in name and name.replace('.', '').replace('-', '').isdigit():
            return float(name)
        else:
            return self.variables.get(name, 0)