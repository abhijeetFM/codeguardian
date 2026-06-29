from analyzers.dependency_analyzer import (
    DependencyAnalyzer
)

from rules.architecture_validator import (
    ArchitectureValidator
)

dependencies = (
    DependencyAnalyzer()
    .analyze_project("sample_project")
)

violations = (
    ArchitectureValidator()
    .validate(dependencies)
)

for violation in violations:

    print(
        violation.source_file,
        "cannot access",
        violation.target_layer
    )