
---
name: bug-fixing
description: Systematically investigates, reproduces, diagnoses and fixes software defects. Includes root cause analysis, regression testing, documentation and automated local commits. Use whenever debugging an application, resolving an error or fixing unexpected behavior.
---

# Bug Fixing

## Objective

Resolve software defects by identifying and correcting their root causes rather than applying superficial workarounds.

## 1. Understand the Bug

- Read docs/Project_Notes.md.
- Understand the reported behavior.
- Identify the expected behavior.
- Identify the actual behavior.
- Collect error messages and relevant logs.
- Identify affected users and functionality.
- Determine the severity and impact.

Ask for missing information when necessary.

## 2. Inspect the Repository

- Inspect relevant source files.
- Understand the affected execution path.
- Review recent relevant changes when useful.
- Inspect dependencies.
- Review related tests.
- Check Git status.
- Preserve existing user modifications.

Do not immediately modify code.

## 3. Reproduce the Problem

Attempt to reproduce the defect using available evidence.

Determine:

- Steps required to reproduce it.
- Input conditions.
- Environment conditions.
- Expected output.
- Actual output.
- Whether the issue occurs consistently.

If the problem cannot be reproduced, report that limitation.

Do not claim reproduction without evidence.

## 4. Perform Root Cause Analysis

Investigate relevant areas:

- Application logic.
- Frontend behavior.
- Backend processing.
- API communication.
- Database operations.
- Authentication and authorization.
- External integrations.
- Configuration.
- Environment differences.
- Race conditions and asynchronous behavior.

Identify the most likely root cause and support it with evidence.

Distinguish confirmed causes from hypotheses.

## 5. Plan the Fix

- Define the intended correction.
- Identify affected modules.
- Assess regression risks.
- Identify required tests.
- Consider whether the fix introduces compatibility issues.

Prefer the smallest reliable correction.

## 6. Implement the Fix

- Modify only relevant functionality.
- Preserve existing architecture.
- Avoid unrelated refactoring.
- Handle relevant edge cases.
- Maintain security and data integrity.
- Explain significant implementation changes.

## 7. Verify the Fix

- Reproduce the original failure where practical.
- Apply the fix.
- Verify the original scenario again.
- Run relevant unit tests.
- Run integration tests where applicable.
- Run regression tests.
- Verify builds where relevant.
- Check for unintended side effects.

A bug is not resolved merely because the error message disappears.

## 8. Review the Fix

Request code review when appropriate.

Check:

- Whether the root cause was actually addressed.
- Whether the fix introduces new defects.
- Whether existing functionality remains intact.
- Whether tests cover the failure scenario.
- Whether security was preserved.

## 9. Update Project Documentation

Update docs/Project_Notes.md when meaningful:

- Record the defect.
- Record its root cause.
- Document the correction.
- Update known issues.
- Update the development log.
- Record verification results.

## 10. Automated Git Commit

Follow .agents/rules/06-git-documentation.md.

After successful verification:

- Review the Git diff.
- Stage only relevant bug-fix changes.
- Create a meaningful local commit.
- Report the commit hash.

Never automatically push to GitHub.

Do not commit unrelated changes.

## 11. Retry and Escalation

If the fix fails:

- Re-examine the root cause.
- Review new evidence.
- Avoid repeatedly applying speculative changes.
- Use a bounded number of repair attempts.
- Report unresolved issues and blockers.

Stop and request guidance when the problem requires missing credentials, privileged access or destructive operations.

## 12. Final Report

Report:

- Original problem.
- Reproduction steps.
- Root cause.
- Implemented correction.
- Files changed.
- Tests performed.
- Verification results.
- Local Git commit.
- Remaining limitations.

## Completion Criteria

A bug fix is complete when the root cause is addressed, the original failure is verified as resolved, relevant regression checks pass, documentation is updated and an appropriate local commit is created.
