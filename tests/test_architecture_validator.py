from rules.architecture_validator import (
    ArchitectureValidator
)


class FakeDependency:

    def __init__(
        self,
        source_file,
        target_module
    ):

        self.source_file = source_file
        self.target_module = target_module


def test_architecture_validator_detects_forbidden_dependency():

    dependency = FakeDependency(
        "sample_project.controllers.user_controller",
        "sample_project.repositories.user_repository"
    )

    validator = ArchitectureValidator()

    violations = validator.validate(
        [dependency]
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