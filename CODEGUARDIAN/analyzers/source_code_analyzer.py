import ast

from pathlib import Path

from CODEGUARDIAN.src.discovery.finder import discover_files
from CODEGUARDIAN.src.parser.ts_parser import parse_typescript
from CODEGUARDIAN.utils.file_cache import FileCache
from CODEGUARDIAN.src.extractor.class_extractor import (
    ClassExtractor
)

from CODEGUARDIAN.src.extractor.function_extractor import (
    functionExtractor
)

from CODEGUARDIAN.src.extractor.import_extractor import (
    importExtractor
)

from CODEGUARDIAN.src.extractor.python_function_extractor import (
    PythonFunctionExtractor
)

from CODEGUARDIAN.src.extractor.python_class_extractor import (
    PythonClassExtractor
)

from CODEGUARDIAN.src.extractor.python_imports_extractor import (
    PythonImportExtractor
)

from CODEGUARDIAN.src.tree.Walker import walk
from CODEGUARDIAN.utils.ast_cache import ASTCache

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
        try:
            tree = ASTCache.get_tree(
            file_path,
            source
            )

        except SyntaxError:
            return None

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
        try:
            tree = ASTCache.get_tree(
            file_path,
            source
            )
        except Exception:
            return None
        
        if tree.root_node.has_error:
           return None

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

        files = FileCache.get_files(
            path,
         {
        ".py",
        ".ts",
        ".js"
         }
        )

        for file_path in files:

            if file_path.suffix == ".py":

                result = self.analyze_python_file(
                  file_path
                )

            else:

                result = self.analyze_ts_js_file(
                file_path
                )
            if result is not None:
                results.append(result)

        return results