# Regras

## Aritmética
expression: term {(PLUS | MINUS) term};  
term: signed-factor {(STAR | SLASH) signed-factor};  
signed-factor: [PLUS | MINUS] factor;  
factor: LEFT-PAREN expression RIGHT-PAREN | INTEGER;  

## Operadores
PLUS: "+";  
MINUS: "-";  
STAR: "*";  
SLASH: "/";  
LEFT-PAREN: "(";  
RIGHT-PAREN: ")";)  

## Tipos de dados
INTEGER: "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0";  
