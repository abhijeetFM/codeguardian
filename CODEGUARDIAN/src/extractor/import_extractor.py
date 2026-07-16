from tree_sitter import Node
from CODEGUARDIAN.src.tree.Walker import walk


class importExtractor:
    def __init__(self):
        self.imports =[]

    def visit(self, node):

      if node.type != "import_statement":
          return

      for child in node.children:

          if child.type == "string":

              self.imports.append(
                child.text.decode("utf8").strip('"')
            )

  

