from rules.architecture_rules import (
    ALLOWED_DEPENDENCIES
)


class ArchitectureViolation:

    def __init__(
        self,
        source_file,
        source_layer,
        target_layer
    ):
        self.source_file = source_file
        self.source_layer = source_layer
        self.target_layer = target_layer


class ArchitectureValidator:

    def get_layer(self, value):

        if "controllers" in value:
            return "controllers"

        if "services" in value:
            return "services"

        if "repositories" in value:
            return "repositories"

        return None

    def validate(self, dependencies):

        violations = []

        for dep in dependencies:

            source_layer = self.get_layer(
                dep.source_file
            )

            target_layer = self.get_layer(
                dep.target_module
            )

            if (
                source_layer is None
                or target_layer is None
            ):
                continue

            allowed = (
                ALLOWED_DEPENDENCIES[
                    source_layer
                ]
            )

            if target_layer not in allowed:

                violations.append(
                    ArchitectureViolation(
                        dep.source_file,
                        source_layer,
                        target_layer
                    )
                )

        return violations