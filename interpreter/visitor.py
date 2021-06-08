# Visitante de nós da AST.
# Classe abstrata, herdada por interpreter.Interpreter.
# Implementa um método genérico que chama os métodos específicos implementados pelas classes herdeiras.
# E implementa um método genérico que trata visitas não definidas.

class NodeVisitor:
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visitor)
        return visitor(node)

    def generic_visitor(self, node):
        raise Exception("No visitor named 'visit_" + type(node).__name__ + "'")
