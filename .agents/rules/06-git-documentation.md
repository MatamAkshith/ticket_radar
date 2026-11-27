---
trigger: always_on
description: Automated local Git commits, version control safety and project documentation.
---

# Git and Documentation Standards

## 1. Git Inspection

Before modifying the repository:

- Inspect the current Git status.
- Identify the active branch and configured remotes.
- Identify staged, unstaged and untracked changes.
- Review existing modifications before editing affected files.
- Preserve all user changes and unrelated work.
- Follow the existing branch and repository structure.
- Never assume the working tree is clean.

## 2. Automated Local Commits

AI agents are authorized to create local Git commits automatically.

After completing a meaningful development task:

1. Run the relevant verification.
2. Update affected project documentation.
3. Review the complete Git diff.
4. Confirm that only task-related files are staged.
5. Create a meaningful local commit.

Commit standards:

- Stage only files belonging to the completed task.
- Never include unrelated staged or unstaged changes.
- Never stage the entire repository blindly using `git add .` or `git add -A`.
- Never create empty commits.
- Never commit code with known failing required tests.
- Never commit secrets, credentials, API keys or sensitive files.
- Use clear, meaningful commit messages.
- Prefer conventional commit prefixes:
  - `feat:` New functionality.
  - `fix:` Bug fixes.
  - `docs:` Documentation changes.
  - `refactor:` Code restructuring.
  - `test:` Testing changes.
  - `chore:` Maintenance tasks.
- Create separate commits for logically independent tasks.
- If unrelated or ambiguous changes cannot be safely separated, stop and report the situation.

## 3. Git Safety

The following operations require explicit user authorization:

- Pushing changes to a remote repository.
- Changing, adding or removing Git remotes.
- Force-pushing.
- Rewriting shared Git history.
- Deleting branches containing unmerged work.
- Discarding user changes or performing destructive cleanup.

Additional rules:

- Local commits are permitted without individual approval.
- Never push automatically.
- Never force-push.
- Never reset, clean, restore or delete files to resolve an issue without first establishing that the affected work is safe to remove and obtaining approval where user work could be lost.
- Do not amend existing commits unless explicitly requested.
- Do not assume that a configured remote means pushing is authorized.

## 4. Persistent Project Documentation

Every project must maintain:

`docs/Project_Notes.md`

Before starting a task:

1. Read `Project_Notes.md`.
2. Review the current development status.
3. Understand the architecture and workflow.
4. Review previous technical decisions.
5. Check completed and pending tasks.

After completing a task, update the relevant sections:

1. Current development status.
2. Architecture and workflow, when affected.
3. Significant technical decisions.
4. Progress tracker.
5. Pending work.
6. Development log.
7. Actual verification results.

Documentation must reflect the actual state of the repository.

Do not rewrite historical development entries or remove useful project history.

## 5. Documentation Quality

- Keep documentation consistent with implementation.
- Preserve historical development entries.
- Explain important technical decisions and their rationale.
- Record unresolved issues and known limitations.
- Never fabricate test results.
- Never mark unverified functionality as complete.
- Distinguish implemented, partially implemented, planned and blocked features.
- Avoid duplicating information unnecessarily.
- Update README files when project setup, usage or architecture changes materially.

## 6. Verification and Completion

After completing a meaningful development task:

- Run relevant tests.
- Run the appropriate build or validation checks.
- Review the implementation and Git diff.
- Update affected documentation.
- Create an appropriate local commit.
- Record the commit hash and message.
- Report test and build results.
- Identify remaining issues or limitations.

If verification fails:

- Investigate the failure.
- Attempt reasonable, bounded fixes.
- Do not conceal or misrepresent failures.
- Do not commit a task as complete while required checks remain failing.
- Report blockers when they cannot be resolved safely.

A task is complete only when implementation, appropriate verification, documentation and the required local commit are complete.

## 7. Project-Specific Restrictions

For Ticket Radar:

- Monitoring must never trigger automated ticket purchases or payments.
- Do not commit platform credentials, Telegram bot tokens, environment files or personal data.
- Do not introduce undocumented external integrations.
- Do not bypass platform access restrictions or anti-bot protections.
- Preserve monitoring evidence and distinguish confirmed availability from failed or incomplete checks.
- Record important changes to platform adapters, monitoring behavior and notification logic in `Project_Notes.md`.