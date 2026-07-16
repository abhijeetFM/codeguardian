from tree_sitter import Node



def walk(node , callbreak):
    callbreak(node)


    for child in node.children:
        walk(child,callbreak)