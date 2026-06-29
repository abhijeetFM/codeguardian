from rich.console import Console
from rich.table import Table
from reports.severity import Severity


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

            table.add_row(
                violation.file_path,
                str(violation.line_count),
                f"🟡 {Severity.WARNING}"
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

            table.add_row(
                violation.function_name,
                str(violation.line_count),
                f"🟡 {Severity.WARNING}"
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
                f"{violation.source_layer} → {violation.target_layer}",
                f"🔴 {Severity.CRITICAL}"
            )

        self.console.print(table)

    def show_summary(
    self,
    total_files,
    file_violations,
    function_violations,
    architecture_violations,
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
            f"🟡 {len(file_violations)}"
        )

        table.add_row(
            "Oversized Functions",
            f"🟡 {len(function_violations)}"
        )

        table.add_row(
            "Architecture Violations",
            f"🔴 {len(architecture_violations)}"
        )
        if score >= 90:
            score_icon = "🟢"

        elif score >= 70:
            score_icon = "🟡"

        else:
            score_icon = "🔴"
        table.add_row(
            "Architecture Score",
            f"{score_icon} {score}/100"
        )

        self.console.print(table)