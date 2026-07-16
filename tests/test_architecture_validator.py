from analyzers.dependency_analyzer import DependencyAnalyzer
from rules.architecture_validator import ArchitectureValidator


def test_architecture_validator():

    dependencies = (
        DependencyAnalyzer()
        .analyze_project(".")
    )

    validator = ArchitectureValidator()

    violations = validator.validate(
        dependencies
    )

    assert len(violations) == 1

    assert (
        violations[0].source_layer
        == "controllers"
    )

    assert (
        violations[0].target_layer
        == "repositories"
    )