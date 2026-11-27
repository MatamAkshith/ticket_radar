# Workflow 03 — Feature Development

## Purpose

Define a consistent process for implementing new features in an existing project while preserving its architecture, coding standards and existing functionality.

The workflow must support incremental implementation, controlled specialist delegation and evidence-based verification.

The Engineering Orchestrator remains responsible for coordination, integration and final reporting.

## Primary Skill

`feature-development`

## Supporting Skills

- `repository-audit` — When the affected implementation or architecture is not sufficiently understood.
- `architecture-design` — When the feature introduces significant architectural changes.
- `implementation-planning` — When the feature requires multiple tasks, dependencies or specialist coordination.
- `release-verification` — When preparing a release or verifying a completed milestone.

Invoke supporting skills when relevant rather than mechanically executing every skill for every feature.

## Responsible Agents

- Engineering Orchestrator
- Frontend Engineer
- Backend Engineer
- Database Engineer
- QA Engineer
- Code Reviewer
- Security Engineer

Use only the agents required by the feature.

## Workflow

### 1. Understand the Feature

- Read `docs/Project_Notes.md`.
- Identify the requested functionality.
- Understand the problem it solves.
- Clarify expected behavior.
- Identify affected user journeys.
- Establish acceptance criteria.
- Identify constraints and dependencies.
- Clarify important ambiguities.

Do not begin implementation based on incomplete assumptions.

### 2. Inspect the Existing System

- Inspect relevant source files.
- Understand existing architecture and conventions.
- Identify reusable components and services.
- Review existing API contracts.
- Inspect database dependencies.
- Check existing tests.
- Review relevant configuration.
- Inspect Git status.

Preserve unrelated user modifications.

Do not duplicate existing functionality or introduce unnecessary architectural changes.

### 3. Plan the Implementation

- Break the feature into manageable tasks.
- Identify affected frontend, backend and database modules.
- Identify API and data model changes.
- Identify shared interfaces and dependencies.
- Identify security implications.
- Define verification criteria.
- Determine suitable specialist agents.
- Establish file ownership when necessary.

Use parallel execution only when tasks are sufficiently independent.

### 4. Delegate and Implement

- Delegate work to relevant specialist agents.
- Provide clear task boundaries and expected outputs.
- Follow existing project conventions.
- Follow approved architecture.
- Avoid unrelated modifications.
- Keep changes modular and maintainable.
- Implement incrementally.
- Maintain consistency across API and database contracts.

The orchestrator must review agent outputs and coordinate integration.

Do not accept delegated implementation without inspecting the changes.

### 5. Integrate and Verify

- Integrate completed components incrementally.
- Run relevant automated tests.
- Perform integration testing.
- Verify API and database behavior.
- Verify acceptance criteria.
- Check for regressions.
- Review error handling and edge cases.
- Verify builds where relevant.
- Request QA review when appropriate.

Record actual verification results.

Do not treat mocked integrations as proof of production functionality.

### 6. Review and Correct

- Perform code review.
- Review security implications.
- Identify architectural inconsistencies.
- Resolve identified defects.
- Repeat failed verification.
- Run relevant regression checks after corrections.

Use bounded correction attempts.

If a blocker cannot be resolved safely, report it instead of applying speculative changes.

### 7. Document

Update relevant documentation:

- Feature implementation details.
- Architecture changes.
- API contracts.
- Database changes.
- Technical decisions.
- Known limitations.
- Development progress.

Update `docs/Project_Notes.md` with:

- Implemented functionality.
- Affected architecture.
- Important decisions.
- Progress tracker.
- Pending work.
- Development log.
- Actual verification results.

Preserve historical entries.

### 8. Git Operations

Follow `.agents/rules/06-git-documentation.md`.

- Inspect the complete Git diff.
- Confirm the active branch.
- Stage only feature-related files.
- Exclude unrelated user modifications.
- Ensure secrets and sensitive files are excluded.
- Create a local commit after successful verification.
- Record the commit hash and message.

Do not push without explicit user authorization.

Do not perform destructive Git operations or rewrite existing commits without authorization.

### 9. Completion Report

Provide:

- Feature summary.
- Acceptance criteria results.
- Implementation details.
- Files changed.
- Agents involved.
- Tests performed.
- Verification results.
- Code review findings.
- Documentation updates.
- Local Git commit.
- Remaining issues or limitations.

Clearly distinguish verified functionality from incomplete or unverified behavior.

## Execution Boundaries

- Remain within the approved feature scope.
- Preserve existing functionality and user changes.
- Do not introduce unapproved paid services.
- Do not perform destructive database operations without authorization.
- Do not bypass security controls.
- Escalate decisions that materially affect cost, architecture, security or product behavior.
- Do not silently skip blocked tasks.

## Completion Criteria

- Feature meets its acceptance criteria.
- Relevant implementation is integrated.
- Required tests and verification pass.
- No unresolved blocking regressions remain.
- Documentation is updated.
- Git changes are reviewed and appropriately committed.
- The final implementation report is provided.