# Lexer para a implementação de interpretador de Pascal
# Autor: GabrielBonagio <gabriel.bonagio16@gmail.com>
# Data: 6/6/2021

import token


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
                return token.Token(token.INTEGER, self.integer())
            elif self.current_char == '+':
                token_instance = token.Token(token.ADDITION, self.current_char)
                self.advance()
                return token_instance
            elif self.current_char == '-':
                token_instance = token.Token(token.SUBTRACTION, self.current_char)
                self.advance()
                return token_instance
            elif self.current_char == '*':
                token_instance = token.Token(token.MULTIPLICATION, self.current_char)
                self.advance()
                return token_instance
            elif self.current_char == '/':
                token_instance = token.Token(token.DIVISION, self.current_char)
                self.advance()
                return token_instance
            else:
                self.error()

        return token.Token(token.EOF, None)
