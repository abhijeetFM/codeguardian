from CODEGUARDIAN.config.config_loader import (
    ConfigLoader
)


class ArchitectureScoreCalculator:

    def __init__(self):

        config = ConfigLoader.load()

        self.penalties = config.get(
            "architecture_score",
            {}
        )

    def calculate(
        self,
        file_violations,
        function_violations,
        architecture_violations,
        circular_violations,
        db_access_violations
    ):

        score = 100

        score -= (
            len(file_violations)
            * self.penalties.get(
                "file_penalty",
                10
            )
        )

        score -= (
            len(function_violations)
            * self.penalties.get(
                "function_penalty",
                5
            )
        )

        score -= (
            len(architecture_violations)
            * self.penalties.get(
                "architecture_penalty",
                20
            )
        )

        score -= (
            len(circular_violations)
            * self.penalties.get(
                "circular_dependency_penalty",
                30
            )
        )

        score -= (
            len(db_access_violations)
            * self.penalties.get(
                "db_access_penalty",
                15
            )
        )

        return max(score, 0)