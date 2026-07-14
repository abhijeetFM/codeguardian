from config.config_loader import (
    ConfigLoader
)


config = ConfigLoader.load()

print(
    "\nLoaded Configuration:\n"
)

for key, value in config.items():

    print(
        f"{key}: {value}"
    )