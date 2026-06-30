from config.config_loader import (
    ConfigLoader
)


class ArchitectureScoreCalculator:

    def __init__(self):

        config = ConfigLoader.load()

        self.penalties = config[
            "architecture_score"
        ]

    def calculate(
        self,
        file_violations,
        function_violations,
        architecture_violations,
        circular_violations
    ):

        score = 100

        score -= (
            len(file_violations)
            * self.penalties[
                "file_penalty"
            ]
        )

        score -= (
            len(function_violations)
            * self.penalties[
                "function_penalty"
            ]
        )

        score -= (
            len(architecture_violations)
            * self.penalties[
                "architecture_penalty"
            ]
        )

        score -= (
            len(circular_violations)
            * self.penalties[
                "circular_dependency_penalty"
            ]
        )

        return max(score, 0)