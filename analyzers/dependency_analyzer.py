import ast
import os

from config.config_loader import ConfigLoader

from src.parser.ts_parser import (
    parse_typescript
)

from src.tree.Walker import walk

from utils.ast_cache import ASTCache
class Dependency:

    def __init__(
        self,
        source_file,
        target_module
    ):

        self.source_file = source_file
        self.target_module = target_module


class DependencyAnalyzer:

    def __init__(self):

        self.config = ConfigLoader.load()

        self.supported_extensions = set(
            self.config["supported_extensions"]
        )

    def analyze_python_file(
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
        ) as file:

            source = file.read()
        try:
           tree = ASTCache.get_tree(
           file_path,
           source
           )
        except SyntaxError:
            return []

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

    def analyze_ts_js_file(
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
            .replace(".ts", "")
            .replace(".js", "")
            .replace(os.sep, ".")
        )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            source = file.read()
        try:
            tree = ASTCache.get_tree(
             file_path,
             source
            )
        except Exception:
            return []
        
        if tree.root_node.has_error:
            return []

        def visit(node):

            if node.type != "import_statement":

                return

            source_node = node.child_by_field_name(
                "source"
            )

            if not source_node:

                return

            imported_module = (
                source_node.text
                .decode("utf8")
                .replace('"', "")
                .replace("'", "")
            )
            if imported_module.startswith("./"):

                current_directory = ".".join(
                    module_name.split(".")[:-1]
                )

                imported_module = (
                    current_directory
                    + "."
                    + imported_module[2:]
                )

                imported_module = imported_module.replace(
                    "/",
                    "."
                )

            dependencies.append(

                Dependency(
                    module_name,
                    imported_module
                )
            )

        walk(
            tree.root_node,
            visit
        )

        return dependencies

    def analyze_project(
        self,
        project_path
    ):

        dependencies = []

       

        ignore_dirs = set(
            self.config[
                "ignored_directories"
            ]
        )

        for root, dirs, files in os.walk(project_path):

            dirs[:] = [

                d for d in dirs

                if d not in ignore_dirs
            ]

            for file in files:

                extension = os.path.splitext(
                    file
                )[1]

                if (
                    extension
                    not in self.supported_extensions
                ):

                    continue

                file_path = os.path.join(
                    root,
                    file
                )

                if extension == ".py":

                    dependencies.extend(

                        self.analyze_python_file(
                            file_path,
                            project_path
                        )
                    )

                elif extension in {

                    ".ts",
                    ".js"
                }:

                    dependencies.extend(

                        self.analyze_ts_js_file(
                            file_path,
                            project_path
                        )
                    )

        return dependencies