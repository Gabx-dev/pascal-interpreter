# Executa o interpretador

from interpreter.interpreter import Interpreter
from interpreter.lexer import Lexer
from interpreter.parser import Parser


def main():
    while 1:
        try:
            text = input('Pascal > ')
        except (EOFError, KeyboardInterrupt):
            break
        
        if not text:
            continue

        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        print(result)


if __name__ == '__main__':
    main()
