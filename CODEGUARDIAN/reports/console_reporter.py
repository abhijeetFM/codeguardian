from rich.console import Console
from rich.table import Table

from CODEGUARDIAN.reports.severity import (
    get_severity
)
from rich.panel import Panel
from rich.text import Text



class ConsoleReporter:

    def __init__(self):

        self.console = Console()

    def show_dashboard(
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

        if score >= 90:
            score_style = "green"

        elif score >= 70:
            score_style = "yellow"

        else:
            score_style = "red"

        dashboard = Text()

        dashboard.append(
            f"✔ Files Scanned              : {total_files}\n",
            style="cyan"
        )

        dashboard.append(
            f"✔ Classes                    : {total_classes}\n",
            style="green"
        )

        dashboard.append(
            f"✔ Functions                  : {total_functions}\n",
            style="green"
        )

        dashboard.append(
            f"✔ Imports                    : {total_imports}\n\n",
            style="green"
        )

       # Oversized Files
        if len(file_violations) == 0:
            dashboard.append(
                f"✔ Oversized Files            : 0\n",
                style="green"
            )
        else:
            dashboard.append(
                f"⚠ Oversized Files            : {len(file_violations)}\n",
                style="yellow"
            )

        # Oversized Functions
        if len(function_violations) == 0:
            dashboard.append(
                f"✔ Oversized Functions        : 0\n",
                style="green"
            )
        else:
            dashboard.append(
                f"⚠ Oversized Functions        : {len(function_violations)}\n",
                style="yellow"
            )

        # Architecture Violations
        if len(architecture_violations) == 0:
            dashboard.append(
                f"✔ Architecture Violations    : 0\n",
                style="green"
            )
        else:
            dashboard.append(
                f"✖ Architecture Violations    : {len(architecture_violations)}\n",
                style="red"
            )

        # Circular Dependencies
        if len(circular_violations) == 0:
            dashboard.append(
                f"✔ Circular Dependencies      : 0\n",
                style="green"
            )
        else:
            dashboard.append(
                f"✖ Circular Dependencies      : {len(circular_violations)}\n",
                style="red"
            )

        # Direct Database Access
        if len(db_access_violations) == 0:
            dashboard.append(
                f"✔ Direct DB Access           : 0\n\n",
                style="green"
            )
        else:
            dashboard.append(
                f"✖ Direct DB Access           : {len(db_access_violations)}\n\n",
                style="red"
            )

        self.console.print(
            Panel.fit(
                dashboard,
                title="Architecture Dashboard",
                border_style="cyan"
            )
        )

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

        if violations:

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

        else:

            table.add_row(
                "No oversized files found",
                "-",
                "✓"
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
        if violations:

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
        else:

            table.add_row(
                "No oversized functions found",
                "-",
                "✓"
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
        

        if violations:

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

        else:

            table.add_row(
                "No architecture violations found",
                "-",
                "✓"
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

        if violations:

            for violation in violations:

                table.add_row(
                    " → ".join(
                        violation.cycle
                    ),
                    "🔴 CRITICAL"
                )
        else:

            table.add_row(
                "No circular dependencies found",
                "✓"
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


        if violations:

            for violation in violations:

                table.add_row(

                violation.source_file,

                violation.database_library

            )
                
        else:

            table.add_row(
                "No direct database access found",
                "-"
            )

        self.console.print(table)

    def show_summary(
        self,
        total_files,
        file_violations,
        function_violations,
        architecture_violations,
        circular_violations,
        db_access_violations,
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
            "Direct Database Access",
            str(len(db_access_violations))
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