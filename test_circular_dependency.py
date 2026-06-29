from analyzers.circular_dependency_analyzer import (
    CircularDependencyAnalyzer
)


class FakeDependency:

    def __init__(
        self,
        source_file,
        target_module
    ):
        self.source_file = source_file
        self.target_module = target_module


dependencies = [

    FakeDependency(
        "UserService",
        "EmailService"
    ),

    FakeDependency(
        "EmailService",
        "NotificationService"
    ),

    FakeDependency(
        "NotificationService",
        "DatabaseService"
    )
]


analyzer = CircularDependencyAnalyzer()

has_cycle = analyzer.detect(
    dependencies
)


if has_cycle:
    print("❌ Circular dependency detected!")

else:
    print("✅ No circular dependencies found.")