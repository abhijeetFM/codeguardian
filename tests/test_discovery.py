from pathlib import Path

from CODEGUARDIAN.src.discovery.finder import discover_files


def test_discover_files():

    extensions = {
        ".py",
        ".ts",
        ".js"
    }

    files = discover_files(
        Path("samples"),
        extensions
    )

    assert isinstance(
        files,
        list
    )

    assert len(files) > 0

    assert all(
        file.suffix in extensions
        for file in files
    )