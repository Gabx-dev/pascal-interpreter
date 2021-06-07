# Regras

## Aritmética
expression: term {(ADDITION | SUBTRACTION) term};
term: factor {(MULTIPLICATION | DIVISION) factor};
factor: INTEGER;

## Operadores
ADDITION: "+";
SUBTRACTION: "-";
MULTIPLICATION: "*";
DIVISION: "/";

## Tipos de dados
INTEGER: "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0";