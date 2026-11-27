---
name: autonomous-sprint
description: Executes a bounded collection of approved software development tasks autonomously. Handles task selection, planning, specialist delegation, implementation, testing, documentation, local commits and progress reporting. Use when running an autonomous development sprint or completing multiple approved tasks.
---

# Autonomous Sprint

## Objective

Execute a predefined collection of approved development tasks with minimal user intervention while maintaining engineering quality, security and controlled autonomy.

Autonomous execution does not mean unrestricted access.

The Engineering Orchestrator is responsible for sprint coordination, task tracking, specialist delegation, integration, verification and reporting.

## 1. Establish Sprint Context

Before execution:

- Read `AGENTS.md`.
- Read `docs/Project_Notes.md`.
- Inspect repository structure.
- Review current Git status.
- Understand the project architecture.
- Review the development roadmap.
- Identify completed and pending tasks.
- Identify available resources and tools.
- Review existing sprint records or unfinished work.

Preserve existing user modifications.

If resuming an interrupted sprint, verify the actual repository state before continuing.

Do not assume that previously reported task completion guarantees the current implementation is intact.

## 2. Define Sprint Scope

Establish:

- Sprint objective.
- Approved tasks.
- Task priorities.
- Dependencies.
- Acceptance criteria.
- Verification requirements.
- Expected deliverables.
- Sprint boundaries.
- Relevant constraints and risks.

Only execute tasks within the approved scope.

Do not invent additional major features.

If new requirements emerge, document them as proposed work rather than silently expanding the sprint.

## 3. Task Selection and Tracking

Maintain a consistent task status.

Classify tasks as:

- Ready: Requirements and dependencies are satisfied.
- Blocked: Missing dependencies or information.
- In Progress: Currently being implemented.
- Verification Pending: Implementation exists but required checks are incomplete.
- Completed: Successfully implemented and verified.
- Failed: Implementation or verification failed.
- Deferred: Intentionally postponed.

Prioritize ready tasks according to importance, dependencies and sprint objectives.

Do not start blocked tasks.

Do not mark a task completed without supporting implementation and verification evidence.

Keep task status synchronized with the actual repository state.

## 4. Execution Planning

- Break tasks into manageable units.
- Identify independent tasks.
- Identify tasks requiring sequential execution.
- Estimate complexity when useful.
- Identify suitable specialist agents.
- Define expected outcomes.
- Establish task dependencies.
- Identify shared files and interfaces.
- Define integration and verification checkpoints.

Use parallel execution only when tasks are sufficiently independent.

Avoid parallelizing work that shares critical files, database schemas or unfinished interfaces.

## 5. Specialist Delegation

Use relevant agents:

- Frontend Engineer.
- Backend Engineer.
- Database Engineer.
- QA Engineer.
- Code Reviewer.
- Security Engineer.

The Engineering Orchestrator remains responsible for coordination and integration.

For every delegated task:

- Define its objective.
- Specify relevant files and modules.
- Provide required context.
- Define expected outputs.
- Identify dependencies.
- Establish file ownership where necessary.
- Specify verification requirements.

Avoid conflicting file ownership.

Review specialist outputs before integrating them.

Do not assume that delegated work is correct merely because an agent reports success.

## 6. Implementation

For each task:

1. Understand the requirement.
2. Inspect relevant code.
3. Define acceptance criteria.
4. Confirm dependencies.
5. Implement the change.
6. Run targeted tests.
7. Review the implementation.
8. Integrate changes where applicable.
9. Resolve identified defects.
10. Update relevant documentation.
11. Create an appropriate local Git commit after successful verification.
12. Update task status.

Follow approved architecture and engineering standards.

Preserve existing functionality and user modifications.

Keep implementation focused on the assigned task.

Do not move a task to Completed without evidence.

## 7. Integration and Verification

Integrate completed tasks incrementally.

Perform appropriate checks:

- Unit tests.
- Integration tests.
- Build verification.
- API verification.
- Database verification.
- Browser testing.
- Regression testing.
- Security checks.
- End-to-end testing.

Select tests according to the actual technology stack and task requirements.

Verify shared interfaces and dependencies after integration.

If integration introduces failures:

- Identify the responsible change.
- Collect relevant evidence.
- Assign a focused correction.
- Re-run failed checks.
- Perform relevant regression testing.

Do not claim tests passed if they were not executed.

Distinguish successful checks from failed, blocked and unexecuted checks.

## 8. Documentation Maintenance

Maintain `docs/Project_Notes.md`.

Update:

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

Documentation must reflect actual repository state.

Do not mark planned or unverified functionality as complete.

## 9. Automated Local Git Management

Follow `.agents/rules/06-git-documentation.md`.

- Inspect Git status before and after meaningful changes.
- Create meaningful local commits after verified tasks.
- Stage only changes belonging to the task.
- Preserve unrelated user changes.
- Never commit secrets.
- Never commit known failing implementations as completed work.
- Review the Git diff before committing.
- Report commit hashes and messages.
- Never automatically push to GitHub or another remote.

If changes cannot be safely separated, stop and report the issue.

## 10. Bounded Autonomy

Respect the following boundaries:

- Do not exceed the approved sprint scope.
- Do not perform destructive database operations without approval.
- Do not modify production infrastructure without approval.
- Do not expose credentials.
- Do not force-push.
- Do not bypass security controls.
- Do not introduce unapproved paid services or infrastructure.
- Do not make irreversible changes without appropriate authorization.
- Do not continue indefinitely when blocked.

Use a bounded retry policy for failed implementations.

Make reasonable engineering decisions within the approved scope, but escalate decisions that materially affect architecture, security, cost or product behavior.

## 11. Sprint Continuity and Recovery

When a sprint is interrupted:

1. Inspect the current repository state.
2. Review the last recorded sprint status.
3. Inspect existing commits and uncommitted changes.
4. Verify previously completed tasks.
5. Identify incomplete or partially implemented tasks.
6. Reassess dependencies.
7. Resume from the earliest actionable task.

Do not repeat completed work unnecessarily.

Do not discard partially completed work without understanding its state.

Record meaningful changes in sprint progress so execution can resume reliably.

## 12. Stop Conditions

Pause execution when:

- Critical requirements are unclear.
- Necessary credentials are unavailable.
- A task requires unauthorized privileges.
- A destructive operation is necessary.
- Repeated implementation attempts fail.
- Verification cannot be completed.
- A critical security issue is discovered.
- The sprint scope is exhausted.
- A user decision is required.

Do not silently skip blockers.

Continue with other independent ready tasks only when doing so is safe and remains within the approved scope.

## 13. Final Sprint Report

Provide:

- Sprint objective.
- Tasks completed.
- Tasks remaining.
- Tasks blocked.
- Tasks deferred or failed.
- Files changed.
- Agents involved.
- Tests executed and results.
- Integration and build results.
- Documentation updates.
- Local commit hashes.
- Known defects.
- Outstanding risks.
- Recommended next sprint.

Clearly distinguish completed work from incomplete work.

## Completion Criteria

A sprint is complete when all approved tasks are either verified and committed or explicitly reported as incomplete, failed, blocked or deferred.

The final report must accurately reflect repository state, verification evidence and remaining work.

Never represent incomplete work as completed.