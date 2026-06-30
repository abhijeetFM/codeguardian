import ast
import os

from config.config_loader import ConfigLoader


class Dependency:

    def __init__(
        self,
        source_file,
        target_module
    ):

        self.source_file = source_file
        self.target_module = target_module


class DependencyAnalyzer:

    def analyze_file(
        self,
        file_path,
        project_root
    ):

        dependencies = []

        relative_path = os.path.relpath(
            file_path,
            project_root
        )

        module_name = (
            relative_path
            .replace(".py", "")
            .replace(os.sep, ".")
        )

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

                if node.module:

                    dependencies.append(
                        Dependency(
                            module_name,
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
                            module_name,
                            imported.name
                        )
                    )

        return dependencies

    def analyze_project(
        self,
        project_path
    ):

        dependencies = []

        config = ConfigLoader.load()

        ignore_dirs = set(
            config["ignored_directories"]
        )

        for root, dirs, files in os.walk(project_path):

            dirs[:] = [
                d for d in dirs
                if d not in ignore_dirs
            ]

            for file in files:

                if not file.endswith(".py"):
                    continue

                file_path = os.path.join(
                    root,
                    file
                )

                dependencies.extend(
                    self.analyze_file(
                        file_path,
                        project_path
                    )
                )

        return dependencies