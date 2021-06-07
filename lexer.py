# Lexer para a implementação de interpretador de Pascal
# Autor: GabrielBonagio <gabriel.bonagio16@gmail.com>
# Data: 6/6/2021

import pascal_tokens as pt


class Lexer(object):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.pos = 0
        if len(self.text) > 0:
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def error(self):
        raise Exception('Caractere inválido')
        
    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def whitespace(self):
        while (self.current_char is not None and
        self.current_char.isspace()):
            self.advance()

    def integer(self):
        result = str()

        while (self.current_char is not None and
        self.current_char.isdigit()):
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.whitespace()
                continue
            elif self.current_char.isdigit():
                return pt.Token(pt.INTEGER, self.integer())
            elif self.current_char == '+':
                current_token = pt.Token(pt.ADDITION, self.current_char)
                self.advance()
                return current_token
            elif self.current_char == '-':
                current_token = pt.Token(pt.SUBTRACTION, self.current_char)
                self.advance()
                return current_token
            elif self.current_char == '*':
                current_token = pt.Token(pt.MULTIPLICATION, self.current_char)
                self.advance()
                return current_token
            elif self.current_char == '/':
                current_token = pt.Token(pt.DIVISION, self.current_char)
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
