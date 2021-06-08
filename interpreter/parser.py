# Analisador de Pascal implementado em Python
# Autor: GabrielBonagio <gabriel.bonagio16@gmail.com>
# Data: 8/6/2021

from . import pascal_tokens as pt
from . import nodes


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        # Levanta uma exceção quando o token não faz parte da sintaxe.
        raise Exception('Sintaxe inválida')

    def eat(self, token_type):
        # Compara o tipo de self.current_token com o token_type. Se os tipos
        #  baterem, consome self.current_token e pega o próximo token do
        #  lexer, chamando self.lexer.get_next_token. Caso contrário, chama
        #  self.error.

        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def parse(self):
        # Inicia a cadeia de análise léxica.
        return self.expression()

    def expression(self):
        # expression: term {(PLUS | MINUS) term};
        # term: signed-factor {(STAR | SLASH) signed-factor};
        # signed-factor: [PLUS | MINUS] factor;
        # factor: "(" expression ")" | integer;

        node = self.term()

        while self.current_token.type in (pt.PLUS, pt.MINUS):
            current_token = self.current_token

            if current_token.type == pt.PLUS:
                self.eat(pt.PLUS)
            elif current_token.type == pt.MINUS:
                self.eat(pt.MINUS)

            node = nodes.BinaryOperation(
                left_node=node,
                operation=current_token.type,
                right_node=self.term()
            )

        return node

    def term(self):
        # term: signed-factor {(STAR | SLASH) signed-factor};
        # signed-factor: [PLUS | MINUS] factor
        # factor: "(" expression ")" | integer;

        node = self.signed_factor()

        while self.current_token.type in (pt.STAR, pt.SLASH):
            current_token = self.current_token

            if current_token.type == pt.STAR:
                self.eat(pt.STAR)
            elif current_token.type == pt.SLASH:
                self.eat(pt.SLASH)

            node = nodes.BinaryOperation(
                left_node=node,
                operation=current_token.type,
                right_node=self.signed_factor()
            )

        return node

    def signed_factor(self):
        # signed-factor: [PLUS | MINUS] factor;
        # factor: "(" expression ")" | integer;

        if self.current_token.type in [pt.PLUS, pt.MINUS]:
            current_token = self.current_token
            if self.current_token.type == pt.PLUS:
                self.eat(pt.PLUS)
            elif current_token.type == pt.MINUS:
                self.eat(pt.MINUS)

            node = nodes.UnaryOperation(
                operation=current_token.type,
                operand_node=self.factor()
            )
        else:
            node = self.factor()

        return node

    def factor(self):
        # factor: "(" expression ")" | integer;

        if self.current_token.type == pt.INTEGER:
            node = nodes.IntegerNumber(self.current_token)
            self.eat(pt.INTEGER)
        elif self.current_token.type == pt.LEFT_PAREN:
            self.eat(pt.LEFT_PAREN)
            node = self.expression()
            self.eat(pt.RIGHT_PAREN)

        return node
