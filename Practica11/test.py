from antlr4 import *
from SwitchGrammarLexer import SwitchGrammarLexer
from SwitchGrammarParser import SwitchGrammarParser

# === Entrada de prueba ===
input_text = "x = 2; switch (x) {  case 1: y = 10;  case 2: y = 20;  default: y = 0;}"

# Crear flujo de entrada
input_stream = InputStream(input_text)

# === Fase léxica ===
lexer = SwitchGrammarLexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("## 🔤 TOKENS")
for token in token_stream.tokens:
    if token.type != Token.EOF:
        print(f"  - {lexer.symbolicNames[token.type]} ('{token.text}') @line {token.line}:{token.column}")

print("\n## 🌳 ÁRBOL SINTÁCTICO (toStringTree)")
parser = SwitchGrammarParser(token_stream)
tree = parser.program()
print(tree.toStringTree(recog=parser))

# === Representación indentada ===
def pretty_tree(node, rule_names, level=0):
    if isinstance(node, TerminalNode):
        return "  " * level + f"TOKEN({node.getText()})"
    else:
        rule_name = rule_names[node.getRuleIndex()]
        result = "  " * level + rule_name
        for child in node.children or []:
            result += "\n" + pretty_tree(child, rule_names, level + 1)
        return result

print("\n## 🌲 ÁRBOL SINTÁCTICO (Indentado)")
print(pretty_tree(tree, parser.ruleNames))