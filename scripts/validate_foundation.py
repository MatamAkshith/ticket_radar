#!/usr/bin/env python3
"""
Foundation Repository Validator v2

Validates repository structure, document content, skill and agent metadata,
and explicit workflow references.

Read-only. Uses Python standard-library functionality only.
"""

from pathlib import Path
import re
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

REQUIRED_SKILL_FIELDS = {"name", "description"}
REQUIRED_AGENT_FIELDS = {
    "name", "description", "mainAgent", "subagent"
}

errors = []
warnings = []
passed = 0


def report(status, message):
    """Print a validation result and update the appropriate collection."""
    global passed

    print(f"[{status}] {message}")

    if status == "PASS":
        passed += 1
    elif status == "ERROR":
        errors.append(message)
    elif status == "WARNING":
        warnings.append(message)


def read_file(path):
    """Read a UTF-8 file without modifying it."""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        report("ERROR", f"Cannot read {path.relative_to(ROOT)}: {exc}")
        return None


def check_directory(relative_path):
    path = ROOT / relative_path

    if path.is_dir():
        report("PASS", f"Directory: {relative_path}")
    else:
        report("ERROR", f"Missing directory: {relative_path}")


def check_file(relative_path):
    path = ROOT / relative_path

    if not path.is_file():
        report("ERROR", f"Missing file: {relative_path}")
        return False

    if read_file(path) is None:
        return False

    report("PASS", f"File: {relative_path}")
    return True


def parse_frontmatter(content, relative_path):
    """
    Parse the limited YAML frontmatter format used by Foundation.

    Supports:
      key: scalar
      key: true/false
      key:
        - item

    This is intentionally not a general-purpose YAML parser.
    """
    lines = content.splitlines()

    if not lines or lines[0].strip() != "---":
        report("ERROR", f"Missing opening frontmatter: {relative_path}")
        return None

    closing_index = None

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break

    if closing_index is None:
        report("ERROR", f"Missing closing frontmatter: {relative_path}")
        return None

    metadata = {}
    current_list = None

    for line_number, line in enumerate(
        lines[1:closing_index], start=2
    ):
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        key_match = re.match(
            r"^([A-Za-z][A-Za-z0-9_-]*):(?:[ \t]*(.*))?$",
            line,
        )

        if key_match:
            key = key_match.group(1)
            value = key_match.group(2) or ""

            if key in metadata:
                report(
                    "ERROR",
                    f"Duplicate metadata key '{key}' in "
                    f"{relative_path}:{line_number}",
                )
                return None

            if value.strip():
                metadata[key] = value.strip()
                current_list = None
            else:
                metadata[key] = []
                current_list = key

            continue

        list_match = re.match(r"^[ \t]+-[ \t]+(.+?)\s*$", line)

        if list_match and current_list:
            metadata[current_list].append(list_match.group(1))
            continue

        report(
            "ERROR",
            f"Unsupported frontmatter syntax in "
            f"{relative_path}:{line_number}",
        )
        return None

    return metadata, "\n".join(lines[closing_index + 1:])


def validate_document_headings(content, relative_path, required):
    headings = {
        re.sub(r"\s+", " ", match.group(1)).strip().casefold()
        for match in re.finditer(r"^#{1,6}\s+(.+?)\s*$", content, re.M)
    }

    missing = [
        heading for heading in required
        if heading.casefold() not in headings
    ]

    if missing:
        report(
            "ERROR",
            f"{relative_path} missing headings: {', '.join(missing)}",
        )
        return False

    return True


def validate_skill(skill_name):
    relative = f".agents/skills/{skill_name}/SKILL.md"
    path = ROOT / relative

    if not path.is_file():
        report("ERROR", f"Missing skill file: {relative}")
        return

    content = read_file(path)
    if content is None:
        return

    parsed = parse_frontmatter(content, relative)
    if parsed is None:
        return

    metadata, body = parsed
    valid = True

    for field in REQUIRED_SKILL_FIELDS:
        if not isinstance(metadata.get(field), str) or not metadata[field].strip():
            report("ERROR", f"{relative}: invalid or missing '{field}'")
            valid = False

    if metadata.get("name") != skill_name:
        report(
            "ERROR",
            f"{relative}: name must match directory '{skill_name}'",
        )
        valid = False

    if not body.strip():
        report("ERROR", f"{relative}: empty document body")
        valid = False

    if not validate_document_headings(
        body, relative, ["Objective", "Completion Criteria"]
    ):
        valid = False

    if valid:
        report("PASS", f"Skill: {skill_name}")


def validate_agent(path):
    relative = str(path.relative_to(ROOT))
    content = read_file(path)

    if content is None:
        return None

    parsed = parse_frontmatter(content, relative)
    if parsed is None:
        return None

    metadata, body = parsed
    valid = True

    for field in REQUIRED_AGENT_FIELDS:
        value = metadata.get(field)

        if value is None or not isinstance(value, str) or not value.strip():
            report("ERROR", f"{relative}: invalid or missing '{field}'")
            valid = False

    for field in ("mainAgent", "subagent"):
        if metadata.get(field) not in ("true", "false"):
            report("ERROR", f"{relative}: '{field}' must be true or false")
            valid = False

    if "tools" in metadata:
        tools = metadata["tools"]

        if not isinstance(tools, list) or not tools:
            report("ERROR", f"{relative}: tools must be a non-empty list")
            valid = False
        elif any(not isinstance(tool, str) or not tool.strip() for tool in tools):
            report("ERROR", f"{relative}: invalid tool entry")
            valid = False
        elif len(tools) != len(set(tools)):
            report("ERROR", f"{relative}: duplicate tool entries")
            valid = False

    if not body.strip():
        report("ERROR", f"{relative}: empty agent instructions")
        valid = False

    if valid:
        report("PASS", f"Agent metadata: {path.name}")

    return metadata.get("name") if valid else None


def validate_workflow(path, skill_names, agent_names):
    relative = str(path.relative_to(ROOT))
    content = read_file(path)

    if content is None:
        return

    valid = True

    required = ["Completion Criteria"]

    if not validate_document_headings(
        content, relative, required
    ):
        valid = False

    if not re.search(r"^#\s+Workflow\s+\d+", content, re.M):
        report("ERROR", f"{relative}: missing numbered workflow title")
        valid = False

    if not re.search(r"^##\s+(Purpose|Objective)\s*$", content, re.M):
        report("ERROR", f"{relative}: missing Purpose or Objective section")
        valid = False

    if not re.search(r"^##\s+(Workflow|Process)\s*$", content, re.M):
        report("ERROR", f"{relative}: missing Workflow or Process section")
        valid = False

    # Validate explicitly declared primary and supporting skills.
    primary = re.search(
        r"^##\s+Primary Skill\s*\n+`([^`]+)`",
        content,
        re.M,
    )

    if primary:
        name = primary.group(1).strip()
        if name not in skill_names:
            report("ERROR", f"{relative}: unknown primary skill '{name}'")
            valid = False
        else:
            report("PASS", f"{relative}: primary skill '{name}'")

    supporting = re.search(
        r"^##\s+Supporting Skills\s*\n(.*?)(?=^##\s|\Z)",
        content,
        re.M | re.S,
    )

    if supporting:
        for name in re.findall(r"^\s*-\s*`([^`]+)`", supporting.group(1), re.M):
            if name not in skill_names:
                report("ERROR", f"{relative}: unknown supporting skill '{name}'")
                valid = False

    
    # Validate explicitly listed responsible agents.
    responsible = re.search(
        r"^##\s+(Responsible Agents|Participants)\s*\n"
        r"(.*?)(?=^##\s|\Z)",
        content,
        re.M | re.S,
    )

    if responsible:
        # Convert metadata identifiers into human-readable names.
        display_names = {
            name.replace("-", " ").casefold(): name
            for name in agent_names
        }

        generic_roles = {
            "relevant development engineer",
            "relevant development engineers",
        }

        for line in responsible.group(2).splitlines():
            match = re.match(r"^\s*-\s*(.+?)\s*$", line)

            if not match:
                continue

            label = match.group(1).strip()

            # Remove conditional descriptions.
            label = re.sub(
                r",\s*when\b.*$",
                "",
                label,
                flags=re.I,
            ).strip()

            normalized = label.casefold()

            if normalized in generic_roles:
                report(
                    "WARNING",
                    f"{relative}: generic participant '{label}' "
                    "is not a specific agent",
                )
                continue

            if normalized not in display_names:
                report(
                    "ERROR",
                    f"{relative}: unknown agent '{label}'",
                )
                valid = False
            else:
                report(
                    "PASS",
                    f"{relative}: agent '{label}' resolved",
                )


    # Validate explicit references to rule files.
    for rule in re.findall(
        r"\.agents/rules/[A-Za-z0-9_.-]+\.md",
        content,
    ):
        if not (ROOT / rule).is_file():
            report("ERROR", f"{relative}: missing rule reference '{rule}'")
            valid = False

    if valid:
        report("PASS", f"Workflow: {path.name}")


def validate_template(path):
    relative = str(path.relative_to(ROOT))
    content = read_file(path)

    if content is None:
        return

    if not content.strip():
        report("ERROR", f"Empty template: {relative}")
        return

    if not re.search(r"^#\s+\S+", content, re.M):
        report("ERROR", f"{relative}: missing H1 title")
        return

    report("PASS", f"Template: {path.name}")


def main():
    print("\n======================================")
    print("       FOUNDATION VALIDATOR v2")
    print("======================================\n")

    print("Checking directories...\n")
    for directory in REQUIRED_DIRECTORIES:
        check_directory(directory)

    print("\nChecking required files...\n")
    for filename in REQUIRED_FILES:
        check_file(filename)

    print("\nChecking skills...\n")
    skill_names = set(REQUIRED_SKILLS)

    for skill in REQUIRED_SKILLS:
        validate_skill(skill)

    print("\nChecking agents...\n")
    agent_directory = ROOT / ".agents/agents"
    agent_names = set()
    seen_names = set()

    if agent_directory.is_dir():
        for path in sorted(agent_directory.glob("*.md")):
            name = validate_agent(path)

            if name:
                if name in seen_names:
                    report("ERROR", f"Duplicate agent name: {name}")
                seen_names.add(name)
                agent_names.add(name)

            if path.name == "agent-discovery-test.md":
                report(
                    "WARNING",
                    "Temporary test agent is present: agent-discovery-test.md",
                )

    missing_agents = set(REQUIRED_AGENTS) - {
        path.name for path in agent_directory.glob("*.md")
    } if agent_directory.is_dir() else set()

    for filename in sorted(missing_agents):
        report("ERROR", f"Missing required agent: {filename}")

    print("\nChecking workflows...\n")
    workflow_directory = ROOT / "workflows"

    if workflow_directory.is_dir():
        for path in sorted(workflow_directory.glob("0*.md")):
            validate_workflow(path, skill_names, agent_names)

    print("\nChecking templates...\n")
    for template in REQUIRED_TEMPLATES:
        validate_template(ROOT / "templates" / template)

    print("\nChecking rules...\n")
    for rule in sorted((ROOT / ".agents/rules").glob("*.md")):
        content = read_file(rule)

        if content is not None and re.search(r"^#\s+\S+", content, re.M):
            report("PASS", f"Rule: {rule.name}")
        elif content is not None:
            report("ERROR", f"Rule missing H1 title: {rule.name}")

    print("\n======================================")
    print("                RESULTS")
    print("======================================")
    print(f"\nPassed:   {passed}")
    print(f"Warnings: {len(warnings)}")
    print(f"Errors:   {len(errors)}")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"  [WARNING] {warning}")

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"  [ERROR] {error}")

        print("\n[FAIL] Foundation validation failed.")
        return 1

    print("\n[PASS] Foundation validation successful.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
