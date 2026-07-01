from pathlib import Path

from config.config_loader import ConfigLoader

from src.discovery.finder import discover_files
from src.parser.ts_parser import parse_typescript

from src.extractor.class_extractor import (
    ClassExtractor
)

from src.extractor.function_extractor import (
    functionExtractor
)

from src.tree.Walker import walk


class SourceCodeAnalyzer:

    def analyze(self, path):

        results = []

        config = ConfigLoader.load()

        ignored = set(
            config["ignored_directories"]
        )

        files = discover_files(
            Path(path)
        )

        for file_path in files:

            if any(
                part in ignored
                for part in file_path.parts
            ):
                continue

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

            walk(
                tree.root_node,
                class_extractor.visit
            )

            walk(
                tree.root_node,
                function_extractor.visit
            )

            results.append(
                {
                    "file": str(file_path),
                    "classes":
                        class_extractor.classes,
                    "functions":
                        function_extractor.function
                }
            )

        return results