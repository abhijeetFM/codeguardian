import typer
import os

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress

from analyzers.file_analyzer import FileAnalyzer
from analyzers.function_analyzer import FunctionAnalyzer
from analyzers.dependency_analyzer import DependencyAnalyzer

from rules.architecture_validator import ArchitectureValidator

from reports.console_reporter import ConsoleReporter
from reports.architecture_score import ArchitectureScoreCalculator


app = typer.Typer()
console = Console()



def calculate_project_score(path: str):

    file_analyzer = FileAnalyzer()
    function_analyzer = FunctionAnalyzer()
    dependency_analyzer = DependencyAnalyzer()

    file_violations = file_analyzer.analyze(path)

    function_violations = (
        function_analyzer.analyze_project(path)
    )

    dependencies = (
        dependency_analyzer.analyze_project(path)
    )

    architecture_violations = (
        ArchitectureValidator()
        .validate(dependencies)
    )

    score = (
        ArchitectureScoreCalculator()
        .calculate(
            file_violations,
            function_violations,
            architecture_violations
        )
    )

    return score




def count_python_files(path):

    count = 0

    IGNORE_DIRS = {
        "venv",
        ".git",
        "__pycache__",
        ".pytest_cache"
    }

    for root, dirs, files in os.walk(path):

        dirs[:] = [
            d for d in dirs
            if d not in IGNORE_DIRS
        ]

        for file in files:

            if file.endswith(".py"):
                count += 1

    return count

def get_score_color(score):

    if score >= 90:
        return "green"

    elif score >= 70:
        return "yellow"

    return "red"


@app.command()
def scan(path: str = "."):

    console.print(
        Panel.fit(
            f"Scanning project: [bold cyan]{path}[/bold cyan]",
            title="CodeGuardian"
        )
    )

    # Initialize analyzers
    file_analyzer = FileAnalyzer()
    function_analyzer = FunctionAnalyzer()
    dependency_analyzer = DependencyAnalyzer()

    # Initialize reporter
    reporter = ConsoleReporter()

    with Progress() as progress:

        file_task = progress.add_task(
            "[cyan]Analyzing files...",
            total=1
        )

        file_violations = file_analyzer.analyze(path)

        progress.update(
            file_task,
            advance=1
        )


        function_task = progress.add_task(
            "[green]Analyzing functions...",
            total=1
        )

        function_violations = (
            function_analyzer.analyze_project(path)
        )

        progress.update(
            function_task,
            advance=1
        )


        dependency_task = progress.add_task(
            "[yellow]Checking dependencies...",
            total=1
        )

        dependencies = (
            dependency_analyzer.analyze_project(path)
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


        score_task = progress.add_task(
            "[magenta]Calculating score...",
            total=1
        )

        score = (
            ArchitectureScoreCalculator()
            .calculate(
                file_violations,
                function_violations,
                architecture_violations
            )
        )

        progress.update(
            score_task,
            advance=1
        )

    # Calculate architecture score
    score = (
        ArchitectureScoreCalculator()
        .calculate(
            file_violations,
            function_violations,
            architecture_violations
        )
    )

    # Report file violations
    if file_violations:
        reporter.show_file_violations(
            file_violations
        )
    else:
        console.print(
            "[green]✓ No oversized files found[/green]"
        )

    # Report function violations
    if function_violations:
        reporter.show_function_violations(
            function_violations
        )
    else:
        console.print(
            "[green]✓ No oversized functions found[/green]"
        )

    # Report architecture violations
    if architecture_violations:
        reporter.show_architecture_violations(
            architecture_violations
        )
    else:
        console.print(
            "[green]✓ No architecture violations found[/green]"
        )

    # Show architecture score
    console.print()

    score_color = get_score_color(score)

    console.print(
        Panel.fit(
            f"[bold {score_color}]"
            f"Architecture Score: {score}/100"
            f"[/bold {score_color}]",
            title="Health Report"
        )
    )

@app.command()
def score(path: str = "."):

    score_value = calculate_project_score(path)

    score_color = get_score_color(score_value)

    console.print(
        Panel.fit(
            f"[bold {score_color}]"
            f"Architecture Score: {score_value}/100"
            f"[/bold {score_color}]",
            title="Code Health"
        )
    )

@app.command()
def report(path: str = "."):

    reporter = ConsoleReporter()

    file_analyzer = FileAnalyzer()
    function_analyzer = FunctionAnalyzer()
    dependency_analyzer = DependencyAnalyzer()

    file_violations = file_analyzer.analyze(path)

    function_violations = (
        function_analyzer.analyze_project(path)
    )

    dependencies = (
        dependency_analyzer.analyze_project(path)
    )

    architecture_violations = (
        ArchitectureValidator()
        .validate(dependencies)
    )

    score = (
        ArchitectureScoreCalculator()
        .calculate(
            file_violations,
            function_violations,
            architecture_violations
        )
    )

    total_files = count_python_files(path)

    reporter.show_summary(
        total_files,
        file_violations,
        function_violations,
        architecture_violations,
        score
    )