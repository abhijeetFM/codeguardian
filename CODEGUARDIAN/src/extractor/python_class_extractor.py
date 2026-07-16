import ast


class PythonClassExtractor:

    def __init__(self):

        self.classes = []

    def extract( self,tree):
        for node in ast.walk(tree):
            if isinstance(node,ast.ClassDef):
                self.classes.append(node.name)