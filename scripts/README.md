# Foundation Scripts

## Purpose

This directory contains utility scripts that support the Foundation Engineering System.

These scripts help inspect repository state, validate essential project structure and perform repeatable engineering checks.

## Design Principles

1. Prefer Python standard-library functionality.
2. Keep scripts portable across development environments.
3. Never modify project files unexpectedly.
4. Avoid destructive operations.
5. Provide clear and actionable error messages.
6. Return appropriate exit codes.
7. Document prerequisites and usage.
8. Keep each script focused on a clearly defined responsibility.

## Available Scripts

| Script | Purpose | Behavior |
|---|---|---|
| `validate_foundation.py` | Validate Foundation repository structure, required files, skill metadata, agent metadata and templates | Read-only |
| `check_markdown.py` | Check Markdown files for empty content and trailing whitespace | Read-only |
| `inspect_git.py` | Inspect Git repository, branch, working-tree status and latest commit | Read-only |

## Prerequisites

- Python 3.
- Git installed for `inspect_git.py`.
- A Git repository for Git-specific inspection.

The scripts should not require third-party Python packages unless explicitly documented.

## Usage

Run scripts from any working directory. Each script determines the repository root from its own location.

From the repository root:

```bash
python3 scripts/validate_foundation.py
python3 scripts/check_markdown.py
python3 scripts/inspect_git.py
```

## Validation Scope

The current validation scripts provide basic repository and documentation checks.

They do not independently prove that:

- Agent instructions are executable.
- Skills and workflows are operational.
- Agent delegation works.
- Architecture and implementation are correct.
- Application tests pass.
- External integrations work.

These capabilities require separate verification.

Future improvements to `validate_foundation.py` should include stronger metadata validation, content checks and cross-reference consistency checks.

## Safety Policy

- Scripts must not delete files.
- Scripts must not overwrite user content.
- Scripts must not expose secrets.
- Scripts must not automatically push Git changes.
- Inspection scripts must not modify Git state.
- Validation scripts must not silently repair files.
- Any future script that modifies files must clearly document its behavior and safeguards.

## Future Utilities

Potential additions:

- Project structure generator.
- Project documentation initializer.
- Documentation consistency checker.
- Test and quality gate runner.
- Project setup assistant.
- Foundation execution diagnostics.