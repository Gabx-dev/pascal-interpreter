# Executa o interpretador

import sys
from interpreter.interpreter import Interpreter
from interpreter.lexer import Lexer
from interpreter.parser import Parser


def main():
    if len(sys.argv) > 1:
        source_path = sys.argv[1]
    else:
        source_path = input('Informe o caminho para o código fonte: ')

    with open(source_path, 'r') as source_file:
        source = source_file.read()

        interpreter = Interpreter(source)
        interpreter.interpret()

        print(interpreter.global_scope)

if __name__ == '__main__':
    main()
