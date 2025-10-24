grammar WhileLang;

program: statement+ EOF;

statement
    : declaration
    | assignment
    | whileStatement
    | ifStatement
    | breakStatement
    | continueStatement
    ;

declaration: type ID ('=' expr)? SEMI;

type: 'int' | 'string';

assignment: ID ASSIGN expr SEMI;

whileStatement: WHILE LPAREN condition RPAREN LBRACE statement* RBRACE;

ifStatement: IF LPAREN condition RPAREN LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)?;

breakStatement: BREAK SEMI;

continueStatement: CONTINUE SEMI;

condition: expr (GT | LT | EQ | NE) expr;

expr
    : expr (MULT | DIV | MINUS) expr   #ArithmeticExpr
    | ID                               #IdExpr
    | NUMBER                           #NumberExpr
    | STRING                           #StringExpr
    | LPAREN expr RPAREN               #ParenExpr
    ;

// Palabras reservadas
WHILE: 'while';
IF: 'if';
ELSE: 'else';
BREAK: 'break';
CONTINUE: 'continue';

// Símbolos
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ASSIGN: '=';

// Operadores relacionales
GT: '>';
LT: '<';
EQ: '==';
NE: '!=';

// Operadores aritméticos
MINUS: '-';
MULT: '*';
DIV: '/';

// Tokens básicos
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
STRING: '"' (~["\\] | '\\' .)* '"';

// Espacios
WS: [ \t\r\n]+ -> skip;
