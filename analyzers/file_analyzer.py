import os

from config.config_loader import ConfigLoader


from utils.file_cache import FileCache


from src.discovery.finder import discover_files


class FileViolation:

    def __init__(
        self,
        file_path,
        line_count
    ):

        self.file_path = str(file_path)
        self.line_count = line_count


class FileAnalyzer:

    def __init__(
        self,
        max_lines=None
    ):

        config = ConfigLoader.load()

        if max_lines is None:

            max_lines = config[
                "max_file_lines"
            ]

        self.max_lines = max_lines
       

        self.supported_extensions = set(

            config[
                "supported_extensions"
            ]
        )

    def analyze(
        self,
        project_path
    ):

        violations = []

        files = FileCache.get_files(
         project_path,
         self.supported_extensions
        )

        for file_path in files:

         

                try:

                    with open(
                        file_path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        line_count = len(
                            f.readlines()
                        )

                    if (

                        line_count
                        > self.max_lines

                    ):

                        violations.append(

                            FileViolation(
                                str(file_path),
                                line_count
                            )
                        )

                except UnicodeDecodeError:

                    continue

        return violations