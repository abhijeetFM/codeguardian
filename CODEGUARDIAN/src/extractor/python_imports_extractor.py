import ast


class PythonImportExtractor:

    def __init__(self):

        self.imports = []

    def extract(self,tree):

        for node in ast.walk(tree):

            if isinstance(node,ast.Import):

                for alias in node.names:

                    self.imports.append(alias.name)

            elif isinstance(node,ast.ImportFrom):

                if node.module:

                    self.imports.append(node.module)