from analyzers.function_analyzer import FunctionAnalyzer

analyzer = FunctionAnalyzer()

violations = analyzer.analyze_file("large_function.py")

for violation in violations:
    print(
        f"{violation.function_name} "
        f"({violation.line_count} lines)"
    )