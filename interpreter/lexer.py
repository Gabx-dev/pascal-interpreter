# Lexer de Pascal
# Autor: GabrielBonagio <gabriel.bonagio16@gmail.com>
# Data: 8/6/2021

from . import pascal_tokens as pt


class Lexer:
    def __init__(self, text):
        # Texto a ser interpretado.
        self.text = text

        # Um índice em self.text.
        self.pos = 0

        if len(self.text) > 0:
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def error(self):
        # Levanta uma exceção caso não tenha sido possível transformar a entrada em um token.
        raise Exception('Caractere inválido')

    def advance(self):
        # Caminha pelos caracteres da entrada.
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def whitespace(self):
        # Salta espaços.
        while (self.current_char is not None and
        self.current_char.isspace()):
            self.advance()

    def integer(self):
        # Retorna um token de número inteiro.
        result = str()

        while (self.current_char is not None and
        self.current_char.isdigit()):
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        '''Analisador léxico

        Quebra a entrada em tokens.'''

        while self.current_char is not None:
            if self.current_char.isspace():
                self.whitespace()
                continue
            elif self.current_char.isdigit():
                return pt.Token(pt.INTEGER, self.integer())
            elif self.current_char == '+':
                current_token = pt.Token(pt.PLUS, self.current_char)
                self.advance()
                return current_token
            elif self.current_char == '-':
                current_token = pt.Token(pt.MINUS, self.current_char)
                self.advance()
                return current_token
            elif self.current_char == '*':
                current_token = pt.Token(pt.STAR, self.current_char)
                self.advance()
                return current_token
            elif self.current_char == '/':
                current_token = pt.Token(pt.SLASH, self.current_char)
                self.advance()
                return current_token
            elif self.current_char == '(':
                current_token = pt.Token(pt.LEFT_PAREN, self.current_char)
                self.advance()
                return current_token
            elif self.current_char == ')':
                current_token = pt.Token(pt.RIGHT_PAREN, self.current_char)
                self.advance()
                return current_token
            else:
                self.error()

        return pt.Token(pt.EOF, None)
