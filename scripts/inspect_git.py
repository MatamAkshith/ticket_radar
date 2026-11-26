
#!/usr/bin/env python3

"""
Foundation Git Inspector

Displays repository status without modifying Git state.
"""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent


def run_git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def main():
    print("\n====== FOUNDATION GIT INSPECTOR ======\n")

    check = run_git("rev-parse", "--is-inside-work-tree")

    if check.returncode != 0:
        print("[ERROR] This directory is not inside a Git repository.")
        return 1

    branch = run_git("branch", "--show-current")
    status = run_git("status", "--short")
    commit = run_git("log", "-1", "--oneline")

    if branch.returncode != 0 or status.returncode != 0:
        print("[ERROR] Unable to inspect Git status.")
        return 1

    print(f"Repository: {ROOT}")
    print(f"Branch: {branch.stdout.strip() or '(detached HEAD)'}")

    print("\nWorking Tree:")

    if status.stdout.strip():
        print(status.stdout)
    else:
        print("[CLEAN] No uncommitted changes.")

    print("Latest Commit:")

    if commit.returncode == 0 and commit.stdout.strip():
        print(commit.stdout.strip())
    else:
        print("[INFO] No commits found.")

    print("\nInspection complete. No Git changes were made.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
