# CodeGuardian Report

## Architecture Score

**0/100**

## Oversized Files

| File | Lines |
|------|------:|
| sample_large.py | 360 |
| cli/commands.py | 473 |
| reports/console_reporter.py | 318 |

## Oversized Functions

| Function | Lines |
|----------|------:|
| analyze_python_file | 62 |
| analyze_ts_js_file | 81 |
| analyze_project | 67 |
| analyze_ts_js_file | 59 |
| scan | 288 |
| greet | 76 |
| generate | 150 |
| generate | 64 |
| show_summary | 55 |
| show_source_analysis | 100 |
| generate | 127 |

## Architecture Violations

No architecture violations found.

## Circular Dependencies

- samples.controller → samples.service → samples.controller

## Source Code Analysis

| File | Classes | Functions | Imports |
|------|---------:|----------:|--------:|
| sample_big.ts | 0 | 0 | 0 |
| sample_large.py | 0 | 0 | 0 |
| large_function.py | 0 | 0 | 0 |
| main.py | 0 | 0 | 0 |
| analyzers/source_code_analyzer.py | 1 | 3 | 0 |
| analyzers/dependency_analyzer.py | 2 | 6 | 0 |
| analyzers/__init__.py | 0 | 0 | 0 |
| analyzers/circular_dependency_analyzer.py | 2 | 5 | 0 |
| analyzers/function_analyzer.py | 2 | 6 | 0 |
| analyzers/file_analyzer.py | 2 | 3 | 0 |
| config/config_loader.py | 1 | 1 | 0 |
| config/__init__.py | 0 | 0 | 0 |
| config/settings.py | 0 | 0 | 0 |
| cli/__init__.py | 0 | 0 | 0 |
| cli/commands.py | 0 | 6 | 0 |
| samples/user.js | 0 | 0 | 0 |
| samples/sample.ts | 1 | 1 | 2 |
| samples/controller.ts | 1 | 0 | 1 |
| samples/service.ts | 1 | 0 | 5 |
| rules/__init__.py | 0 | 0 | 0 |
| rules/architecture_validator.py | 2 | 4 | 0 |
| rules/architecture_rules.py | 0 | 0 | 0 |
| reports/severity.py | 0 | 1 | 0 |
| reports/html_reporter.py | 1 | 1 | 0 |
| reports/json_reporter.py | 1 | 1 | 0 |
| reports/__init__.py | 0 | 0 | 0 |
| reports/architecture_score.py | 1 | 2 | 0 |
| reports/console_reporter.py | 1 | 7 | 0 |
| reports/markdown_reporter.py | 1 | 1 | 0 |
| src/__init__.py | 0 | 0 | 0 |
| src/main.py | 0 | 0 | 0 |
| src/tree/Walker.py | 0 | 1 | 0 |
| src/tree/__init__.py | 0 | 0 | 0 |
| src/discovery/finder.py | 0 | 1 | 0 |
| src/discovery/__init__.py | 0 | 0 | 0 |
| src/extractor/__init__.py | 0 | 0 | 0 |
| src/extractor/class_extractor.py | 1 | 2 | 0 |
| src/extractor/import_extractor.py | 1 | 2 | 0 |
| src/extractor/function_extractor.py | 1 | 2 | 0 |
| src/parser/ts_parser.py | 0 | 1 | 0 |
| src/parser/__init__.py | 0 | 0 | 0 |
| sample_project/repositories/user_repository.py | 1 | 1 | 0 |
| sample_project/controllers/user_controller.py | 1 | 2 | 0 |
| sample_project/services/notification_service.py | 1 | 0 | 0 |
| sample_project/services/email_service.py | 1 | 0 | 0 |
| sample_project/services/user_service.py | 1 | 2 | 0 |