from analyzers.function_analyzer import FunctionAnalyzer

from analyzers.source_code_analyzer import SourceCodeAnalyzer


def test_malformed_typescript_is_skipped():

    analyzer = SourceCodeAnalyzer()

    result = analyzer.analyze_ts_js_file(
        "broken_file.ts"
    )

    assert result is None


def test_malformed_python_does_not_crash():

    analyzer = FunctionAnalyzer()

    result = analyzer.analyze_python_file(
        "broken_file.py"
    )

    assert result == []