# Interpretador de Pascal escrito em Python
# Autor: GabrielBonagio <gabriel.bonagio16@gmail.com>

from . import pascal_tokens as pt
from . import visitor
from .parser import Parser


class Interpreter(visitor.NodeVisitor):
    def __init__(self, text):
        self.parser = Parser(text)
        self.global_scope = dict()

    def visit_BinaryOperation(self, node):
        if node.operation == pt.PLUS:
            return self.visit(node.left_node) + self.visit(node.right_node)
        elif node.operation == pt.MINUS:
            return self.visit(node.left_node) - self.visit(node.right_node)
        elif node.operation == pt.STAR:
            return self.visit(node.left_node) * self.visit(node.right_node)
        elif node.operation == pt.SLASH:
            return self.visit(node.left_node) / self.visit(node.right_node)

    def visit_UnaryOperation(self, node):
        if node.operation == pt.PLUS:
            return +self.visit(node.operand_node)
        elif node.operation == pt.MINUS:
            return -self.visit(node.operand_node)

    def visit_IntegerNumber(self, node):
        return node.value

    def visit_CompoundStatement(self, node):
        for child in node.children:
            self.visit(child)

    def visit_AssignmentOperation(self, node):
        name = node.left_node.name
        value = self.visit(node.right_node)
        self.global_scope[name] = value

    def visit_Variable(self, node):
        value = self.global_scope.get(node.name)

        if value is None:
            raise NameError(repr(node.name))
        else:
            return value

    def visit_NoOp(self, node):
        pass

    def interpret(self):
        tree = self.parser.parse()
        self.visit(tree)
