# Workflow 05 — Autonomous Sprint

## Purpose

Define how the Engineering Orchestrator coordinates a bounded development sprint, delegates tasks to specialist agents, integrates changes, verifies results and maintains project documentation.

The workflow enables controlled autonomous development while preserving engineering quality, project scope and user control.

The Engineering Orchestrator remains accountable for all sprint outcomes.

## Primary Skill

`autonomous-sprint`

## Supporting Skills

- `repository-audit` — Understand the current implementation when necessary.
- `implementation-planning` — Break approved work into actionable tasks.
- `feature-development` — Implement individual features.
- `bug-fixing` — Investigate and resolve defects.
- `release-verification` — Assess release readiness when required.

Invoke supporting skills according to task requirements.

## Responsible Agents

- Engineering Orchestrator
- Frontend Engineer
- Backend Engineer
- Database Engineer
- QA Engineer
- Code Reviewer
- Security Engineer

Use only agents relevant to the sprint.

## Workflow

### 1. Establish Sprint Context

- Read `AGENTS.md`.
- Read `docs/Project_Notes.md`.
- Inspect the current repository state.
- Review Git status and existing modifications.
- Review existing architecture and technology stack.
- Identify current project status and known issues.
- Review previous sprint progress.
- Identify available tools and resources.
- Understand the sprint objective and boundaries.

Preserve all existing user changes.

If resuming an interrupted sprint, verify the actual repository state before continuing.

### 2. Define Sprint Scope

- Identify approved tasks.
- Prioritize work according to importance and dependencies.
- Break work into small, independently verifiable tasks.
- Define expected outcomes.
- Establish acceptance criteria.
- Identify dependencies and risks.
- Define verification requirements.
- Identify tasks requiring user decisions.

Avoid expanding scope without user authorization.

Do not turn newly discovered opportunities into additional sprint commitments automatically.

### 3. Establish Task Tracking

Maintain explicit task states:

- Ready: Requirements and dependencies are satisfied.
- In Progress: Currently being implemented.
- Blocked: Missing information, dependencies or authorization.
- Verification Pending: Implementation exists but required checks remain incomplete.
- Completed: Implementation and required verification have succeeded.
- Failed: Implementation or verification did not succeed.
- Deferred: Intentionally postponed.

Maintain task ownership, dependencies and progress.

Never mark a task completed based solely on an agent's success report.

### 4. Plan and Delegate

- Assign tasks to appropriate specialist agents.
- Establish clear responsibilities.
- Identify files and modules likely to be affected.
- Define expected inputs and outputs.
- Define verification criteria for each task.
- Coordinate dependencies between agents.
- Establish shared interface contracts.
- Define file ownership where necessary.

Use parallel execution only when tasks are sufficiently independent.

Avoid concurrent modifications to shared files, database schemas or unfinished interfaces.

The orchestrator must coordinate delegation and resolve ownership conflicts.

### 5. Execute Development

For each task:

1. Understand the requirement.
2. Inspect relevant implementation.
3. Confirm dependencies.
4. Implement the assigned change.
5. Run targeted verification.
6. Review the implementation.
7. Integrate completed work where appropriate.
8. Resolve identified defects.
9. Update relevant documentation.
10. Create an appropriate local commit after successful verification.
11. Update task status.

Follow project architecture and engineering rules.

Preserve existing user changes.

Avoid unnecessary refactoring.

Report blockers instead of making risky assumptions.

### 6. Integrate Changes

- Review specialist outputs.
- Inspect actual file changes.
- Integrate completed work incrementally.
- Resolve integration conflicts.
- Verify compatibility between components.
- Validate shared API and database contracts.
- Run integration checks after meaningful merges.

Do not assume individually successful tasks automatically produce a working integrated system.

The orchestrator owns final integration.

### 7. Quality Assurance

- Run relevant unit tests.
- Check integration behavior.
- Verify API and database behavior.
- Review error handling and edge cases.
- Perform regression testing.
- Perform security checks where relevant.
- Verify sprint acceptance criteria.
- Review build results.

Record actual verification results.

Distinguish passed, failed, skipped, blocked and unexecuted checks.

Do not weaken tests or conceal failures to complete a sprint.

### 8. Failure Recovery

When implementation or verification fails:

1. Collect relevant logs and evidence.
2. Identify the affected task.
3. Investigate the likely root cause.
4. Assign a focused correction.
5. Re-run the failed verification.
6. Perform relevant regression checks.
7. Update task status.

Use bounded correction attempts.

If a blocker requires a user decision, privileged access or an unsafe operation, pause the affected task and report it.

Continue other independent ready tasks only when safe and within the approved scope.

### 9. Documentation

Update relevant technical documentation.

Maintain `docs/Project_Notes.md` with:

- Current development phase.
- Sprint objective and progress.
- Completed tasks.
- Pending tasks.
- Blocked and deferred tasks.
- Architecture changes.
- Technical decisions.
- Development log.
- Verification results.
- Known issues and limitations.

Preserve historical entries.

Ensure documentation reflects actual implementation rather than planned functionality.

### 10. Git Operations

Follow `.agents/rules/06-git-documentation.md`.

- Inspect the complete Git diff.
- Confirm the active branch.
- Stage only sprint-related changes.
- Preserve unrelated user modifications.
- Exclude secrets and credentials.
- Create local commits after successful verification.
- Record commit hashes and messages.
- Never push without explicit user authorization.

Do not perform destructive Git operations or rewrite existing commits without authorization.

If changes cannot be safely separated, stop and report the issue.

### 11. Sprint Continuity

When a sprint is interrupted:

- Inspect the current repository state.
- Review recorded sprint progress.
- Verify previously completed tasks.
- Identify incomplete or partially implemented work.
- Reassess dependencies.
- Resume from the earliest actionable task.

Do not repeat completed work unnecessarily.

Do not discard partially completed work without understanding its state.

Maintain sufficient progress information for reliable continuation.

### 12. Sprint Report

Provide:

- Sprint objective.
- Tasks completed.
- Tasks remaining.
- Tasks blocked.
- Tasks failed or deferred.
- Files modified.
- Agents involved.
- Integration results.
- Tests and verification results.
- Documentation updates.
- Git commit details.
- Unresolved issues.
- Known risks.
- Recommended next tasks.

Clearly distinguish completed work from incomplete work.

## Autonomy Boundaries

- Do not exceed approved sprint scope.
- Do not introduce new technologies without justification.
- Do not change project architecture without documenting the decision and obtaining required approval.
- Do not delete important files without authorization.
- Do not expose secrets or credentials.
- Do not push changes without explicit authorization.
- Do not perform destructive database operations without approval.
- Do not modify production infrastructure without approval.
- Do not bypass security controls.
- Stop when a blocker requires a user decision.
- Use bounded retries for failed implementations.

Autonomy applies to execution within approved boundaries, not to unrestricted decision-making.

## Completion Criteria

- Agreed sprint scope is addressed.
- All completed tasks have supporting verification evidence.
- Changes are integrated.
- Relevant verification passes or remaining failures are explicitly reported.
- Documentation is updated.
- Local commits are created where appropriate.
- Incomplete and blocked tasks are identified.
- Sprint report is provided.

Never represent incomplete work as completed.