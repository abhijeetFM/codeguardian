from analyzers.dependency_analyzer import DependencyAnalyzer
from rules.architecture_validator import ArchitectureValidator


dependencies = (
    DependencyAnalyzer()
    .analyze_project(".")
)

validator = ArchitectureValidator()

print("\nForbidden Rules:")
print(validator.forbidden_dependencies)

print("\nDependencies:\n")

for dep in dependencies:

    source_layer = validator.get_layer(
        dep.source_file
    )

    target_layer = validator.get_layer(
        dep.target_module
    )

    print(
        dep.source_file,
        "=>",
        source_layer,
        "|",
        dep.target_module,
        "=>",
        target_layer
    )

violations = validator.validate(dependencies)

print("\nViolations:\n")

for v in violations:

    print(
        v.source_file,
        "->",
        v.source_layer,
        "->",
        v.target_layer
    )