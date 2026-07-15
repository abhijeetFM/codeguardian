import os

from rich.console import Console
from rich.table import Table


class StatisticsReporter:

    def __init__(self):
        self.console = Console()

    def show_statistics(
        self,
        source_analysis,
        file_violations,
        function_violations,
        architecture_violations,
        circular_violations,
        db_access_violations,
        score
    ):

        total_files = len(source_analysis)

        total_classes = sum(
            len(item["classes"])
            for item in source_analysis
        )

        total_functions = sum(
            len(item["functions"])
            for item in source_analysis
        )

        total_imports = sum(
            len(item["imports"])
            for item in source_analysis
        )

        py_files = 0
        ts_files = 0
        js_files = 0

        total_lines = 0
        largest_file = "-"
        largest_line_count = 0

        for item in source_analysis:

            file_name = item["file"]

            if file_name.endswith(".py"):
                py_files += 1

            elif file_name.endswith(".ts"):
                ts_files += 1

            elif file_name.endswith(".js"):
                js_files += 1

            try:

                with open(
                    file_name,
                    "r",
                    encoding="utf-8"
                ) as file:

                    line_count = len(
                        file.readlines()
                    )

                total_lines += line_count

                if line_count > largest_line_count:

                    largest_line_count = line_count
                    largest_file = file_name

            except Exception:
                continue

        average_lines = (
            total_lines // total_files
            if total_files > 0
            else 0
        )

        table = Table(
            title="Project Statistics"
        )

        table.add_column(
            "Metric",
            style="cyan"
        )

        table.add_column(
            "Value",
            style="green"
        )

        table.add_row(
            "Files Scanned",
            str(total_files)
        )

        table.add_row(
            "Classes Found",
            str(total_classes)
        )

        table.add_row(
            "Functions Found",
            str(total_functions)
        )

        table.add_row(
            "Imports Found",
            str(total_imports)
        )

        table.add_row(
            "Python Files",
            str(py_files)
        )

        table.add_row(
            "TypeScript Files",
            str(ts_files)
        )

        table.add_row(
            "JavaScript Files",
            str(js_files)
        )

        table.add_row(
            "Total Lines of Code",
            str(total_lines)
        )

        table.add_row(
            "Average File Size",
            f"{average_lines} lines"
        )

        table.add_row(
            "Largest File",
            f"{largest_file} ({largest_line_count} lines)"
        )

        table.add_row(
            "Oversized Files",
            str(len(file_violations))
        )

        table.add_row(
            "Oversized Functions",
            str(len(function_violations))
        )

        table.add_row(
            "Architecture Violations",
            str(len(architecture_violations))
        )

        table.add_row(
            "Circular Dependencies",
            str(len(circular_violations))
        )

        table.add_row(
            "Direct DB Access Issues",
            str(len(db_access_violations))
        )

        table.add_row(
            "Architecture Score",
            f"{score}/100"
        )

        self.console.print(table)