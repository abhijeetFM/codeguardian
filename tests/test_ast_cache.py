from utils.ast_cache import ASTCache


def test_ast_cache_returns_same_tree():

    file_path = "sample.py"

    source = """
def greet():
    return "Hello"
"""

    first_tree = ASTCache.get_tree(
        file_path,
        source
    )

    second_tree = ASTCache.get_tree(
        file_path,
        source
    )

    assert first_tree is second_tree


def test_ast_cache_updates_when_source_changes():

    file_path = "sample.py"

    first_source = """
def greet():
    return "Hello"
"""

    second_source = """
def greet():
    return "Hello World"
"""

    first_tree = ASTCache.get_tree(
        file_path,
        first_source
    )

    second_tree = ASTCache.get_tree(
        file_path,
        second_source
    )

    assert first_tree is not second_tree