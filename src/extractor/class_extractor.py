# class_extractor.py

from tree_sitter import Node


def walk_tree(node: Node):

    print(node.type)

    for child in node.children:
        walk_tree(child)