# Interpretador de Pascal implementado em Python
# Autor: GabrielBonagio <gabriel.bonagio16@gmail.com>
# Data: 6/6/2021

import pascal_tokens as pt


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

        while self.current_token.type in (pt.ADDITION, pt.SUBTRACTION):
            current_token = self.current_token

            if current_token.type == pt.ADDITION:
                self.eat(pt.ADDITION)
                result += self.term()
            elif current_token.type == pt.SUBTRACTION:
                self.eat(pt.SUBTRACTION)
                result -= self.term()

        return result

    def term(self):
        '''term: factor {(MULTIPLICATION | DIVISION) factor};'''
        result = self.factor()

        while self.current_token.type in (pt.MULTIPLICATION, pt.DIVISION):
            current_token = self.current_token

            if current_token.type == pt.MULTIPLICATION:
                self.eat(pt.MULTIPLICATION)
                result *= self.factor()
            elif current_token.type == pt.DIVISION:
                self.eat(pt.DIVISION)
                result /= self.factor()
        return result

    def factor(self):
        '''factor: "(" expression ")" | integer;'''
        if self.current_token.type == pt.INTEGER:
            integer = self.current_token.value
            self.eat(pt.INTEGER)
            return integer
        elif self.current_token.type == pt.LEFT_PAREN:
            self.eat(pt.LEFT_PAREN)
            result = self.expression()
            self.eat(pt.RIGHT_PAREN)
            return result
