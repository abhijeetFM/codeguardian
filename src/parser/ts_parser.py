from tree_sitter import Language, Parser
from tree_sitter_typescript import language_typescript


def parse_typescript(source_code: str):
    parser = Parser()

    language = Language(language_typescript())

    parser.language = language

    tree = parser.parse(bytes(source_code, "utf8"))

    return tree