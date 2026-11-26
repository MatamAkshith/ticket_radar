
---
name: autonomous-sprint
description: Executes a bounded collection of approved software development tasks autonomously. Handles task selection, planning, specialist delegation, implementation, testing, documentation, local commits and progress reporting. Use when running an autonomous development sprint or completing multiple approved tasks.
---

# Autonomous Sprint

## Objective

Execute a predefined collection of development tasks with minimal user intervention while maintaining engineering quality, security and controlled autonomy.

Autonomous execution does not mean unrestricted access.

## 1. Establish Sprint Context

Before execution:

- Read AGENTS.md.
- Read docs/Project_Notes.md.
- Inspect repository structure.
- Review current Git status.
- Understand the project architecture.
- Review the development roadmap.
- Identify completed and pending tasks.
- Identify available resources and tools.

## 2. Define Sprint Scope

Establish:

- Sprint objective.
- Approved tasks.
- Task priorities.
- Dependencies.
- Acceptance criteria.
- Verification requirements.
- Expected deliverables.

Only execute tasks within the approved scope.

Do not invent additional major features.

## 3. Task Selection

Classify tasks as:

- Ready: Requirements and dependencies are satisfied.
- Blocked: Missing dependencies or information.
- In Progress: Currently being implemented.
- Completed: Successfully implemented and verified.

Prioritize ready tasks according to importance and dependencies.

Do not start blocked tasks.

## 4. Execution Planning

- Break tasks into manageable units.
- Identify independent tasks.
- Identify tasks requiring sequential execution.
- Estimate complexity when useful.
- Identify suitable specialist agents.
- Define expected outcomes.

Use parallel execution only when tasks are sufficiently independent.

## 5. Specialist Delegation

Use relevant agents:

- Frontend Engineer.
- Backend Engineer.
- Database Engineer.
- QA Engineer.
- Code Reviewer.
- Security Engineer.

The Engineering Orchestrator remains responsible for coordination and integration.

Avoid conflicting file ownership.

## 6. Implementation

For each task:

1. Understand the requirement.
2. Inspect relevant code.
3. Define acceptance criteria.
4. Implement the change.
5. Run targeted tests.
6. Review the implementation.
7. Resolve identified defects.
8. Update relevant documentation.
9. Create an appropriate local Git commit after successful verification.
10. Update task status.

Do not move a task to Completed without evidence.

## 7. Automated Verification

Perform appropriate checks:

- Unit tests.
- Integration tests.
- Build verification.
- API verification.
- Database verification.
- Browser testing.
- Regression testing.
- Security checks.

Select tests according to the actual technology stack.

Do not claim tests passed if they were not executed.

## 8. Documentation Maintenance

Maintain docs/Project_Notes.md.

Update:

- Current development phase.
- Sprint progress.
- Completed tasks.
- Pending tasks.
- Architecture changes.
- Technical decisions.
- Development log.
- Verification results.

Preserve historical entries.

## 9. Automated Local Git Management

Follow .agents/rules/06-git-documentation.md.

- Create meaningful local commits after verified tasks.
- Stage only changes belonging to the task.
- Preserve unrelated user changes.
- Never commit secrets.
- Never commit known failing implementations.
- Report commit hashes.
- Never automatically push to GitHub.

If changes cannot be safely separated, stop and report the issue.

## 10. Bounded Autonomy

Respect the following boundaries:

- Do not exceed the approved sprint scope.
- Do not perform destructive database operations without approval.
- Do not modify production infrastructure without approval.
- Do not expose credentials.
- Do not force-push.
- Do not bypass security controls.
- Do not continue indefinitely when blocked.

Use a bounded retry policy for failed implementations.

## 11. Stop Conditions

Pause execution when:

- Critical requirements are unclear.
- Necessary credentials are unavailable.
- A task requires unauthorized privileges.
- A destructive operation is necessary.
- Repeated implementation attempts fail.
- Verification cannot be completed.
- The sprint scope is exhausted.

Do not silently skip blockers.

## 12. Final Sprint Report

Provide:

- Sprint objective.
- Tasks completed.
- Tasks remaining.
- Tasks blocked.
- Files changed.
- Agents involved.
- Tests executed and results.
- Documentation updates.
- Local commit hashes.
- Known defects.
- Outstanding risks.
- Recommended next sprint.

## Completion Criteria

A sprint is complete when all approved tasks are either verified and committed or explicitly reported as incomplete or blocked.

Never represent incomplete work as completed.
