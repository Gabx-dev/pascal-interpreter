# Parser de Pascal implementado em Python
# Autor: GabrielBonagio <gabriel.bonagio16@gmail.com>
# Data: 7/6/2021

from . import pascal_tokens as pt
from . import nodes


class Parser(object):
    def __init__(self, lexer):
        super().__init__()
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Sintaxe inválida')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def parse(self):
        return self.expression()

    def expression(self):
        '''expression: term {(ADDITION | SUBTRACTION) term};'''
        node = self.term()

        while self.current_token.type in (pt.ADDITION, pt.SUBTRACTION):
            current_token = self.current_token

            if current_token.type == pt.ADDITION:
                self.eat(pt.ADDITION)
            elif current_token.type == pt.SUBTRACTION:
                self.eat(pt.SUBTRACTION)
            
            node = nodes.BinaryOperation(
                left_node=node,
                operation=current_token.type,
                right_node=self.term()
            )

        return node

    def term(self):
        '''term: factor {(MULTIPLICATION | DIVISION) factor};'''
        node = self.factor()

        while self.current_token.type in (pt.MULTIPLICATION, pt.DIVISION):
            current_token = self.current_token

            if current_token.type == pt.MULTIPLICATION:
                self.eat(pt.MULTIPLICATION)
            elif current_token.type == pt.DIVISION:
                self.eat(pt.DIVISION)
            
            node = nodes.BinaryOperation(
                left_node=node,
                operation=current_token.type,
                right_node=self.factor()
            )

        return node

    def factor(self):
        '''factor: "(" expression ")" | integer;'''
        current_token = self.current_token
        if current_token.type == pt.INTEGER:
            node = nodes.IntegerNumber(current_token)
            self.eat(pt.INTEGER)
        elif current_token.type == pt.LEFT_PAREN:
            self.eat(pt.LEFT_PAREN)
            node = self.expression()
            self.eat(pt.RIGHT_PAREN)
            return node
