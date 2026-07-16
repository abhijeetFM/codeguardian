# CodeGuardian Report

## Architecture Score

**90/100**

## Oversized Files

No oversized files found.

## Oversized Functions

No oversized functions found.

## Architecture Violations

| File | Rule |
|------|------|
| CODEGUARDIAN.rules.controllers.user_controller | controllers → repositories |

## Circular Dependencies

- samples.controller → samples.service → samples.controller

## Source Code Analysis

| File | Classes | Functions | Imports |
|------|---------:|----------:|--------:|
| install_hook.py | 0 | 0 | 1 |
| samples/user.js | 0 | 0 | 0 |
| samples/sample.ts | 1 | 1 | 2 |
| samples/controller.ts | 1 | 0 | 1 |
| samples/service.ts | 1 | 0 | 5 |
| CODEGUARDIAN/__init__.py | 0 | 0 | 0 |
| CODEGUARDIAN/main.py | 0 | 0 | 1 |
| sample_project/repositories/user_repository.py | 1 | 1 | 0 |
| sample_project/services/notification_service.py | 1 | 0 | 1 |
| sample_project/services/email_service.py | 1 | 0 | 1 |
| sample_project/services/user_service.py | 1 | 2 | 1 |
| CODEGUARDIAN/analyzers/source_code_analyzer.py | 1 | 3 | 13 |
| CODEGUARDIAN/analyzers/dependency_analyzer.py | 2 | 6 | 6 |
| CODEGUARDIAN/analyzers/__init__.py | 0 | 0 | 0 |
| CODEGUARDIAN/analyzers/circular_dependency_analyzer.py | 2 | 5 | 0 |
| CODEGUARDIAN/analyzers/function_analyzer.py | 2 | 6 | 5 |
| CODEGUARDIAN/analyzers/file_analyzer.py | 2 | 3 | 4 |
| CODEGUARDIAN/analyzers/db_access_analyzer.py | 2 | 2 | 1 |
| CODEGUARDIAN/config/config_loader.py | 1 | 1 | 2 |
| CODEGUARDIAN/config/__init__.py | 0 | 0 | 0 |
| CODEGUARDIAN/config/settings.py | 0 | 0 | 0 |
| CODEGUARDIAN/utils/layer_utils.py | 0 | 1 | 0 |
| CODEGUARDIAN/utils/file_cache.py | 1 | 1 | 2 |
| CODEGUARDIAN/utils/ast_cache.py | 1 | 1 | 3 |
| CODEGUARDIAN/utils/__init__.py | 0 | 0 | 0 |
| CODEGUARDIAN/cli/__init__.py | 0 | 0 | 0 |
| CODEGUARDIAN/cli/commands.py | 0 | 5 | 18 |
| CODEGUARDIAN/rules/__init__.py | 0 | 0 | 0 |
| CODEGUARDIAN/rules/architecture_validator.py | 2 | 3 | 2 |
| CODEGUARDIAN/rules/architecture_rules.py | 0 | 0 | 0 |
| CODEGUARDIAN/reports/severity.py | 0 | 1 | 0 |
| CODEGUARDIAN/reports/html_reporter.py | 1 | 2 | 1 |
| CODEGUARDIAN/reports/json_reporter.py | 1 | 1 | 1 |
| CODEGUARDIAN/reports/__init__.py | 0 | 0 | 0 |
| CODEGUARDIAN/reports/architecture_score.py | 1 | 2 | 1 |
| CODEGUARDIAN/reports/statistics_reporter.py | 1 | 2 | 3 |
| CODEGUARDIAN/reports/console_reporter.py | 1 | 9 | 5 |
| CODEGUARDIAN/reports/markdown_reporter.py | 1 | 1 | 0 |
| CODEGUARDIAN/src/__init__.py | 0 | 0 | 0 |
| CODEGUARDIAN/src/main.py | 0 | 0 | 7 |
| CODEGUARDIAN/src/tree/Walker.py | 0 | 1 | 1 |
| CODEGUARDIAN/src/tree/__init__.py | 0 | 0 | 0 |
| CODEGUARDIAN/src/discovery/finder.py | 0 | 1 | 1 |
| CODEGUARDIAN/src/discovery/__init__.py | 0 | 0 | 0 |
| CODEGUARDIAN/src/extractor/python_imports_extractor.py | 1 | 2 | 1 |
| CODEGUARDIAN/src/extractor/python_class_extractor.py | 1 | 2 | 1 |
| CODEGUARDIAN/src/extractor/__init__.py | 0 | 0 | 0 |
| CODEGUARDIAN/src/extractor/class_extractor.py | 1 | 2 | 2 |
| CODEGUARDIAN/src/extractor/import_extractor.py | 1 | 2 | 2 |
| CODEGUARDIAN/src/extractor/function_extractor.py | 1 | 2 | 2 |
| CODEGUARDIAN/src/extractor/python_function_extractor.py | 1 | 2 | 1 |
| CODEGUARDIAN/src/parser/ts_parser.py | 0 | 1 | 2 |
| CODEGUARDIAN/src/parser/__init__.py | 0 | 0 | 0 |
| CODEGUARDIAN/rules/controllers/user_controller.py | 1 | 2 | 1 |