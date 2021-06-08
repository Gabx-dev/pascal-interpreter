# Constantes de token e classe Token para o interpretador de Pascal
# Autor: GabrielBonagio <gabriel.bonagio16@gmail.com>
# Data: 6/6/2021

INTEGER = 'INTEGER'
PLUS, MINUS = 'PLUS', 'MINUS'
STAR, SLASH = 'STAR', 'SLASH'
LEFT_PAREN, RIGHT_PAREN = 'LEFT_PAREN', 'RIGHT_PAREN'
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
