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

from rules.architecture_validator import (
    ArchitectureValidator
)

from reports.console_reporter import (
    ConsoleReporter
)
from reports.architecture_score import (
    ArchitectureScoreCalculator
)


app = typer.Typer()
console = Console()


def get_score_color(score):

    if score >= 90:
        return "green"

    elif score >= 70:
        return "yellow"

    return "red"


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

    config = ConfigLoader.load()

    if config["enable_circular_dependency_check"]:

        circular_violations = (
            CircularDependencyAnalyzer()
            .detect(dependencies)
        )

    else:

        circular_violations = []

    score = (
        ArchitectureScoreCalculator()
        .calculate(
            file_violations,
            function_violations,
            architecture_violations,
            circular_violations
        )
    )

    return score


from config.config_loader import ConfigLoader


def count_python_files(path):

    count = 0

    config = ConfigLoader.load()

    ignore_dirs = set(
        config["ignored_directories"]
    )

    for root, dirs, files in os.walk(path):

        dirs[:] = [
            d for d in dirs
            if d not in ignore_dirs
        ]

        for file in files:

            if file.endswith(".py"):
                count += 1

    return count


@app.command()
def scan(path: str = "."):

    console.print(
        Panel.fit(
            f"Scanning project: [bold cyan]{path}[/bold cyan]",
            title="CodeGuardian"
        )
    )

    reporter = ConsoleReporter()

    with Progress() as progress:

        file_task = progress.add_task(
            "[cyan]Analyzing files...",
            total=1
        )

        file_violations = (
            FileAnalyzer().analyze(path)
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
            FunctionAnalyzer()
            .analyze_project(path)
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

        score_task = progress.add_task(
            "[blue]Calculating score...",
            total=1
        )

        score = (
            ArchitectureScoreCalculator()
            .calculate(
                file_violations,
                function_violations,
                architecture_violations,
                circular_violations
            )
        )

        progress.update(
            score_task,
            advance=1
        )

    # File violations
    if file_violations:

        reporter.show_file_violations(
            file_violations
        )

    else:

        console.print(
            "[green]✓ No oversized files found[/green]"
        )

    # Function violations
    if function_violations:

        reporter.show_function_violations(
            function_violations
        )

    else:

        console.print(
            "[green]✓ No oversized functions found[/green]"
        )

    # Architecture violations
    if architecture_violations:

        reporter.show_architecture_violations(
            architecture_violations
        )

    else:

        console.print(
            "[green]✓ No architecture violations found[/green]"
        )

    # Circular dependencies
    if circular_violations:

        reporter.show_circular_dependencies(
            circular_violations
        )

    else:

        console.print(
            "[green]✓ No circular dependencies found[/green]"
        )

    score_color = get_score_color(score)

    console.print()

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

    score_color = get_score_color(
        score_value
    )

    console.print(
        Panel.fit(
            f"[bold {score_color}]"
            f"Architecture Score: "
            f"{score_value}/100"
            f"[/bold {score_color}]",
            title="Code Health"
        )
    )


@app.command()
def report(path: str = "."):

    reporter = ConsoleReporter()

    file_violations = (
        FileAnalyzer().analyze(path)
    )

    function_violations = (
        FunctionAnalyzer()
        .analyze_project(path)
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
        .calculate(
            file_violations,
            function_violations,
            architecture_violations,
            circular_violations
        )
    )

    total_files = count_python_files(path)

    reporter.show_summary(
        total_files,
        file_violations,
        function_violations,
        architecture_violations,
        circular_violations,
        score
    )