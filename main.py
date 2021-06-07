# Executa o interpretador

from interpreter import Interpreter
from lexer import Lexer


def main():
    while 1:
        try:
            text = input('Pascal > ')
        except (EOFError, KeyboardInterrupt):
            break
        
        if not text:
            continue

        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.parse()
        print(result)


if __name__ == '__main__':
    main()
