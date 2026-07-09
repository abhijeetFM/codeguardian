from pathlib import Path

hook_dir = Path(".git/hooks")

hook_file = hook_dir / "pre-commit"

print(f"Git hooks directory: {hook_dir}")

if not hook_dir.exists():

    print("❌ Not a Git repository.")

    exit()

print("✅ Git repository found.")

hook_content = """#!/bin/sh

echo "Running CodeGuardian..."

python main.py scan

if [ $? -ne 0 ]; then

    echo "❌ Commit blocked."

    exit 1

fi

echo "✅ Commit allowed."

exit 0
"""

hook_file.write_text(
    hook_content,
    encoding="utf-8"
)

print("✅ Pre-commit hook installed.")