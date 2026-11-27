---
name: bug-fixing
description: Systematically investigates, reproduces, diagnoses and fixes software defects. Includes root cause analysis, regression testing, documentation and automated local commits. Use whenever debugging an application, resolving an error or fixing unexpected behavior.
---

# Bug Fixing

## Objective

Resolve software defects by identifying and correcting their root causes rather than applying superficial workarounds.

Every fix must be evidence-based, narrowly scoped and verified against the original failure.

## 1. Understand the Bug

- Read `docs/Project_Notes.md`.
- Understand the reported behavior.
- Identify the expected behavior.
- Identify the actual behavior.
- Collect error messages and relevant logs.
- Identify affected users and functionality.
- Determine the severity and impact.
- Identify relevant environmental conditions.

Ask for missing information when necessary.

Distinguish confirmed symptoms from assumptions about the cause.

## 2. Inspect the Repository

- Inspect relevant source files.
- Understand the affected execution path.
- Review recent relevant changes when useful.
- Inspect dependencies.
- Review related tests.
- Inspect relevant configuration.
- Check Git status.
- Preserve existing user modifications.

Identify the current implementation before proposing changes.

Do not immediately modify code.

## 3. Establish a Baseline

Before implementing a fix:

- Run relevant existing tests when safe.
- Record existing failures.
- Check whether the affected functionality currently builds.
- Identify unrelated defects.
- Preserve the original failure evidence.
- Determine whether the issue is new or pre-existing when possible.

Do not attribute existing failures to the current bug without evidence.

## 4. Reproduce the Problem

Attempt to reproduce the defect using available evidence.

Determine:

- Steps required to reproduce it.
- Input conditions.
- Environment conditions.
- Expected output.
- Actual output.
- Whether the issue occurs consistently.
- Whether the failure depends on timing or external conditions.

If the problem cannot be reproduced, report that limitation.

Do not claim reproduction without evidence.

When practical, create a minimal reproduction or regression test that demonstrates the failure.

## 5. Perform Root Cause Analysis

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
- Data integrity and transaction handling.

Identify the most likely root cause and support it with evidence.

Distinguish:

- Confirmed root cause.
- Strongly supported hypothesis.
- Unverified hypothesis.

Do not modify unrelated components based on speculation.

## 6. Plan the Fix

- Define the intended correction.
- Identify affected modules.
- Assess regression risks.
- Identify required tests.
- Consider compatibility issues.
- Consider data migration requirements when applicable.
- Identify security implications.

Prefer the smallest reliable correction.

Do not weaken validation, authorization, security controls or test assertions merely to make a failure disappear.

## 7. Implement the Fix

- Modify only relevant functionality.
- Preserve existing architecture.
- Avoid unrelated refactoring.
- Handle relevant edge cases.
- Maintain security and data integrity.
- Preserve existing user changes.
- Explain significant implementation changes.

For database-related defects:

- Preserve existing data.
- Use appropriate migrations.
- Avoid destructive schema changes without authorization.
- Verify migration behavior safely.

For external integration defects:

- Check documented platform behavior and permitted access methods.
- Handle timeouts, failures and unexpected responses.
- Do not bypass authentication, rate limits or anti-bot protections.

## 8. Verify the Fix

- Reproduce the original failure where practical.
- Apply the fix.
- Verify the original scenario again.
- Run relevant unit tests.
- Run integration tests where applicable.
- Run regression tests.
- Verify builds where relevant.
- Check for unintended side effects.

A bug is not resolved merely because the error message disappears.

Verification must demonstrate that:

- The original failure is addressed.
- Expected behavior is restored.
- Relevant edge cases are handled.
- Existing functionality remains intact.

If the original failure cannot be reproduced again, explain the limitation and provide the available verification evidence.

## 9. Review the Fix

Request code review when appropriate.

Check:

- Whether the root cause was actually addressed.
- Whether the fix introduces new defects.
- Whether existing functionality remains intact.
- Whether tests cover the failure scenario.
- Whether security was preserved.
- Whether the implementation introduces unnecessary complexity.
- Whether documentation remains accurate.

## 10. Update Project Documentation

Update `docs/Project_Notes.md` when meaningful:

- Record the defect.
- Record its root cause or current uncertainty.
- Document the correction.
- Update known issues.
- Update the development log.
- Record verification results.
- Document remaining limitations.

Preserve historical development entries.

Do not claim a defect is resolved when verification is incomplete.

## 11. Automated Git Commit

Follow `.agents/rules/06-git-documentation.md`.

After successful verification:

- Review the Git diff.
- Confirm the active branch.
- Stage only relevant bug-fix changes.
- Exclude unrelated user modifications.
- Ensure secrets and sensitive files are excluded.
- Create a meaningful local commit.
- Report the commit hash and message.

Never automatically push to GitHub or another remote.

Do not rewrite existing commits or perform destructive Git operations without authorization.

If changes cannot be safely separated from unrelated modifications, stop and report the issue.

## 12. Retry and Escalation

If the fix fails:

- Re-examine the root cause.
- Review new evidence.
- Reassess the original hypothesis.
- Avoid repeatedly applying speculative changes.
- Use a bounded number of repair attempts.
- Run relevant regression checks after each meaningful correction.
- Report unresolved issues and blockers.

Stop and request guidance when the problem requires missing credentials, privileged access, destructive operations or a decision that belongs to the user.

Do not conceal repeated failures.

## 13. Final Report

Report:

- Original problem.
- Expected and actual behavior.
- Reproduction steps.
- Root cause and supporting evidence.
- Implemented correction.
- Files changed.
- Tests performed.
- Verification results.
- Local Git commit.
- Remaining limitations.

Clearly distinguish confirmed results from unresolved hypotheses.

## Completion Criteria

A bug fix is complete when:

- The root cause is identified or adequately explained.
- The correction is implemented.
- The original failure is verified as resolved.
- Relevant regression checks pass.
- Existing functionality remains intact.
- Documentation is updated.
- An appropriate local commit is created.
- Remaining limitations are accurately reported.