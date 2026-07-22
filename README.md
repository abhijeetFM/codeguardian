# CodeGuardian CLI

CodeGuardian CLI is a lightweight and extensible architecture and code quality analysis tool for Python, JavaScript, and TypeScript projects. It helps developers maintain clean project architecture by detecting code quality issues, dependency violations, circular dependencies, and direct database access while providing an overall architecture health score.

CodeGuardian is distributed as a PyPI package and can be easily integrated into your development workflow.

---

## Features

- Architecture and code quality analysis.
- Architecture score calculation.
- Oversized file detection.
- Oversized function detection.
- Architecture rule validation.
- Circular dependency detection.
- Direct database access detection.
- Source code analysis.
- Automatic virtual environment detection and exclusion.
- Pre-commit hook support.
- Multi-language support:
  - Python
  - JavaScript
  - TypeScript
- Multiple report formats:
  - Console
  - JSON
  - HTML
  - Markdown
- Easy installation through PyPI.
- Extensible and configurable architecture rules.

---

## Installation

Install CodeGuardian directly from PyPI:

```bash
pip install codeguardian-cli
```

Verify the installation:

```bash
codeguardian --help
```

---

## Supported Languages

| Language | Supported |
|---------|----------|
| Python | Yes |
| JavaScript | Yes |
| TypeScript | Yes |

---

## Supported Commands

### Scan Command

The `scan` command performs a complete architecture and code quality analysis of a project.

```bash
codeguardian scan <project_path>
```

Examples:

```bash
codeguardian scan 
```

```bash
codeguardian scan my_project
```

If no path is provided, the current working directory is scanned.

---

### Report Command

The `report` command generates a summarized architecture report for the project.

```bash
codeguardian report
```

---

## Scan Flags

The following flags are supported with the `scan` command:

| Flag | Description |
|------|------------|
| --json | Generate JSON report |
| --html | Generate HTML report |
| --markdown | Generate Markdown report |
| --details | Display detailed source code analysis |
| --score | Display architecture score |
| --stayistics |Display an overall stats of the project|

Examples:

Generate JSON report:

```bash
codeguardian scan . --json
```

Generate HTML report:

```bash
codeguardian scan . --html
```

Generate Markdown report:

```bash
codeguardian scan . --markdown
```

Display architecture score:

```bash
codeguardian scan . --score
```

Display statistic:

```bash
codeguardian scan . --statistics
```

Display detailed source code analysis:

```bash
codeguardian scan . --details
```

Combine multiple flags:

```bash
codeguardian scan . --html --score
```

---

## Project Structure

```text
CODEGUARDIAN/
│
├── analyzers/
│   ├── Circular Dependency Analyzer
│   ├── Database Access Analyzer
│   ├── Dependency Analyzer
│   ├── File Analyzer
│   ├── Function Analyzer
│   └── Source Code Analyzer
│
├── cli/
│   └── CLI Commands
│
├── config/
│   └── Configuration Loader
│
├── reports/
│   ├── Console Reporter
│   ├── HTML Reporter
│   ├── JSON Reporter
│   └── Markdown Reporter
│
├── rules/
│   └── Architecture Validator
│
├── src/
│   ├── Discovery
│   ├── Parser
│   └── Tree Walker
│
├── utils/
│   └── Utility Modules
│
├── main.py
│
└── __init__.py
```

---

## Architecture Score

CodeGuardian generates an overall architecture score that reflects the health of your project's architecture.

The score is calculated based on:

- Oversized files
- Oversized functions
- Architecture violations
- Circular dependencies
- Direct database access violations

The scoring mechanism can be customized through the configuration file.

---

## Generated Reports

CodeGuardian supports multiple report formats.

### Console Report

Displayed directly in the terminal after running the scan command.

### HTML Report

Generated as:

```text
report.html
```

### JSON Report

Generated as:

```text
report.json
```

### Markdown Report

Generated as:

```text
report.md
```

---

## Example Usage

Scan the current project:

```bash
codeguardian scan .
```

Scan a specific project:

```bash
codeguardian scan backend_project
```

Generate an HTML report:

```bash
codeguardian scan . --html
```

Generate a Markdown report:

```bash
codeguardian scan . --markdown
```

Generate a JSON report:

```bash
codeguardian scan . --json
```

Display architecture score:

```bash
codeguardian scan . --score
```

Display detailed source code analysis:

```bash
codeguardian scan . --details
```

Generate a summarized report:

```bash
codeguardian report
```

---

## Configuration

CodeGuardian uses a configuration file named:

```text
codeguardian.json
```

The configuration file allows developers to customize various project-specific settings, including:

- Maximum file line limit
- Maximum function line limit
- Supported file extensions
- Architecture scoring penalties
- Circular dependency checks
- Direct database access checks
- Architecture validation rules
- Additional project configurations

---

## Automatic Virtual Environment Detection

CodeGuardian automatically skips Python virtual environments during project analysis.

Any directory containing:

```text
pyvenv.cfg
```

is automatically ignored during scanning.

Examples include:

```text
venv/
.venv/
test_env/
cg_env/
backend_env/
```

This prevents installed dependencies and packages from affecting architecture and code quality reports.

No additional configuration is required.

---

## Developer Notes

### Pre-Commit Hook Support

CodeGuardian provides a pre-commit hook that helps maintain architecture and code quality standards before every commit.

During the development of CodeGuardian itself, the repository contains sample files with intentional architecture violations, circular dependencies, and other test cases used for validation purposes.

These files may cause the pre-commit hook to block commits.

If required, the hook can be temporarily disabled.

---

### Windows (PowerShell)

Disable the hook:

```powershell
Rename-Item .git\hooks\pre-commit pre-commit.bak
```

Restore the hook:

```powershell
Rename-Item .git\hooks\pre-commit.bak pre-commit
```

---

### Linux / macOS

Disable the hook:

```bash
mv .git/hooks/pre-commit .git/hooks/pre-commit.bak
```

Restore the hook:

```bash
mv .git/hooks/pre-commit.bak .git/hooks/pre-commit
```

---

### Reinstalling the Hook

If the hook is accidentally deleted or corrupted, it can be reinstalled using:

```bash
python install_hook.py
```

---

## PyPI Package Information

| Field | Value |
|------|------|
| Package Name | codeguardian-cli |
| Current Version | 1.2.3 |

Install directly from PyPI:

```bash
pip install codeguardian-cli
```

---

## Future Enhancements

Some planned improvements for future releases include:

- Framework-specific architecture rules.
- CI/CD pipeline integration.
- GitHub Actions support.
- Architecture visualization.
- Additional language support.
- Custom rule creation.
- IDE integrations.
- Advanced reporting capabilities.

---

## License

This project is licensed under the MIT License.

---

## Authors

Developed by the CodeGuardian Team.
