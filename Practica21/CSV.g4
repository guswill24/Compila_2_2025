// CSV.g4
grammar CSV;

csvFile : header row* lastRow? ; // Permite cero o más filas completas y una última fila opcional
header  : row ;
row     : field (',' field)* '\r'? '\n' ;
lastRow : field (',' field)* ;      // Una regla para la última fila, sin el '\n' obligatorio

field   : TEXT   # text
        | STRING # string
        |        # empty
        ;

TEXT    : ~[,\n\r"]+ ;
STRING  : '"' ('""'|~'"')* '"' ;
WS      : [ \t]+ -> skip ;