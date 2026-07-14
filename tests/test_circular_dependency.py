from analyzers.dependency_analyzer import (
    DependencyAnalyzer
)

from analyzers.circular_dependency_analyzer import (
    CircularDependencyAnalyzer
)


dependencies = (
    DependencyAnalyzer()
    .analyze_project(
        "sample_project"
    )
)

print("\nDependencies Found:\n")

for dep in dependencies:

    print(
        dep.source_file,
        "->",
        dep.target_module
    )

cycles = (
    CircularDependencyAnalyzer()
    .detect(dependencies)
)

if cycles:

    print(
        "\nCircular Dependencies Found:\n"
    )

    for cycle in cycles:

        print(
            " -> ".join(
                cycle.cycle
            )
        )

else:

    print(
        "No circular dependencies found."
    )