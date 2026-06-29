from tree_sitter import Node


def extract_classes(node: Node, classes: list[str]) -> None:
    if node.type == "class_declaration":
        name_node = node.child_by_field_name("name")

        if name_node:
            classes.append(name_node.text.decode("utf8"))

    for child in node.children:
        extract_classes(child, classes)