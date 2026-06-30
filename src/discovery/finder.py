from pathlib import Path


SUPPORTED_EXTENSIONS = {".ts", ".js"}


def discover_files(project_path: Path) -> list[Path]:
    files = []

    for file in project_path.rglob("*"):

        if file.is_file() and file.suffix in SUPPORTED_EXTENSIONS:
            files.append(file)

    return files