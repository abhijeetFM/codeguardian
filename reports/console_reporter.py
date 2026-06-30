from rich.console import Console
from rich.table import Table

from reports.severity import (
    get_severity
)


class ConsoleReporter:

    def __init__(self):

        self.console = Console()

    def show_file_violations(
        self,
        violations
    ):

        table = Table(
            title="Oversized Files"
        )

        table.add_column(
            "File",
            style="cyan"
        )

        table.add_column(
            "Lines",
            style="red"
        )

        table.add_column(
            "Severity",
            style="yellow"
        )

        for violation in violations:

            severity = get_severity(
                violation.line_count,
                warning_threshold=300,
                critical_threshold=500
            )

            table.add_row(
                violation.file_path,
                str(violation.line_count),
                severity
            )

        self.console.print(table)

    def show_function_violations(
        self,
        violations
    ):

        table = Table(
            title="Oversized Functions"
        )

        table.add_column(
            "Function",
            style="cyan"
        )

        table.add_column(
            "Lines",
            style="red"
        )

        table.add_column(
            "Severity",
            style="yellow"
        )

        for violation in violations:

            severity = get_severity(
                violation.line_count,
                warning_threshold=50,
                critical_threshold=100
            )

            table.add_row(
                violation.function_name,
                str(violation.line_count),
                severity
            )

        self.console.print(table)

    def show_architecture_violations(
        self,
        violations
    ):

        table = Table(
            title="Architecture Violations"
        )

        table.add_column(
            "File",
            style="cyan"
        )

        table.add_column(
            "Rule Broken",
            style="red"
        )

        table.add_column(
            "Severity",
            style="red"
        )

        for violation in violations:

            table.add_row(
                violation.source_file,
                (
                    f"{violation.source_layer}"
                    f" → "
                    f"{violation.target_layer}"
                ),
                "🔴 CRITICAL"
            )

        self.console.print(table)

    def show_circular_dependencies(
        self,
        violations
    ):

        table = Table(
            title="Circular Dependencies"
        )

        table.add_column(
            "Dependency Cycle",
            style="red"
        )

        table.add_column(
            "Severity",
            style="red"
        )

        for violation in violations:

            table.add_row(
                " → ".join(
                    violation.cycle
                ),
                "🔴 CRITICAL"
            )

        self.console.print(table)

    def show_summary(
        self,
        total_files,
        file_violations,
        function_violations,
        architecture_violations,
        circular_violations,
        score
    ):

        table = Table(
            title="CodeGuardian Summary"
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
            "Architecture Score",
            f"{score}/100"
        )

        self.console.print(table)