import json
import os


class ConfigLoader:

    DEFAULT_CONFIG = {

        "max_file_lines": 300,

        "max_function_lines": 50,

        "ignored_directories": [
            "venv",
            ".git",
            "__pycache__",
            ".pytest_cache"
        ],

        "forbidden_dependencies": [
            [
                "controllers",
                "repositories"
            ]
        ],

        "architecture_score": {

            "file_penalty": 10,

            "function_penalty": 5,

            "architecture_penalty": 20,

            "circular_dependency_penalty": 30
        }
    }

    @classmethod
    def load(
        cls,
        config_path="codeguardian.json"
    ):

        if not os.path.exists(config_path):

            print(
                "⚠ codeguardian.json not found."
            )

            print(
                "Using default configuration."
            )

            return cls.DEFAULT_CONFIG

        with open(
            config_path,
            "r",
            encoding="utf-8"
        ) as file:

            user_config = json.load(file)

        config = cls.DEFAULT_CONFIG.copy()

        config.update(user_config)

        return config