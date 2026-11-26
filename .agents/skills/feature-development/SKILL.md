
---
name: feature-development
description: Manages end-to-end software feature development, including requirement analysis, repository inspection, implementation planning, specialist delegation, coding, testing, documentation and automated local commits. Use whenever implementing or extending a software feature.
---

# Feature Development

## Objective

Implement software features in a structured, incremental and verifiable manner.

Every feature must be understood, planned, implemented, tested, documented and committed appropriately.

## 1. Understand the Requirement

- Read docs/Project_Notes.md.
- Understand the requested feature.
- Identify the problem it solves.
- Identify affected user journeys.
- Identify functional requirements.
- Identify relevant non-functional requirements.
- Clarify important ambiguities.

Do not start implementation based on incomplete assumptions.

## 2. Inspect the Repository

- Inspect relevant source files.
- Understand existing architecture.
- Identify reusable components.
- Review existing API contracts.
- Inspect database dependencies.
- Check relevant tests.
- Inspect Git status.

Preserve unrelated user modifications.

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

## 4. Create an Implementation Plan

- Identify affected modules.
- Break implementation into manageable tasks.
- Identify dependencies.
- Define verification requirements.
- Determine whether specialist delegation is useful.

Keep the implementation scope focused.

## 5. Delegate Implementation

When appropriate:

- Use frontend-engineer for UI work.
- Use backend-engineer for APIs and business logic.
- Use database-engineer for schema and data changes.
- Keep the orchestrator responsible for coordination and integration.

Avoid unnecessary parallel execution.

## 6. Implement Incrementally

- Follow approved architecture.
- Reuse existing functionality.
- Make focused changes.
- Maintain compatibility with existing features.
- Handle errors and edge cases.
- Avoid unrelated refactoring.
- Keep API and database contracts consistent.

## 7. Verify Implementation

- Run relevant unit tests.
- Run integration tests where applicable.
- Verify application builds.
- Test important user journeys.
- Check error handling.
- Validate acceptance criteria.
- Request QA review when appropriate.
- Request code review for meaningful changes.
- Perform security review when the feature affects sensitive functionality.

Fix identified defects and repeat relevant checks.

## 8. Update Project Documentation

Update docs/Project_Notes.md:

- Record the implemented feature.
- Update affected architecture sections.
- Update workflow documentation where necessary.
- Record important technical decisions.
- Update the progress tracker.
- Update pending work.
- Append a development log entry.
- Record actual verification results.

## 9. Automated Git Commit

Follow .agents/rules/06-git-documentation.md.

After successful verification:

- Review the Git diff.
- Stage only files belonging to this feature.
- Exclude unrelated user changes.
- Create a meaningful local commit.
- Report the commit hash.

Never automatically push to GitHub.

If changes cannot be safely separated from unrelated modifications, stop and report the issue.

## 10. Final Report

Report:

- Feature implemented.
- Implementation summary.
- Files changed.
- Tests performed.
- Verification results.
- Documentation updates.
- Local Git commit.
- Remaining issues or limitations.

## Completion Criteria

A feature is complete when its acceptance criteria are satisfied, relevant verification passes, documentation is updated and an appropriate local commit is created.
