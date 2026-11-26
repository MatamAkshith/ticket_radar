
# Foundation Scripts

## Purpose

This directory contains utility scripts that support the Foundation Engineering System.

These scripts help validate repository structure, inspect configuration, and automate repeatable engineering checks.

## Design Principles

1. Prefer Python standard-library functionality.
2. Keep scripts portable across development environments.
3. Never modify project files unexpectedly.
4. Avoid destructive operations.
5. Provide clear and actionable error messages.
6. Return appropriate exit codes.
7. Document prerequisites and usage.

## Available Scripts

| Script | Purpose | Behavior |
|---|---|---|
| `validate_foundation.py` | Validate Foundation repository structure and essential files | Read-only |

## Usage

Run scripts from the Foundation repository root.

Example:

```bash
python3 scripts/validate_foundation.py
```

## Safety Policy

- Scripts must not delete files.
- Scripts must not overwrite user content.
- Scripts must not expose secrets.
- Scripts must not automatically push Git changes.
- Any future script that modifies files must clearly document its behavior and safeguards.

## Future Utilities

Potential additions:

- Project structure generator.
- Project documentation initializer.
- Git state inspection.
- Documentation consistency checker.
- Test and quality gate runner.
- Project setup assistant.
