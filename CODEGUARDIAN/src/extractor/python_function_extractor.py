import ast


class PythonFunctionExtractor:

    def __init__(self):

        self.functions = []

    def extract( self,tree):

        for node in ast.walk(tree):

            if isinstance(node,ast.FunctionDef):

                self.functions.append( node.name)