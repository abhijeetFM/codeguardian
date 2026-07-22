import json
import os
from pathlib import Path


class ConfigLoader:

    @classmethod
    def load(
        cls,
        config_path="codeguardian.json"
    ):

        # Use user's configuration file if it exists
        if os.path.exists(config_path):

            with open(
                config_path,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        # Otherwise use the package's default configuration
        default_path = (
            Path(__file__).parent
            / "default_config.json"
        )

        with open(
            default_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)