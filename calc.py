# Uma implementação de interpretador de Pascal escrita em Python
# Autor: GabrielBonagio <gabriel.bonagio16@gmail.com>
# Data: 4/6/2021

# Tipos de tokens
INTEGER = 'INTEGER'
MULT = 'MULT'
DIV = 'DIV'
EOF = 'EOF'


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        'Representação em string da instância de token.'

        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        # self.pos é um índice em self.text.
        self.pos = 0
        self.current_token = None
        if len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def error(self):
        'Levanta uma exceção caso a entrada não possa ser processada.'
        raise Exception('Error parsing input')

    def advance(self):
        '''Avança o ponteiro de posição e define a variável self.current_char.'''
        self.pos += 1
        
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while (self.current_char is not None and
        self.current_char.isspace()):
            self.advance()
    
    def integer(self):
        '''Retorna um inteiro de múltiplos dígitos consumido da entrada.'''
        result = ''
        while (self.current_char is not None and
        self.current_char.isdigit()):
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        '''Analisador léxico.'''
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            elif self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            elif self.current_char == '*':
                self.advance()
                return Token(MULT, self.current_char)
            elif self.current_char == '/':
                self.advance()
                return Token(DIV, self.current_char)
            else:
                self.error()
            
        return Token(EOF, None)

    def eat(self, token_type):
        # Compara o tipo do token atual com o token passado e se eles combinarem,
        # consome o token atual e passa o próximo token para self.current_token.
        # Caso contrário, levanta uma exceção.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def term(self):
        '''Retorna o valor de um token de inteiro.'''
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        '''Parser/interpretador.'''
        # Define o token atual como o primeiro token na entrada.
        self.current_token = self.get_next_token()

        result = self.term()
        while self.current_token.type in (MULT, DIV):
            token = self.current_token

            if token.type == MULT:
                self.eat(MULT)
                result *= self.term()
            elif token.type == DIV:
                self.eat(DIV)
                divisor = self.term()
                if divisor:
                    result /= divisor
                else:  # Division by 0.
                    raise ZeroDivisionError

        return result

def main():
    while 1:
        try:
            text = input('Calc > ')
        except (EOFError, KeyboardInterrupt):
            break
        
        if not text:
            continue

        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
