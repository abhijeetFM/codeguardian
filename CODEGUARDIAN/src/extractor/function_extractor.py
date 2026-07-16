from  tree_sitter import Node

from CODEGUARDIAN.src.tree.Walker import walk


class functionExtractor:
    def __init__(self):
        self.function =[]

    def visit(self,node):
        if node.type =="function_declaration":
            name_node =node.child_by_field_name("name")

            if name_node:
                self.function.append(name_node.text.decode("utf8"))


