# Interpretador de Pascal escrito em Python
# Autor: GabrielBonagio <gabriel.bonagio16@gmail.com>
# Data: 7/6/2021

from . import pascal_tokens as pt
from . import visitor
from . import parser


class Interpreter(visitor.NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinaryOperation(self, node):
        if node.operation == pt.ADDITION:
            return self.visit(node.left_node) + self.visit(node.right_node)
        elif node.operation == pt.SUBTRACTION:
            return self.visit(node.left_node) - self.visit(node.right_node)
        elif node.operation == pt.MULTIPLICATION:
            return self.visit(node.left_node) * self.visit(node.right_node)
        elif node.operation == pt.DIVISION:
            return self.visit(node.left_node) / self.visit(node.right_node)

    def visit_IntegerNumber(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)
