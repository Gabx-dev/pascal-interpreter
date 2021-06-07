# Interpretador de Pascal implementado em Python
# Autor: GabrielBonagio <gabriel.bonagio16@gmail.com>
# Data: 6/6/2021

import token


class Interpreter(object):
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
        result = self.term()

        while self.current_token.type in (token.ADDITION, token.SUBTRACTION):
            current_token = self.current_token

            if current_token.type == token.ADDITION:
                self.eat(token.ADDITION)
                result += self.term()
            elif current_token.type == token.SUBTRACTION:
                self.eat(token.SUBTRACTION)
                result -= self.term()

        return result

    def term(self):
        '''term: factor {(MULTIPLICATION | DIVISION) factor};'''
        result = self.factor()

        while self.current_token.type in (token.MULTIPLICATION, token.DIVISION):
            current_token = self.current_token

            if current_token.type == token.MULTIPLICATION:
                self.eat(token.MULTIPLICATION)
                result *= self.factor()
            elif current_token.type == token.DIVISION:
                self.eat(token.DIVISION)
                result /= self.factor()
        return result

    def factor(self):
        '''factor: INTEGER;'''
        integer = self.current_token.value
        self.eat(token.INTEGER)
        return integer
