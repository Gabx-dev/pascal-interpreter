# Constantes de token e classe Token para o interpretador de Pascal
# Autor: GabrielBonagio <gabriel.bonagio16@gmail.com>

INTEGER = 'INTEGER'
PLUS, MINUS = 'PLUS', 'MINUS'
STAR, SLASH = 'STAR', 'SLASH'
LEFT_PAREN, RIGHT_PAREN = 'LEFT_PAREN', 'RIGHT_PAREN'
IDENTIFIER = 'IDENTIFIER'
ASSIGN = 'ASSIGN'
SEMI, DOT = 'SEMI', 'DOT'
EOF = 'EOF'


class Token:
    def __init__(self, type, value):
        # Um dentre INTEGER, PLUS, MINUS, STAR, SLASH, LEFT_PAREN, RIGHT_PAREN, e EOF.
        self.type = type

        # E um valor correspondente
        self.value = value

    def __str__(self):
        '''Representação em string do Token.'''
        return f'Token({self.type}, {self.value})'

    def __repr__(self):
        return self.__str__()

# Palavras reservadas

BEGIN, END = 'BEGIN', 'END'

RESERVED_KEYWORDS = {
    BEGIN: Token(BEGIN, BEGIN),
    END: Token(END, END)
}
