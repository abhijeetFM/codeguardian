import ast
import os

from config.config_loader import ConfigLoader
from src.discovery.finder import discover_files

from src.parser.ts_parser import (
    parse_typescript
)

from src.tree.Walker import walk


class FunctionViolation:

    def __init__(
        self,
        function_name,
        line_count
    ):

        self.function_name = function_name
        self.line_count = line_count


class FunctionAnalyzer:

    def __init__(
        self,
        max_lines=None
    ):

        config = ConfigLoader.load()

        if max_lines is None:

            max_lines = config[
                "max_function_lines"
            ]

        self.max_lines = max_lines

        self.supported_extensions = set(
            config[
                "supported_extensions"
            ]
        )

    def analyze_python_file(
        self,
        file_path
    ):

        violations = []

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            source = f.read()

        tree = ast.parse(source)

        for node in ast.walk(tree):

            if isinstance(
                node,
                ast.FunctionDef
            ):

                line_count = (
                    node.end_lineno
                    - node.lineno
                    + 1
                )

                if line_count > self.max_lines:

                    violations.append(

                        FunctionViolation(
                            node.name,
                            line_count
                        )
                    )

        return violations

    def analyze_ts_js_file(
        self,
        file_path
    ):

        violations = []

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            source = file.read()

        tree = parse_typescript(
            source
        )

        def visit(node):

            if node.type != "function_declaration":

                return

            name_node = node.child_by_field_name(
                "name"
            )

            if not name_node:

                return

            function_name = (
                name_node.text.decode("utf8")
            )

            line_count = (
                node.end_point[0]
                - node.start_point[0]
                + 1
            )

            if line_count > self.max_lines:

                violations.append(

                    FunctionViolation(
                        function_name,
                        line_count
                    )
                )

        walk(
            tree.root_node,
            visit
        )

        return violations

    def analyze_project(
      self,
      project_path 
      ):

      violations = []

      files = discover_files(
        project_path,
        self.supported_extensions
     )

      for file_path in files:

        extension = file_path.suffix

        if extension == ".py":

            violations.extend(
                self.analyze_python_file(
                    file_path
                )
            )

        elif extension in {
            ".ts",
            ".js"
        }:

            violations.extend(
                self.analyze_ts_js_file(
                    file_path
                )
            )

      return violations