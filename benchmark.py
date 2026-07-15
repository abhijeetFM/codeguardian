import time

from analyzers.file_analyzer import FileAnalyzer
from analyzers.function_analyzer import FunctionAnalyzer
from analyzers.dependency_analyzer import DependencyAnalyzer
from analyzers.source_code_analyzer import SourceCodeAnalyzer


def run_scan(project_path):

    FileAnalyzer().analyze(
        project_path
    )

    FunctionAnalyzer().analyze_project(
        project_path
    )

    DependencyAnalyzer().analyze_project(
        project_path
    )

    SourceCodeAnalyzer().analyze(
        project_path
    )


def benchmark(
    project_path,
    runs=5
):

    print("Running cold scan...")

    start_time = time.perf_counter()

    run_scan(project_path)

    end_time = time.perf_counter()

    cold_scan_time = (
        end_time - start_time
    )

    print(
        f"Cold scan: "
        f"{cold_scan_time:.6f} seconds"
    )


    warm_scan_times = []

    print(
        f"\nRunning {runs} warm scans..."
    )

    for run_number in range(
        1,
        runs + 1
    ):

        start_time = time.perf_counter()

        run_scan(project_path)

        end_time = time.perf_counter()

        execution_time = (
            end_time - start_time
        )

        warm_scan_times.append(
            execution_time
        )

        print(
            f"Warm scan {run_number}: "
            f"{execution_time:.6f} seconds"
        )


    average_warm_time = (
        sum(warm_scan_times)
        / len(warm_scan_times)
    )

    print(
        f"\nAverage warm scan: "
        f"{average_warm_time:.6f} seconds"
    )

if __name__ == "__main__":

    benchmark(".")