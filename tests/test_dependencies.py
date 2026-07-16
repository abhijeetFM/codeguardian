from CODEGUARDIAN.analyzers.dependency_analyzer import DependencyAnalyzer


dependencies = (
    DependencyAnalyzer()
    .analyze_project(".")
)

print(f"\nFound {len(dependencies)} dependencies:\n")

for dep in dependencies:

    print(
        dep.source_file,
        "->",
        dep.target_module
    )