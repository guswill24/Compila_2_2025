grammar SwitchGrammar;

// Regla principal: un programa consiste en una o más sentencias
program: statement+ EOF;

// Sentencias pueden ser asignaciones o declaraciones switch
statement: assignment | switchStatement;

// Asignación: variable = expresión;
assignment: ID ASSIGN expr SEMI;

// Declaración switch: switch (expresión) { casos y default }
switchStatement: SWITCH LPAREN expr RPAREN LBRACE caseBlock* defaultCase? RBRACE;

// Bloque case: case expresión: sentencias
caseBlock: CASE expr COLON statement*;

// Bloque default: default: sentencias
defaultCase: DEFAULT COLON statement*;

// Expresiones: variables o números
expr: ID | NUMBER;

// Tokens léxicos
// Palabras clave
SWITCH: 'switch';
CASE: 'case';
DEFAULT: 'default';

// Símbolos
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
COLON: ':';
SEMI: ';';
ASSIGN: '=';

// Identificadores y números
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;

// Espacios en blanco: ignorar
WS: [ \t\r\n]+ -> skip;

