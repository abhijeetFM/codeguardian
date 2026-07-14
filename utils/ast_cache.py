import ast

from pathlib import Path

from src.parser.ts_parser import parse_typescript


class ASTCache:

    _cache = {}

    @classmethod
    def get_tree(cls, file_path, source):

        file_path = str(Path(file_path).resolve())

        if file_path not in cls._cache:

           

            if file_path.endswith(".py"):

                cls._cache[file_path] = ast.parse(source)

            else:

                cls._cache[file_path] = parse_typescript(source)
        

        return cls._cache[file_path]