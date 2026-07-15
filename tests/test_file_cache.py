from utils.file_cache import FileCache


def test_file_cache_returns_same_result():

    extensions = {
        ".py",
        ".ts",
        ".js"
    }

    first_result = FileCache.get_files(
        ".",
        extensions
    )

    second_result = FileCache.get_files(
        ".",
        extensions
    )

    assert first_result is second_result