import ast
import os

from config.settings import MAX_FUNCTION_LINES


class FunctionViolation:
    def __init__(self,
                 function_name,
                 line_count):

        self.function_name = function_name
        self.line_count = line_count


class FunctionAnalyzer:

    def __init__(self,
                 max_lines=MAX_FUNCTION_LINES):
        self.max_lines = max_lines

    def analyze_file(self, file_path):

        violations = []

        with open(file_path,
                  "r",
                  encoding="utf-8") as f:

            source = f.read()

        tree = ast.parse(source)

        for node in ast.walk(tree):

            if isinstance(node,
                          ast.FunctionDef):

                length = (
                    node.end_lineno
                    - node.lineno
                    + 1
                )

                if length > self.max_lines:

                    violations.append(
                        FunctionViolation(
                            node.name,
                            length
                        )
                    )

        return violations
    
    def analyze_project(self, project_path):

        violations = []

        IGNORE_DIRS = {
            "venv",
            ".git",
            "__pycache__",
            ".pytest_cache"
        }

        for root, dirs, files in os.walk(project_path):

            dirs[:] = [
                d for d in dirs
                if d not in IGNORE_DIRS
            ]

            for file in files:

                if not file.endswith(".py"):
                    continue

                file_path = os.path.join(
                    root,
                    file
                )

                violations.extend(
                    self.analyze_file(file_path)
                )

        return violations