from pathlib import Path

IGNORE_DIRS = {
    ".venv",
    ".git",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
}


def discover_files(project_path, extensions) -> list[Path]:
    project_path = Path(project_path)

    files = []

    for file in project_path.rglob("*"):

        if any(part in IGNORE_DIRS for part in file.parts):
            continue

        if file.is_file() and file.suffix in extensions:
            files.append(file)

    return files