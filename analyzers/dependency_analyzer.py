import ast
import os

class Dependency:

    def __init__(self,
                 source_file,
                 target_module):

        self.source_file = source_file
        self.target_module = target_module


class DependencyAnalyzer:

    def analyze_file(self, file_path):

        dependencies = []

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
                ast.ImportFrom
            ):

                dependencies.append(
                    Dependency(
                        file_path,
                        node.module
                    )
                )

            elif isinstance(
                node,
                ast.Import
            ):

                for imported in node.names:

                    dependencies.append(
                        Dependency(
                            file_path,
                            imported.name
                        )
                    )

        return dependencies

    def analyze_project(self, project_path):

        dependencies = []

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

                dependencies.extend(
                    self.analyze_file(file_path)
                )

        return dependencies