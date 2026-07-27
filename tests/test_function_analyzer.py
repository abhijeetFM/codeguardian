from CODEGUARDIAN.analyzers.function_analyzer import FunctionAnalyzer


def test_function_analyzer_detects_large_function(
    tmp_path
):

    test_file = tmp_path / "large_function.py"

    function_body = "\n".join(
        "    print('Hello')"
        for _ in range(60)
    )

    test_file.write_text(
        "def large_function():\n"
        + function_body,
        encoding="utf-8"
    )

    analyzer = FunctionAnalyzer(
        max_lines=50
    )

    violations = analyzer.analyze_python_file(
        test_file
    )

    assert len(violations) == 1

    assert (
        violations[0].function_name
        == "large_function"
    )

    assert (
        violations[0].line_count
        > analyzer.max_lines
    )