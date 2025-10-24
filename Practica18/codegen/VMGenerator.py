# codegen/VMGenerator.py
class SimpleVM:
    def __init__(self):
        self.memory = {}  # Variables
        self.stack = []   # Stack para operaciones
        self.pc = 0      # Program counter
        self.instructions = []
        
    def load_program(self, tac_instructions):
        """Carga programa TAC en la VM"""
        self.instructions = self.translate_to_vm_code(tac_instructions)
        
    def translate_to_vm_code(self, tac_instructions):
        """Traduce TAC a instrucciones VM"""
        vm_code = []
        label_map = {}
        
        # Primera pasada: mapear etiquetas
        for i, inst in enumerate(tac_instructions):
            if inst['op'].endswith(':'):
                label_map[inst['op'][:-1]] = i
        
        # Segunda pasada: traducir instrucciones
        for inst in tac_instructions:
            vm_inst = self.translate_tac_to_vm(inst, label_map)
            if vm_inst:
                vm_code.append(vm_inst)
                
        return vm_code
    
    def translate_tac_to_vm(self, tac_inst, label_map):
        """Traduce una instrucción TAC a VM"""
        op = tac_inst['op']
        
        if op in ['+', '-', '*', '/']:
            return {
                'opcode': 'BINARY_OP',
                'operator': op,
                'arg1': tac_inst['arg1'],
                'arg2': tac_inst['arg2'], 
                'result': tac_inst['result']
            }
            
        elif op == '=':
            return {
                'opcode': 'ASSIGN',
                'source': tac_inst['arg1'],
                'dest': tac_inst['result']
            }
            
        elif op == 'if_false_goto':
            return {
                'opcode': 'JUMP_IF_FALSE',
                'condition': tac_inst['arg1'],
                'target': label_map.get(tac_inst['result'], 0)
            }
            
        elif op == 'goto':
            return {
                'opcode': 'JUMP',
                'target': label_map.get(tac_inst['result'], 0)
            }
            
        return None
    
    def execute(self):
        """Ejecuta el programa cargado"""
        self.pc = 0
        
        while self.pc < len(self.instructions):
            inst = self.instructions[self.pc]
            
            if inst['opcode'] == 'BINARY_OP':
                val1 = self.get_value(inst['arg1'])
                val2 = self.get_value(inst['arg2'])
                
                if inst['operator'] == '+':
                    result = val1 + val2
                elif inst['operator'] == '-':
                    result = val1 - val2
                elif inst['operator'] == '*':
                    result = val1 * val2
                elif inst['operator'] == '/':
                    result = val1 / val2 if val2 != 0 else 0
                    
                self.memory[inst['result']] = result
                
            elif inst['opcode'] == 'ASSIGN':
                value = self.get_value(inst['source'])
                self.memory[inst['dest']] = value
                
            elif inst['opcode'] == 'JUMP_IF_FALSE':
                condition = self.get_value(inst['condition'])
                if not condition:
                    self.pc = inst['target']
                    continue
                    
            elif inst['opcode'] == 'JUMP':
                self.pc = inst['target']
                continue
            
            self.pc += 1
    
    def get_value(self, operand):
        """Obtiene valor de operando (variable o literal)"""
        if operand.isdigit() or (operand.startswith('-') and operand[1:].isdigit()):
            return int(operand)
        elif operand.replace('.', '').isdigit():
            return float(operand)
        else:
            return self.memory.get(operand, 0)