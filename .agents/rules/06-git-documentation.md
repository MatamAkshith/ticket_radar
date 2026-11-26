
---
trigger: always_on
description: Automated local Git commits, version control safety and project documentation.
---

# Git and Documentation Standards

## 1. Git Inspection

- Inspect Git status before starting development.
- Identify existing uncommitted changes.
- Preserve all existing user modifications.
- Never overwrite or discard unrelated work.
- Follow the existing branch and repository structure.

## 2. Automated Local Commits

- AI agents are authorized to create local Git commits automatically.
- After completing a meaningful feature or development task, run relevant verification.
- Update project documentation before committing.
- Stage only files belonging to the completed task.
- Never stage unrelated user changes.
- Generate clear, meaningful commit messages.
- Prefer conventional commit prefixes:
  - feat: New functionality.
  - fix: Bug fixes.
  - docs: Documentation changes.
  - refactor: Code restructuring.
  - test: Testing changes.
  - chore: Maintenance tasks.
- Create separate commits for logically independent features.
- Do not create empty commits.
- Never commit code with known failing required tests.
- Never commit secrets, credentials or sensitive files.
- If unrelated or ambiguous changes cannot be safely separated, stop and report the situation instead of committing.

## 3. Git Push Policy

- Automatically creating local commits is permitted.
- Automatically pushing to remote repositories is NOT permitted.
- Do not add, change or remove Git remotes without user authorization.
- Do not push until the user provides or confirms the remote repository and explicitly requests a push.
- Never force-push.
- Never rewrite shared Git history without explicit approval.

## 4. Persistent Project Documentation

Every project should maintain:

docs/Project_Notes.md

Before starting a task:

1. Read Project_Notes.md.
2. Review the current development status.
3. Understand the architecture and workflow.
4. Review previous technical decisions.
5. Check completed and pending tasks.

After completing a task:

1. Update current development status.
2. Update architecture and workflow when affected.
3. Record significant technical decisions.
4. Update the progress tracker.
5. Update pending work.
6. Append a development log entry.
7. Record actual verification results.

## 5. Documentation Quality

- Keep documentation consistent with implementation.
- Preserve historical development entries.
- Explain important technical decisions.
- Never fabricate test results.
- Never mark unverified functionality as complete.

## 6. Completion Requirements

After completing a meaningful development task:

- Verify the implementation.
- Update documentation.
- Review the Git diff.
- Create an appropriate local commit.
- Report the commit hash and message.
- Report tests and build results.
- Identify remaining issues or limitations.

A task is complete only when implementation, verification, documentation and the appropriate local commit are complete.
