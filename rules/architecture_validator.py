from config.config_loader import (
    ConfigLoader
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

    def __init__(self):

        config = ConfigLoader.load()

        self.forbidden_dependencies = {

            tuple(rule)

            for rule in config[
                "forbidden_dependencies"
            ]
        }

    def get_layer(
        self,
        module_name
    ):

        return module_name.split(".")[0]

    def validate(
        self,
        dependencies
    ):

        violations = []

        for dep in dependencies:

            source_layer = self.get_layer(
                dep.source_file
            )

            target_layer = self.get_layer(
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