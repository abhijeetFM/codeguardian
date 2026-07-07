class MarkdownReporter:

    def generate(
        self,
        file_violations,
        function_violations,
        architecture_violations,
        circular_violations,
        source_analysis,
        score
    ):

        lines = []

        lines.append("# CodeGuardian Report\n")

        lines.append(f"## Architecture Score\n")
        lines.append(f"**{score}/100**\n")

        # --------------------------------------------------

        lines.append("## Oversized Files\n")

        if file_violations:

            lines.append("| File | Lines |")
            lines.append("|------|------:|")

            for violation in file_violations:

                lines.append(
                    f"| {violation.file_path} | {violation.line_count} |"
                )

        else:

            lines.append("No oversized files found.")

        lines.append("")

        # --------------------------------------------------

        lines.append("## Oversized Functions\n")

        if function_violations:

            lines.append("| Function | Lines |")
            lines.append("|----------|------:|")

            for violation in function_violations:

                lines.append(
                    f"| {violation.function_name} | {violation.line_count} |"
                )

        else:

            lines.append("No oversized functions found.")

        lines.append("")

        # --------------------------------------------------

        lines.append("## Architecture Violations\n")

        if architecture_violations:

            lines.append("| File | Rule |")
            lines.append("|------|------|")

            for violation in architecture_violations:

                lines.append(
                    f"| {violation.source_file} | "
                    f"{violation.source_layer} → "
                    f"{violation.target_layer} |"
                )

        else:

            lines.append("No architecture violations found.")

        lines.append("")

        # --------------------------------------------------

        lines.append("## Circular Dependencies\n")

        if circular_violations:

            for violation in circular_violations:

                cycle = " → ".join(
                    violation.cycle
                )

                lines.append(f"- {cycle}")

        else:

            lines.append("No circular dependencies found.")

        lines.append("")

        # --------------------------------------------------

        lines.append("## Source Code Analysis\n")

        lines.append("| File | Classes | Functions | Imports |")
        lines.append("|------|---------:|----------:|--------:|")

        for item in source_analysis:

            lines.append(
                f"| {item['file']} | "
                f"{len(item['classes'])} | "
                f"{len(item['functions'])} | "
                f"{len(item['imports'])} |"
            )

        with open(
            "report.md",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "\n".join(lines)
            )