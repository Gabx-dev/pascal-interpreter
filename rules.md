# Regras

## Aritmética
expression: term {(ADDITION | SUBTRACTION) term};
term: factor {(MULTIPLICATION | DIVISION) factor};
factor: INTEGER | LEFT-PAREN expression RIGHT-PAREN;

## Operadores
ADDITION: "+";
SUBTRACTION: "-";
MULTIPLICATION: "*";
DIVISION: "/";
LEFT-PAREN: "(";
RIGHT-PAREN: ")";)

## Tipos de dados
INTEGER: "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0";