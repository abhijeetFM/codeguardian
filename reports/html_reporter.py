class HtmlReporter:

    def generate(
        self,
        file_violations,
        function_violations,
        architecture_violations,
        circular_violations,
        source_analysis,
        score
    ):

        html = f"""
        <html>

        <head>

            <title>
                CodeGuardian Report
            </title>

        </head>

        <body>

            <h1>
                CodeGuardian Report
            </h1>

            <h2>
                Architecture Score:
                {score}/100
            </h2>

            <h3>
                Oversized Files
            </h3>

            <ul>
        """

        for violation in file_violations:

            html += f"""

            <li>

                {violation.file_path}
                ({violation.line_count} lines)

            </li>

            """

        html += """

            </ul>

            <h3>
                Oversized Functions
            </h3>

            <ul>

        """

        for violation in function_violations:

            html += f"""

            <li>

                {violation.function_name}
                ({violation.line_count} lines)

            </li>

            """

        html += """

            </ul>

            <h3>
                Architecture Violations
            </h3>

            <ul>

        """

        for violation in architecture_violations:

            html += f"""

            <li>

                {violation.source_file}

                :

                {violation.source_layer}

                →

                {violation.target_layer}

            </li>

            """

        html += """

            </ul>

            <h3>
                Circular Dependencies
            </h3>

            <ul>

        """

        for violation in circular_violations:

            html += f"""

            <li>

                {" → ".join(violation.cycle)}

            </li>

            """

        html += """

            </ul>

        </body>

        </html>

        """

        with open(
            "report.html",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html)