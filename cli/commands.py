import os
import typer

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress

from analyzers.file_analyzer import FileAnalyzer
from analyzers.function_analyzer import FunctionAnalyzer
from analyzers.dependency_analyzer import (
    DependencyAnalyzer
)
from analyzers.circular_dependency_analyzer import (
    CircularDependencyAnalyzer
)
from analyzers.source_code_analyzer import (
    SourceCodeAnalyzer
)

from rules.architecture_validator import (
    ArchitectureValidator
)

from reports.console_reporter import (
    ConsoleReporter
)

from reports.json_reporter import (
    JsonReporter
)

from reports.architecture_score import (
    ArchitectureScoreCalculator
)
from reports.html_reporter import (
    HtmlReporter
)
from reports.markdown_reporter import (
    MarkdownReporter
)

from analyzers.db_access_analyzer import (
    DBAccessAnalyzer
)


app = typer.Typer(
        help="""
    CodeGuardian

    Analyze your project's architecture and code quality.

    Supported languages:
    • Python (.py)
    • TypeScript (.ts)
    • JavaScript (.js)

    Generate reports in Console, JSON, HTML and Markdown.
    """
    )
console = Console()


def get_score_color(score):

    if score >= 90:
        return "green"

    elif score >= 70:
        return "yellow"

    return "red"


def calculate_project_score(
    path,
    max_file_lines=300,
    max_function_lines=50
):
    file_violations = (
        FileAnalyzer(
            max_file_lines
        ).analyze(path)
    )

    function_violations = (
        FunctionAnalyzer(
            max_function_lines
        ).analyze_project(path)
    )

    dependencies = (
        DependencyAnalyzer()
        .analyze_project(path)
    )

    

    architecture_violations = (
        ArchitectureValidator()
        .validate(dependencies)
    )

    circular_violations = (
        CircularDependencyAnalyzer()
        .detect(dependencies)
    )

    return (
        ArchitectureScoreCalculator()
        .calculate(
            file_violations,
            function_violations,
            architecture_violations,
            circular_violations
        )
    )


def count_python_files(path):

    count = 0

    ignore_dirs = {
        "venv",
        ".git",
        "__pycache__",
        ".pytest_cache"
    }

    for root, dirs, files in os.walk(path):

        dirs[:] = [
            d for d in dirs
            if d not in ignore_dirs
        ]

        for file in files:

            if file.endswith(".py"):

                count += 1

    return count


@app.command(
    help="""
Run a complete architecture scan.

Examples:

  python main.py scan

  python main.py scan --json

  python main.py scan --html

  python main.py scan --markdown

  python main.py scan --score

  python main.py scan --details
"""
)
def scan(

    path: str = ".",
    max_file_lines: int = typer.Option(
        300,
        "--max-file-lines",
        help="Maximum allowed lines per file."
    ),

    max_function_lines: int = typer.Option(
        50,
        "--max-function-lines",
        help="Maximum allowed lines per function."
    ),
    json_output: bool = typer.Option(
        False,
        "--json",
        "-j",
        help="Generate a JSON report."
    ),

    html_output: bool = typer.Option(
        False,
        "--html",
        help="Generate an HTML report."
    ),

    score_only: bool = typer.Option(
        False,
        "--score",
        help="Display only the architecture score."
    ),
    details: bool = typer.Option(
        False,
        "--details",
        help="Show detailed classes, functions and imports."
    ),
    markdown_output: bool = typer.Option(
        False,
        "--markdown",
        help="Generate a Markdown report."
    ),
        
):
    if not (
        json_output
        or html_output
        or score_only
    ):

        console.print(
            Panel.fit(
                f"Scanning project: "
                f"[bold cyan]{path}[/bold cyan]",
                title="CodeGuardian"
            )
        )

    reporter = ConsoleReporter()

    with Progress(
        disable=(
            json_output
            or html_output
            or markdown_output
            or score_only
        )
    ) as progress:

        file_task = progress.add_task(
            "[cyan]Analyzing files...",
            total=1
        )

        file_violations = (
            FileAnalyzer(
                max_file_lines
            ).analyze(path)
        )

        progress.update(
            file_task,
            advance=1
        )

        function_task = progress.add_task(
            "[green]Analyzing functions...",
            total=1
        )

        function_violations = (
            FunctionAnalyzer(
                max_function_lines
            ).analyze_project(path)
        )

        progress.update(
            function_task,
            advance=1
        )

        dependency_task = progress.add_task(
            "[yellow]Analyzing dependencies...",
            total=1
        )

        dependencies = (
            DependencyAnalyzer()
            .analyze_project(path)
        )

        db_access_violations = (
            DBAccessAnalyzer()
            .analyze(dependencies)
        )

        progress.update(
            dependency_task,
            advance=1
        )

        architecture_task = progress.add_task(
            "[red]Validating architecture...",
            total=1
        )

        architecture_violations = (
            ArchitectureValidator()
            .validate(dependencies)
        )

        progress.update(
            architecture_task,
            advance=1
        )

        circular_task = progress.add_task(
            "[magenta]Checking circular dependencies...",
            total=1
        )

        circular_violations = (
            CircularDependencyAnalyzer()
            .detect(dependencies)
        )

        progress.update(
            circular_task,
            advance=1
        )

        source_task = progress.add_task(
            "[blue]Analyzing JS/TS files...",
            total=1
        )

        source_analysis = (
            SourceCodeAnalyzer()
            .analyze(path)
        )

        progress.update(
            source_task,
            advance=1
        )

        score_task = progress.add_task(
            "[white]Calculating score...",
            total=1
        )

        score = (
            ArchitectureScoreCalculator()
            .calculate(file_violations,function_violations,architecture_violations,circular_violations
            )
        )

        progress.update(
            score_task,
            advance=1
        )

    if json_output:

        output = (
            JsonReporter()
            .generate(file_violations,function_violations,architecture_violations,circular_violations,source_analysis,score
            )
        )

        print(output)

        return
    
    if html_output:

        HtmlReporter().generate(file_violations,function_violations,architecture_violations,circular_violations,source_analysis,score
        )

        console.print(
            "[green]✓ report.html generated[/green]"
        )

        return
    
    if markdown_output:

        MarkdownReporter().generate(
            file_violations,
            function_violations,
            architecture_violations,
            circular_violations,
            source_analysis,
            score
        )

        console.print(
            "[green]✓ report.md generated[/green]"
        )

        return


    if score_only:

        score_color = get_score_color(
            score
        )

        console.print(
            f"[bold {score_color}]"
            f"{score}/100"
            f"[/bold {score_color}]"
        )

        return

    reporter.show_dashboard(
        source_analysis,
        file_violations,
        function_violations,
        architecture_violations,
        circular_violations,
        db_access_violations,
        score
    )

    console.print()

    if file_violations:

        reporter.show_file_violations(
            file_violations
        )

    else:

        console.print(
            "[green]✓ No oversized files found[/green]"
        )
    if function_violations:

        reporter.show_function_violations(
            function_violations
        )

    else:

        console.print(
            "[green]✓ No oversized functions found[/green]"
        )

    if architecture_violations:

        reporter.show_architecture_violations(
            architecture_violations
        )

    else:

        console.print(
            "[green]✓ No architecture violations found[/green]"
        )

    if circular_violations:

        reporter.show_circular_dependencies(
            circular_violations
        )

    else:

        console.print(
            "[green]✓ No circular dependencies found[/green]"
        )



    if db_access_violations:

        reporter.show_db_access_violations(
          db_access_violations
        )

    else:

       console.print(
            "[green]✓ No direct database access found[/green]"
       )

    if source_analysis:

        reporter.show_source_analysis(
            source_analysis,
            details
        )

    score_color = get_score_color(score)

    console.print()

    

    console.print(
        Panel.fit(
            f"[bold {score_color}]"
            f"Architecture Score: "
            f"{score}/100"
            f"[/bold {score_color}]",
            title="Health Report"
        )
    )

    critical_found = (
        len(architecture_violations) > 0
        or len(circular_violations) > 0
    )

    if critical_found:
        raise typer.Exit(code=1)


    console.print(
        "[bold green]✓ Scan completed successfully[/bold green]"
    )





@app.command()
def report(

    path: str = ".",

    max_file_lines: int = typer.Option(
        300,
        "--max-file-lines",
        help="Maximum allowed lines per file."
    ),

    max_function_lines: int = typer.Option(
        50,
        "--max-function-lines",
        help="Maximum allowed lines per function."
    )
):

    reporter = ConsoleReporter()

    file_violations = (
        FileAnalyzer(
            max_file_lines
        ).analyze(path)
    )

    function_violations = (
        FunctionAnalyzer(
            max_function_lines
        ).analyze_project(path)
    )

    dependencies = (
        DependencyAnalyzer()
        .analyze_project(path)
    )

    architecture_violations = (
        ArchitectureValidator()
        .validate(dependencies)
    )

    circular_violations = (
        CircularDependencyAnalyzer()
        .detect(dependencies)
    )

    score = (
        ArchitectureScoreCalculator()
        .calculate(file_violations,function_violations,architecture_violations,circular_violations
        )
    )

    total_files = count_python_files(path)

    reporter.show_summary(total_files,file_violations,function_violations,architecture_violations,circular_violations,score
    )