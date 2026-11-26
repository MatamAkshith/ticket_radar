
#!/usr/bin/env python3

"""
Foundation Markdown Checker

Checks Markdown files for:
- Empty files
- Trailing whitespace

Read-only utility. Does not modify files.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

EXCLUDED_DIRECTORIES = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
}


def find_markdown_files():
    files = []

    for path in ROOT.rglob("*.md"):
        if any(part in EXCLUDED_DIRECTORIES for part in path.parts):
            continue

        files.append(path)

    return sorted(files)


def check_file(path):
    relative_path = path.relative_to(ROOT)

    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        print(f"[ERROR] {relative_path}: {error}")
        return 1

    issues = 0

    if not content.strip():
        print(f"[ERROR] Empty Markdown file: {relative_path}")
        return 1

    for line_number, line in enumerate(content.splitlines(), start=1):
        if line.rstrip() != line:
            print(
                f"[WARNING] Trailing whitespace: "
                f"{relative_path}:{line_number}"
            )
            issues += 1

    if issues == 0:
        print(f"[PASS] {relative_path}")

    return issues


def main():
    print("\n====== FOUNDATION MARKDOWN CHECKER ======\n")

    files = find_markdown_files()

    if not files:
        print("[ERROR] No Markdown files found.")
        return 1

    total_issues = 0

    for path in files:
        total_issues += check_file(path)

    print("\n========================================")
    print(f"Markdown files checked: {len(files)}")
    print(f"Issues found: {total_issues}")

    if total_issues:
        print("[WARNING] Review the reported findings.")
        return 1

    print("[PASS] All Markdown files passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
