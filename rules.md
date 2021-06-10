# Gramática  

program: compound-statement DOT;  
compound-statement: BEGIN statement-list END;  
statement-list: statement {SEMI statement};  
statement: assignment-statement | compound-statement | empty-statement;  
assignment-statement: variable ASSIGN expression;  
empty-statement: ;  
variable: ID;  
expression: term {(PLUS | MINUS) term};  
term: factor {(STAR | SLASH) factor};  
factor: (PLUS | MINUS) factor | integer | LEFT-PAREN expression RIGHT-PAREN | variable;  
integer: digit | DIGIT-EXCLUDING-ZERO {digit};  
DOT: ".";  
SEMI: ";";  
ASSIGN: ":=";  
PLUS: "+";  
MINUS: "-";  
STAR: "*";  
SLASH: "/";  
LEFT-PAREN: "(";  
RIGHT-PAREN: ")";  )
BEGIN: "BEGIN";  
END: "END";  
ID: LETTER {LETTER | DIGIT};  
  
digit: DIGIT-EXCLUDING-ZERO | "0";  
DIGIT-EXCLUDING-ZERO: "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";  
LETTER:  
"a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "j" | "k" | "l" | "m" |  
"n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" |  
"A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" |  
"N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z";  
