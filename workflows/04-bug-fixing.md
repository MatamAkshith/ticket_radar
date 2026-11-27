# Workflow 04 — Bug Fixing

## Purpose

Establish a systematic process for identifying, reproducing, diagnosing, fixing and verifying software defects.

The workflow prioritizes root-cause analysis, minimal corrections, regression prevention and evidence-based verification.

The Engineering Orchestrator coordinates the process and remains responsible for integration and final reporting.

## Primary Skill

`bug-fixing`

## Supporting Skills

- `repository-audit` — When the affected implementation is not sufficiently understood.
- `feature-development` — When the correction requires significant feature-level changes.
- `release-verification` — When verifying a release after critical fixes.

Invoke supporting skills when relevant.

## Responsible Agents

- Engineering Orchestrator
- Relevant Development Engineer
- QA Engineer
- Code Reviewer
- Security Engineer, when required

## Workflow

### 1. Understand the Bug

- Identify the reported issue.
- Understand expected versus actual behavior.
- Collect error messages, logs and reproduction steps.
- Determine the affected functionality.
- Identify affected users and severity.
- Review relevant project documentation.
- Read `docs/Project_Notes.md`.

Distinguish confirmed symptoms from assumptions about the cause.

### 2. Inspect the Existing System

- Inspect relevant source files.
- Understand the affected execution path.
- Review recent relevant changes when useful.
- Examine dependencies and integrations.
- Check relevant database operations and API behavior.
- Review existing tests.
- Inspect Git status.

Preserve existing user modifications.

Do not immediately modify code.

### 3. Establish a Baseline and Reproduce

- Run relevant existing tests when safe.
- Record existing failures.
- Reproduce the issue using the available environment.
- Record input and environment conditions.
- Document expected and actual results.
- Determine whether the issue occurs consistently or intermittently.

Preserve evidence of the original failure.

If the problem cannot be reproduced, report that limitation.

Do not claim reproduction without evidence.

### 4. Diagnose the Root Cause

- Inspect relevant source code.
- Trace the execution flow.
- Examine dependencies and integrations.
- Check database operations and API behavior where relevant.
- Investigate configuration and environment differences.
- Examine asynchronous behavior and race conditions where applicable.
- Identify the actual root cause rather than treating symptoms.

Support conclusions with evidence.

Distinguish confirmed causes from hypotheses.

### 5. Plan the Fix

- Define the smallest safe correction.
- Identify affected components.
- Evaluate possible side effects.
- Assess compatibility and data-integrity risks.
- Define regression tests.
- Identify security implications.

Do not weaken validation, authorization or existing safeguards to make an error disappear.

### 6. Implement the Fix

- Modify only the necessary files.
- Preserve existing architecture and conventions.
- Avoid unrelated refactoring.
- Add or update tests where appropriate.
- Handle relevant edge cases.
- Preserve unrelated user modifications.

The orchestrator must review implementation changes before integration.

### 7. Verify the Fix

- Confirm the original issue is resolved under the relevant conditions.
- Run relevant automated tests.
- Perform regression testing.
- Check related edge cases.
- Verify builds where relevant.
- Check that existing functionality remains intact.
- Review unintended side effects.

For intermittent defects, document the available evidence and limitations rather than claiming guaranteed resolution.

### 8. Review and Correct

- Review the code changes.
- Check security implications.
- Request independent code review when appropriate.
- Resolve identified defects.
- Repeat failed verification.
- Run relevant regression tests after corrections.

Use bounded correction attempts.

If the issue remains unresolved, reassess the root-cause hypothesis and report the blocker instead of repeatedly applying speculative changes.

### 9. Document

Document:

- Original defect.
- Reproduction conditions.
- Root cause or remaining uncertainty.
- Implemented correction.
- Affected components.
- Regression tests.
- Verification results.
- Known limitations.

Update `docs/Project_Notes.md` when meaningful.

Preserve historical development entries.

### 10. Git Operations

Follow `.agents/rules/06-git-documentation.md`.

- Inspect the Git diff.
- Confirm the active branch.
- Stage only bug-fix-related files.
- Exclude unrelated user modifications.
- Ensure secrets and sensitive files are excluded.
- Create a local commit after successful verification.
- Record the commit hash and message.

Do not push without explicit user authorization.

Do not perform destructive Git operations or rewrite existing commits without authorization.

### 11. Final Bug-Fix Report

Provide:

- Original problem.
- Expected versus actual behavior.
- Reproduction steps and evidence.
- Root cause.
- Implemented correction.
- Files changed.
- Tests performed.
- Verification results.
- Regression results.
- Documentation updates.
- Local Git commit.
- Remaining limitations.

Clearly distinguish confirmed results from unresolved hypotheses.

## Execution Boundaries

- Do not modify unrelated functionality.
- Preserve existing user work.
- Do not perform destructive database operations without authorization.
- Do not expose credentials.
- Do not bypass security controls.
- Do not conceal failed verification.
- Escalate blockers requiring privileged access or user decisions.

## Completion Criteria

- The original issue is verified as resolved, or its unresolved status is explicitly reported.
- Root cause is documented.
- Relevant tests pass.
- No unresolved blocking regressions remain.
- Documentation is updated.
- Git changes are reviewed and appropriately committed.
- Final bug-fix report is provided.