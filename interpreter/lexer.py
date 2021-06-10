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

    def advance(self, ammount=1):
        # Caminha pelos caracteres da entrada.
        for _ in range(ammount):
            self.pos += 1

        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def peek(self):
        # Retorna o caractere na posição self.pos + 1 sem alterar self.pos se
        # self.pos + 1 for um índice válido dentro de self.text.
        peek_pos = self.pos + 1
        if peek_pos > len(self.text) - 1:
                return None
        return self.text[peek_pos]

    def whitespace(self):
        # Salta espaços.
        while (self.current_char is not None and
        self.current_char.isspace()):
            self.advance()

    def integer(self):
        # Retorna um token de número inteiro.
        result = ''

        while (self.current_char is not None and
        self.current_char.isdigit()):
            result += self.current_char
            self.advance()
        return pt.Token(
            type=pt.INTEGER,
            value=int(result)
        )

    def identifier(self):
        result = self.current_char
        self.advance()

        while (self.current_char is not None and
        self.current_char.isalnum()):
            result += self.current_char
            self.advance()

        token = pt.RESERVED_KEYWORDS.get(
            result,
            pt.Token(pt.IDENTIFIER, result)
        )

        return token

    def get_next_token(self):
        '''Analisador léxico

        Quebra a entrada em tokens.'''

        while self.current_char is not None:
            if self.current_char.isspace():
                self.whitespace()
                continue
            elif self.current_char.isdigit():
                return self.integer()
            elif self.current_char.isalpha():
                return self.identifier()
            elif self.current_char == '+':
                self.advance()
                return pt.Token(pt.PLUS, '+')
            elif self.current_char == '-':
                self.advance()
                return pt.Token(pt.MINUS, '-')
            elif self.current_char == '*':
                self.advance()
                return pt.Token(pt.STAR, '*')
            elif self.current_char == '/':
                self.advance()
                return pt.Token(pt.SLASH, '/')
            elif self.current_char == '(':
                self.advance()
                return pt.Token(pt.LEFT_PAREN, '(')
            elif self.current_char == ')':
                self.advance()
                return pt.Token(pt.RIGHT_PAREN, ')')
            elif self.current_char == ':' and self.peek() == '=':
                self.advance(2)
                return pt.Token(pt.ASSIGN, ':=')
            elif self.current_char == ';':
                self.advance()
                return pt.Token(pt.SEMI, ';')
            elif self.current_char == '.':
                self.advance()
                return pt.Token(pt.DOT, '.')
            else:
                self.error()

        return pt.Token(pt.EOF, None)
