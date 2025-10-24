# codegen/AssemblyGenerator.py
class AssemblyGenerator:
    def __init__(self):
        self.code = []
        self.data_section = []
        self.label_counter = 0
        
    def generate(self, tac_instructions):
        """Genera pseudo-ensamblador desde TAC"""
        self.emit_header()
        self.process_instructions(tac_instructions)
        self.emit_footer()
        return self.format_output()
    
    def process_instructions(self, instructions):
        for inst in instructions:
            op = inst['op']
            
            if op in ['+', '-', '*', '/']:
                self.emit_arithmetic(inst)
            elif op == '=':
                self.emit_assignment(inst)
            elif op == 'if_false_goto':
                self.emit_conditional_jump(inst)
            elif op.endswith(':'):
                self.emit_label(inst['op'])
                
    def emit_arithmetic(self, inst):
        """Genera código para operación aritmética"""
        self.emit(f"    ; {inst['result']} = {inst['arg1']} {inst['op']} {inst['arg2']}")
        self.emit(f"    MOV R1, {inst['arg1']}")
        self.emit(f"    MOV R2, {inst['arg2']}")
        
        if inst['op'] == '+':
            self.emit("    ADD R1, R2")
        elif inst['op'] == '-':
            self.emit("    SUB R1, R2")
        elif inst['op'] == '*':
            self.emit("    MUL R1, R2")
        elif inst['op'] == '/':
            self.emit("    DIV R1, R2")
            
        self.emit(f"    MOV {inst['result']}, R1")
        self.emit("")
    
    def emit_assignment(self, inst):
        """Genera código para asignación"""
        self.emit(f"    ; {inst['result']} = {inst['arg1']}")
        self.emit(f"    MOV R1, {inst['arg1']}")
        self.emit(f"    MOV {inst['result']}, R1")
        self.emit("")
    
    def emit_conditional_jump(self, inst):
        """Genera salto condicional"""
        self.emit(f"    ; if_false {inst['arg1']} goto {inst['result']}")
        self.emit(f"    MOV R1, {inst['arg1']}")
        self.emit("    CMP R1, 0")
        self.emit(f"    JE {inst['result']}")
        self.emit("")
    
    def emit_label(self, label):
        """Genera etiqueta"""
        self.emit(f"{label}")
    
    def emit_header(self):
        self.emit(".section .data")
        self.emit("    ; Variables globales")
        self.emit("")
        self.emit(".section .text")
        self.emit("    .global _start")
        self.emit("")
        self.emit("_start:")
    
    def emit_footer(self):
        self.emit("    ; Terminar programa")
        self.emit("    MOV R0, 0")
        self.emit("    HALT")
    
    def emit(self, line):
        self.code.append(line)
    
    def format_output(self):
        return '\n'.join(self.code)