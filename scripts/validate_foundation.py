
#!/usr/bin/env python3

"""
Foundation Repository Validator

Checks the expected Foundation directory structure,
required documentation, skill files, and agent definitions.

This script is read-only. It does not modify any files.
"""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent

REQUIRED_DIRECTORIES = [
    ".agents/rules",
    ".agents/skills",
    ".agents/agents",
    "docs",
    "docs/architecture",
    "docs/guides",
    "docs/standards",
    "scripts",
    "templates",
    "workflows",
]

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "LICENSE",
    "docs/Project_Notes.md",
    ".agents/rules/01-architecture.md",
    ".agents/rules/02-coding-standards.md",
    ".agents/rules/03-testing-standards.md",
    ".agents/rules/04-security-standards.md",
    ".agents/rules/05-database-standards.md",
    ".agents/rules/06-git-documentation.md",
    "workflows/README.md",
    "workflows/01-new-project.md",
    "workflows/02-existing-project.md",
    "workflows/03-feature-development.md",
    "workflows/04-bug-fixing.md",
    "workflows/05-autonomous-sprint.md",
    "workflows/06-release-verification.md",
    "templates/README.md",
]

REQUIRED_SKILLS = [
    "project-discovery",
    "repository-audit",
    "architecture-design",
    "implementation-planning",
    "new-project-development",
    "existing-project-onboarding",
    "feature-development",
    "bug-fixing",
    "autonomous-sprint",
    "release-verification",
]

REQUIRED_AGENTS = [
    "engineering-orchestrator.md",
    "frontend-engineer.md",
    "backend-engineer.md",
    "database-engineer.md",
    "qa-engineer.md",
    "code-reviewer.md",
    "security-engineer.md",
]

REQUIRED_TEMPLATES = [
    "project-discovery-template.md",
    "architecture-template.md",
    "implementation-plan-template.md",
    "feature-spec-template.md",
    "bug-report-template.md",
    "adr-template.md",
    "development-report-template.md",
]


errors = []
warnings = []


def check_directory(relative_path):
    path = ROOT / relative_path

    if path.is_dir():
        print(f"[PASS] Directory: {relative_path}")
    else:
        errors.append(f"Missing directory: {relative_path}")


def check_file(relative_path):
    path = ROOT / relative_path

    if path.is_file():
        print(f"[PASS] File: {relative_path}")
    else:
        errors.append(f"Missing file: {relative_path}")


def read_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        errors.append(f"Could not read {path.relative_to(ROOT)}: {error}")
        return ""


def check_skill(skill_name):
    relative_path = f".agents/skills/{skill_name}/SKILL.md"
    path = ROOT / relative_path

    if not path.is_file():
        errors.append(f"Missing skill file: {relative_path}")
        return

    content = read_text(path)

    if not content.lstrip().startswith("---"):
        errors.append(f"Missing YAML frontmatter: {relative_path}")
        return

    if "\nname:" not in content:
        errors.append(f"Missing skill name metadata: {relative_path}")

    if "\ndescription:" not in content:
        errors.append(f"Missing skill description metadata: {relative_path}")

    if "\nname:" in content and "\ndescription:" in content:
        print(f"[PASS] Skill metadata: {skill_name}")


def check_agent(filename):
    relative_path = f".agents/agents/{filename}"
    path = ROOT / relative_path

    if not path.is_file():
        errors.append(f"Missing agent file: {relative_path}")
        return

    content = read_text(path)

    if not content.lstrip().startswith("---"):
        errors.append(f"Missing YAML frontmatter: {relative_path}")
        return

    for field in ("name:", "mainAgent:", "subagent:"):
        if f"\n{field}" not in content:
            errors.append(
                f"Missing agent metadata '{field}' in {relative_path}"
            )

    if all(f"\n{field}" in content for field in (
        "name:",
        "mainAgent:",
        "subagent:",
    )):
        print(f"[PASS] Agent metadata: {filename}")


def main():
    print("\n===================================")
    print("       FOUNDATION VALIDATOR")
    print("===================================\n")

    print("Checking directories...\n")
    for directory in REQUIRED_DIRECTORIES:
        check_directory(directory)

    print("\nChecking required files...\n")
    for filename in REQUIRED_FILES:
        check_file(filename)

    print("\nChecking skills...\n")
    for skill in REQUIRED_SKILLS:
        check_skill(skill)

    print("\nChecking agents...\n")
    for agent in REQUIRED_AGENTS:
        check_agent(agent)

    print("\nChecking templates...\n")
    for template in REQUIRED_TEMPLATES:
        check_file(f"templates/{template}")

    print("\n===================================")
    print("             RESULTS")
    print("===================================")

    if errors:
        print(f"\nFound {len(errors)} error(s):\n")

        for error in errors:
            print(f"[ERROR] {error}")

    if warnings:
        print(f"\nFound {len(warnings)} warning(s):\n")

        for warning in warnings:
            print(f"[WARNING] {warning}")

    if not errors:
        print("\n[PASS] Foundation structure validation successful.")
        return 0

    print("\n[FAIL] Foundation validation needs attention.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
