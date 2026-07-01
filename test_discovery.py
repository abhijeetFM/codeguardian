from pathlib import Path

from src.discovery.finder import discover_files


files = discover_files(
    Path("samples")
)

print("\nDiscovered files:\n")

for file in files:
    print(file)