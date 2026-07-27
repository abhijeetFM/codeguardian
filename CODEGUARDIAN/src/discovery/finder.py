from pathlib import Path
import os

IGNORE_DIRS = {
    "venv",
    ".venv",
    ".git",
    "__pycache__",
    ".pytest_cache",
    "node_modules",
    "dist",
    "build",
    "tests",
}


def discover_files(project_path, extensions):

    project_path = Path(project_path)

    files = []

    for root, dirs, filenames in os.walk(project_path):

        # Ignore predefined directories
        dirs[:] = [
            d for d in dirs
            if d not in IGNORE_DIRS
        ]

        # Ignore Python virtual environments
        dirs[:] = [
            d for d in dirs
            if not (Path(root) / d / "pyvenv.cfg").exists()
        ]

        for filename in filenames:

            file_path = Path(root) / filename

            if filename.startswith("test_"):
                continue

            if (
                file_path.is_file()
                and file_path.suffix in extensions
            ):
                files.append(file_path)

    return files