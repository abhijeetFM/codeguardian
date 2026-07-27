from CODEGUARDIAN.config.config_loader import (
    ConfigLoader
)

from CODEGUARDIAN.utils.layer_utils import get_layer


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

    def __init__(self):

        config = ConfigLoader.load()

        self.forbidden_dependencies = {

            tuple(rule)

            for rule in config[
                "forbidden_dependencies"
            ]
        }



    def validate(
        self,
        dependencies
    ):

        violations = []

        for dep in dependencies:

            source_layer = get_layer(
                dep.source_file
            )

            target_layer = get_layer(
                dep.target_module
            )

            if (
                source_layer,
                target_layer
            ) in self.forbidden_dependencies:

                violations.append(
                    ArchitectureViolation(
                        dep.source_file,
                        source_layer,
                        target_layer
                    )
                )

        return violations