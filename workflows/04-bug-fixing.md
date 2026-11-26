
# Bug Fixing Workflow

## Purpose
Establish a systematic process for identifying, reproducing, diagnosing, fixing, and verifying software defects.

## Primary Skill
`bug-fixing`

## Supporting Skills
- `repository-audit`
- `feature-development`
- `release-verification`

## Responsible Agents
- Engineering Orchestrator
- Relevant Development Engineer
- QA Engineer
- Code Reviewer
- Security Engineer

## Workflow

### 1. Understand the Bug
- Identify the reported issue.
- Understand expected versus actual behavior.
- Collect error messages, logs, and reproduction steps.
- Determine the affected functionality.

### 2. Reproduce the Issue
- Inspect relevant project documentation.
- Read `docs/Project_Notes.md`.
- Reproduce the issue using the available environment.
- Record the conditions under which it occurs.

### 3. Diagnose the Root Cause
- Inspect relevant source code.
- Trace the execution flow.
- Examine dependencies and integrations.
- Check database operations and API behavior where relevant.
- Identify the actual root cause rather than treating symptoms.

### 4. Plan the Fix
- Define the smallest safe correction.
- Identify affected components.
- Evaluate possible side effects.
- Define regression tests.

### 5. Implement the Fix
- Modify only the necessary files.
- Preserve existing architecture and conventions.
- Avoid unrelated refactoring.
- Add or update tests where appropriate.

### 6. Verify the Fix
- Confirm the original issue is resolved.
- Run relevant automated tests.
- Perform regression testing.
- Check related edge cases.
- Verify that existing functionality remains intact.

### 7. Review and Document
- Review the code changes.
- Check security implications.
- Document the root cause and correction.
- Update `docs/Project_Notes.md`.

### 8. Git Operations
- Review the Git diff.
- Stage only bug-fix-related files.
- Create a local commit after successful verification.
- Do not push without explicit user authorization.

## Completion Criteria
- Original issue is reproducibly resolved.
- Root cause is documented.
- Relevant tests pass.
- No known regressions remain.
- Documentation is updated.
- Local Git commit is created.
- Final bug-fix report is provided.
