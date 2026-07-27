import json


class JsonReporter:

    def generate(
        self,
        file_violations,
        function_violations,
        architecture_violations,
        circular_violations,
        db_access_violations,
        source_analysis,
        score
    ):
        report = {

            "architecture_score": score,

            "oversized_files": [

                {
                    "file": v.file_path,
                    "lines": v.line_count
                }

                for v in file_violations
            ],

            "oversized_functions": [

                {
                    "function": v.function_name,
                    "lines": v.line_count
                }

                for v in function_violations
            ],

            "architecture_violations": [

                {
                    "source_file": v.source_file,
                    "rule": (
                        f"{v.source_layer}"
                        f" -> "
                        f"{v.target_layer}"
                    )
                }

                for v in architecture_violations
            ],

            "circular_dependencies": [

                {
                    "cycle": c.cycle
                }

                for c in circular_violations
            ],

            "source_analysis": source_analysis
        }

        return json.dumps(
            report,
            indent=4
        )