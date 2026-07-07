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


    def show_db_access_violations(
        self,
        violations
    ):

        table = Table(
        title="Direct Database Access"
        )

        table.add_column(
        "Controller",
        style="cyan"
        )

        table.add_column(
        "Database",
        style="red"
        )

        for violation in violations:

            table.add_row(

            violation.source_file,

            violation.database_library

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

    def show_source_analysis(
        self,
        source_analysis,
        details=False
    ):

        table = Table(
            title="Source Code Analysis"
        )

        table.add_column(
            "File",
            style="cyan"
        )

        table.add_column(
            "Classes",
            justify="center",
            style="green"
        )

        table.add_column(
            "Functions",
            justify="center",
            style="yellow"
        )

        table.add_column(
            "Imports",
            justify="center",
            style="magenta"
        )

        for item in source_analysis:

            table.add_row(
                item["file"],
                str(len(item["classes"])),
                str(len(item["functions"])),
                str(len(item["imports"]))
            )

        self.console.print(table)

        if not details:
            return

        self.console.rule(
            "[bold blue]Source Code Details[/bold blue]"
        )

        for item in source_analysis:

            # Skip completely empty files
            if (
                not item["classes"]
                and not item["functions"]
                and not item["imports"]
            ):
                continue

            self.console.print()

            self.console.print(
                f"[bold cyan]{item['file']}[/bold cyan]"
            )

            classes = (
                ", ".join(item["classes"])
                if item["classes"]
                else "-"
            )

            functions = (
                ", ".join(item["functions"])
                if item["functions"]
                else "-"
            )

            imports = (
                ", ".join(item["imports"])
                if item["imports"]
                else "-"
            )

            self.console.print(
                f"[green]Classes:[/green] {classes}"
            )

            self.console.print(
                f"[yellow]Functions:[/yellow] {functions}"
            )

            self.console.print(
                f"[magenta]Imports:[/magenta] {imports}"
            )

            self.console.print(
                "-" * 70
            )