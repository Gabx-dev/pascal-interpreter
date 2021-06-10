# Analisador de Pascal implementado em Python
# Autor: GabrielBonagio <gabriel.bonagio16@gmail.com>
# Data: 8/6/2021

from . import pascal_tokens as pt
from . import nodes
from .lexer import Lexer


class Parser:
    def __init__(self, text):
        self.lexer = Lexer(text)
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
        tree = self.program()

        if self.current_token.type != pt.EOF:
            self.error()

        return tree

    def program(self):
        # program: compound-statement DOT;

        node = self.compound_statement()
        self.eat(pt.DOT)

        return node

    def compound_statement(self):
        # compound-statement: BEGIN statement-list END;

        self.eat(pt.BEGIN)
        statements = self.statement_list()
        root = nodes.CompoundStatement(statements)
        self.eat(pt.END)

        return root

    def statement_list(self):
        # statement-list: statement {SEMI statement};

        statements = [self.statement()]

        while self.current_token.type == pt.SEMI:
            self.eat(pt.SEMI)
            statements.append(self.statement())

        if self.current_token.type == pt.IDENTIFIER:
            self.error()

        return statements

    def statement(self):
        # statement: compound-statement | assignment-statement | empty-statement;

        if self.current_token.type == pt.BEGIN:
            node = self.compound_statement()
        elif self.current_token.type == pt.IDENTIFIER:
            node = self.assignment_statement()
        else:
            node = self.empty_statement()

        return node

    def assignment_statement(self):
        # assignment-statement: variable ASSIGN expression;

        left = self.variable()
        token = self.current_token
        self.eat(pt.ASSIGN)
        right = self.expression()

        node = nodes.AssignmentOperation(
            left_node=left,
            operation=token.type,
            right_node=right
        )

        return node

    def empty_statement(self):
        # empty-statement: ;

        return nodes.NoOp()

    def variable(self):
        # variable: IDENTIFIER;

        node = nodes.Variable(self.current_token.value)
        self.eat(pt.IDENTIFIER)
        return node

    def expression(self):
        # expression: term {(PLUS | MINUS) term};

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

        node = self.factor()

        while self.current_token.type in (pt.STAR, pt.SLASH):
            current_token = self.current_token

            if current_token.type == pt.STAR:
                self.eat(pt.STAR)
            elif current_token.type == pt.SLASH:
                self.eat(pt.SLASH)

            node = nodes.BinaryOperation(
                left_node=node,
                operation=current_token.type,
                right_node=self.factor()
            )

        return node

    def factor(self):
        # factor: (PLUS | MINUS) factor | "(" expression ")" | integer | variable;

        if self.current_token.type == pt.INTEGER:
            node = nodes.IntegerNumber(self.current_token)
            self.eat(pt.INTEGER)
        elif self.current_token.type == pt.LEFT_PAREN:
            self.eat(pt.LEFT_PAREN)
            node = self.expression()
            self.eat(pt.RIGHT_PAREN)
        elif self.current_token.type in [pt.PLUS, pt.MINUS]:
            current_token = self.current_token
            if self.current_token == pt.PLUS:
                self.eat(pt.PLUS)
            elif self.current_token.type == pt.MINUS:
                self.eat(pt.MINUS)

            node = nodes.UnaryOperation(
                operation=current_token.type,
                operand_node=self.factor()
            )
        elif self.current_token.type == pt.IDENTIFIER:
            node = self.variable()

        return node
