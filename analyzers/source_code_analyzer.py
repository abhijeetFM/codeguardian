import ast

from pathlib import Path

from src.discovery.finder import discover_files
from src.parser.ts_parser import parse_typescript

from src.extractor.class_extractor import (
    ClassExtractor
)

from src.extractor.function_extractor import (
    functionExtractor
)

from src.extractor.import_extractor import (
    importExtractor
)

from src.extractor.python_function_extractor import (
    PythonFunctionExtractor
)

from src.extractor.python_class_extractor import (
    PythonClassExtractor
)

from src.extractor.python_imports_extractor import (
    PythonImportExtractor
)

from src.tree.Walker import walk


class SourceCodeAnalyzer:

    def analyze_python_file(
        self,
        file_path
    ):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            source = file.read()

        tree = ast.parse(source)

        class_extractor = (
            PythonClassExtractor()
        )
        class_extractor.extract(tree)

        function_extractor = (
            PythonFunctionExtractor()
        )
        function_extractor.extract(tree)

        import_extractor = (
            PythonImportExtractor()
        )
        import_extractor.extract(tree)

        return {
            "file": str(file_path),
            "classes": class_extractor.classes,
            "functions": function_extractor.functions,
            "imports": import_extractor.imports
        }

    def analyze_ts_js_file(
        self,
        file_path
    ):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            source = file.read()

        tree = parse_typescript(
            source
        )

        class_extractor = (
            ClassExtractor()
        )

        function_extractor = (
            functionExtractor()
        )

        import_extractor = (
            importExtractor()
        )

        walk(
            tree.root_node,
            class_extractor.visit
        )

        walk(
            tree.root_node,
            function_extractor.visit
        )

        walk(
            tree.root_node,
            import_extractor.visit
        )

        return {
            "file": str(file_path),
            "classes": class_extractor.classes,
            "functions": function_extractor.function,
            "imports": import_extractor.imports
        }

    def analyze(
        self,
        path
    ):

        results = []

        files = discover_files(
            Path(path),
            {
                ".py",
                ".ts",
                ".js"
            }
        )

        for file_path in files:

            if file_path.suffix == ".py":

                results.append(
                    self.analyze_python_file(
                        file_path
                    )
                )

            else:

                results.append(
                    self.analyze_ts_js_file(
                        file_path
                    )
                )

        return results