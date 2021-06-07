# Constantes de token e classe Token para o interpretador de Pascal
# Autor: GabrielBonagio <gabriel.bonagio16@gmail.com>
# Data: 6/6/2021

INTEGER = 'INTEGER'
ADDITION, SUBTRACTION = 'ADDITION', 'SUBTRACTION'
MULTIPLICATION, DIVISION = 'MULTIPLICATION', 'DIVISION'
EOF = 'EOF'


class Token(object):
    def __init__(self, type, value):
        super().__init__()
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {self.value})'

    def __repr__(self):
        return self.__str__()
