import ast

from pathlib import Path

from src.parser.ts_parser import parse_typescript


class ASTCache:

    _cache = {}

    @classmethod
    def get_tree(
        cls,
        file_path,
        source
    ):

        file_path = str(
            Path(file_path).resolve()
        )

        cached_data = cls._cache.get(
            file_path
        )

        if (
            cached_data is not None
            and cached_data["source"] == source
        ):

            return cached_data["tree"]

        if file_path.endswith(".py"):

            tree = ast.parse(source)

        else:

            tree = parse_typescript(source)

        cls._cache[file_path] = {
            "source": source,
            "tree": tree
        }

        return tree