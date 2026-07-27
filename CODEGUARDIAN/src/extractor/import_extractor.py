from tree_sitter import Node
from CODEGUARDIAN.src.tree.Walker import walk


class importExtractor:
    def __init__(self):
        self.imports =[]

    def visit(self, node):

      if node.type not in { "import_statement","export_statement"}:
         return
     

      source_node = node.child_by_field_name("source")

      if not source_node:
        return

      module = (
         source_node.text
         .decode("utf8")
         .replace('"', "")
         .replace("'", "")
        )

      self.imports.append(module)

      
      

  

