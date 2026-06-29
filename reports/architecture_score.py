class ArchitectureScoreCalculator:

    def calculate(
        self,
        file_violations,
        function_violations,
        architecture_violations
    ):

        score = 100

        score -= len(file_violations) * 10

        score -= len(function_violations) * 5

        score -= (
            len(architecture_violations)
            * 20
        )

        return max(score, 0)