# Uma implementação de interpretador de Pascal escrita em Python
# Autor: GabrielBonagio <gabriel.bonagio16@gmail.com>
# Data: 4/6/2021

# Tipos de tokens
INTEGER = 'INTEGER'
PLUS = 'PLUS'
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

    def error(self):
        'Levanta uma exceção caso a entrada não possa ser processada.'
        raise Exception('Error parsing input')

    def get_next_token(self):
        '''Analisador léxico.'''
        text = self.text

        # Se a posição tiver passado do fim de text, então retorna EOF,
        # já que não há mais entrada pra processar.
        if self.pos > len(text) - 1:
            return Token(EOF, None)
        
        # Pega o caractere na posição self.pos e decide que token criar baseado no valor do caractere.
        current_char = text[self.pos]

        # Se for um número, converte em um inteiro, cria um token do tipo INTEGER,
        # incrementa self.pos e retorna o token criado.
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token
        
        # Se for um +, cria um token do tipo PLUS, incrementa self.pos
        # e retorna o token criado.
        elif current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        else:
            self.error()
    
    def eat(self, token_type):
        # Compara o tipo do token atual com o token passado e se eles combinarem,
        # come o token atual e passa o próximo token para self.current_token.
        # Caso contrário, levanta uma exceção.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        '''expr -> INTEGER PLUS INTEGER'''
        # Define o token atual como o primeiro token na entrada.
        self.current_token = self.get_next_token()

        # Esperamos que o token atual seja um inteiro de um dígito.
        left = self.current_token
        self.eat(INTEGER)

        # E depois um sinal de +.
        op = self.current_token
        self.eat(PLUS)

        # E por fim, outro inteiro de um dígito.
        right = self.current_token
        self.eat(INTEGER)

        # Depois da chamada acima, self.current_token é um EOF.
        # A operação foi concluída e o método pode retornar o resultado,
        # i.e., efetivamente somando 2 inteiros.
        result = left.value + right.value
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
