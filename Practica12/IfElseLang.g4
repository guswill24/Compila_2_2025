grammar IfElseLang;

program: statement+ EOF; 

declaration: type ID ('=' expr)? SEMI; 

type: 'int' | 'string';

statement: assignment | ifStatement | declaration;
assignment: ID ASSIGN expr SEMI;

ifStatement: IF LPAREN condition RPAREN LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)?;

condition: expr operator expr;

expr: ID | NUMBER;

operator: LT | GT | GE | LE | EQ | NE;

IF: 'if';
ELSE: 'else';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ASSIGN: '=';
LT: '<';
GT: '>';
GE: '>=';
LE: '<=';
EQ: '==';
NE: '!=';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
COMMENT: '//' .*? '\n' -> skip;
WS: [ \t\r\n]+ -> skip;