# Implementa a classe base AST e as classes herdeiras
# BinaryOperation -> define o nó de uma operação binária.
# IntegerNumber -> define o nó de um número inteiro.

class AST:
    pass

class BinaryOperation(AST):
    def __init__(self, left_node, operation, right_node):
        self.left_node = left_node
        self.operation = operation
        self.right_node = right_node

class IntegerNumber(AST):
    def __init__(self, integer):
        self.type = integer.type
        self.value = integer.value
