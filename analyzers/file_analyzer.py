import os
from config.settings import MAX_FILE_LINES

IGNORE_DIRS = {
        "venv",
        ".git",
        "__pycache__",
        ".pytest_cache"
        }
class FileViolation:
    def __init__(self, file_path, line_count):
        self.file_path = file_path
        self.line_count = line_count


class FileAnalyzer:

    def __init__(self, max_lines=MAX_FILE_LINES):
        self.max_lines = max_lines

    def analyze(self, project_path):
        violations = []
        

        for root, dirs, files in os.walk(project_path):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

            for file in files:

                if not file.endswith(".py"):
                    continue

                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    line_count = len(f.readlines())

                if line_count > self.max_lines:
                    violations.append(
                        FileViolation(
                            file_path=file_path,
                            line_count=line_count
                        )
                    )

        return violations