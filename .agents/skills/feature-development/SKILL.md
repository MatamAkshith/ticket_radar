---
name: feature-development
description: Manages end-to-end software feature development, including requirement analysis, repository inspection, implementation planning, specialist delegation, coding, testing, documentation and automated local commits. Use whenever implementing or extending a software feature.
---

# Feature Development

## Objective

Implement software features in a structured, incremental and verifiable manner.

Every feature must be understood, planned, implemented, tested, documented and committed appropriately.

The engineering orchestrator remains responsible for coordination, integration and final verification.

## 1. Understand the Requirement

- Read `docs/Project_Notes.md`.
- Understand the requested feature.
- Identify the problem it solves.
- Identify affected user journeys.
- Identify functional requirements.
- Identify relevant non-functional requirements.
- Identify dependencies and constraints.
- Clarify important ambiguities.

Do not start implementation based on incomplete assumptions.

Distinguish confirmed requirements from assumptions and proposed behavior.

## 2. Inspect the Repository

- Inspect relevant source files.
- Understand existing architecture.
- Identify reusable components.
- Review existing API contracts.
- Inspect database dependencies.
- Check relevant tests.
- Inspect build and configuration files.
- Inspect Git status.

Preserve unrelated user modifications.

Understand existing implementation before deciding which files need changes.

Avoid duplicating existing functionality.

## 3. Define Acceptance Criteria

Create observable criteria describing successful implementation.

Consider:

- Expected functionality.
- Input validation.
- Error handling.
- Authorization.
- Data persistence.
- UI behavior.
- Integration requirements.
- Edge cases.
- Failure recovery.
- Compatibility with existing functionality.

Acceptance criteria must be testable.

Avoid vague conditions such as "feature works correctly."

## 4. Create an Implementation Plan

- Identify affected modules.
- Break implementation into manageable tasks.
- Identify dependencies.
- Define shared interfaces and API contracts.
- Define file ownership when multiple agents are involved.
- Define verification requirements.
- Identify risks and blockers.
- Determine whether specialist delegation is useful.

Keep the implementation scope focused.

Do not begin implementation until the required interfaces and dependencies are sufficiently clear.

## 5. Delegate Implementation

When appropriate:

- Use `frontend-engineer` for UI work.
- Use `backend-engineer` for APIs and business logic.
- Use `database-engineer` for schema and data changes.
- Use `qa-engineer` for test planning and verification.
- Use `code-reviewer` for independent code review.
- Use `security-engineer` when security-sensitive functionality is affected.

Keep the orchestrator responsible for coordination and integration.

Delegation requirements:

- Provide clear task descriptions.
- Specify relevant files and modules.
- Define expected inputs and outputs.
- Establish dependencies.
- Avoid conflicting modifications.
- Require agents to report their changes and verification results.

Avoid unnecessary parallel execution.

## 6. Implement Incrementally

- Follow approved architecture.
- Reuse existing functionality.
- Make focused changes.
- Maintain compatibility with existing features.
- Handle errors and edge cases.
- Avoid unrelated refactoring.
- Keep API and database contracts consistent.
- Preserve existing user changes.
- Verify meaningful implementation increments before integrating further changes.

Do not accept agent output without reviewing the changes.

The orchestrator must resolve integration conflicts and ensure that the complete feature works across affected components.

## 7. Verify Implementation

- Run relevant unit tests.
- Run integration tests where applicable.
- Verify application builds.
- Test important user journeys.
- Check error handling.
- Validate acceptance criteria.
- Run relevant regression tests.
- Request QA review when appropriate.
- Request code review for meaningful changes.
- Perform security review when the feature affects sensitive functionality.

For Ticket Radar, where applicable, verify:

- Availability normalization.
- Monitoring failure handling.
- Stale observation handling.
- Duplicate event prevention.
- Notification delivery and retry behavior.
- Platform adapter failure isolation.

Do not treat mocked external integrations as proof of successful production access.

Fix identified defects and repeat relevant checks.

Use bounded correction attempts. If a blocker cannot be resolved safely, report it.

Never conceal failing verification or weaken acceptance criteria to obtain a passing result.

## 8. Update Project Documentation

Update `docs/Project_Notes.md` where relevant:

- Record the implemented feature.
- Update affected architecture sections.
- Update workflow documentation where necessary.
- Record important technical decisions.
- Update the progress tracker.
- Update pending work.
- Append a development log entry.
- Record actual verification results.
- Document known limitations.

Preserve historical development entries.

Do not mark unverified functionality as complete.

## 9. Automated Git Commit

Follow `.agents/rules/06-git-documentation.md`.

After successful verification:

- Review the Git diff.
- Confirm the active branch.
- Stage only files belonging to this feature.
- Exclude unrelated user changes.
- Ensure secrets and sensitive files are excluded.
- Create a meaningful local commit.
- Record the commit hash and message.

Never automatically push to GitHub or another remote.

Do not rewrite existing commits or perform destructive Git operations without authorization.

If changes cannot be safely separated from unrelated modifications, stop and report the issue.

## 10. Final Report

Report:

- Feature implemented.
- Implementation summary.
- Files changed.
- Tests performed.
- Verification results.
- Regression results.
- Documentation updates.
- Local Git commit.
- Remaining issues or limitations.

Clearly distinguish successful checks from checks that were not run or remain blocked.

## Completion Criteria

A feature is complete when:

- Its acceptance criteria are satisfied.
- Relevant implementation is integrated.
- Required verification passes.
- Relevant regression checks pass.
- Documentation is updated.
- The Git diff has been reviewed.
- An appropriate local commit is created.
- Remaining limitations are accurately reported.