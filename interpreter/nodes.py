# Implementa a classe base AST e as classes herdeiras
# BinaryOperation -> define o nó de uma operação binária.
# IntegerNumber -> define o nó de um número inteiro.

class AST:
    pass

class BinaryOperation(AST):
    # Representa um nó de operação binária.
    def __init__(self, left_node, operation, right_node):
        self.left_node = left_node
        self.operation = operation
        self.right_node = right_node


class UnaryOperation(AST):
    # Representa um nó de operação unária.
    def __init__(self, operation, operand_node):
        self.operation = operation
        self.operand_node = operand_node


class IntegerNumber(AST):
    # Representa um nó de número inteiro.
    def __init__(self, integer):
        self.type = integer.type
        self.value = integer.value
