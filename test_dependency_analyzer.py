from analyzers.dependency_analyzer import (
    DependencyAnalyzer
)

analyzer = DependencyAnalyzer()

dependencies = analyzer.analyze_project(
    "sample_project"
)

for dep in dependencies:

    print(
        dep.source_file,
        "->",
        dep.target_module
    )