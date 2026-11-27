---
name: new-project-development
description: Coordinates the development of a new software project from a validated idea through requirements, architecture, implementation, testing and verified completion. Use when starting a completely new software project.
---

# New Project Development

## Objective

Coordinate the development of a new software project using Foundation's engineering standards, skills and specialist agents.

The workflow must move from a validated idea to a working, tested and documented MVP through controlled and verifiable stages.

The engineering orchestrator is responsible for coordinating the complete lifecycle.

## 1. Discovery

Invoke `project-discovery`.

Responsibilities:

- Understand the problem and target users.
- Identify functional and non-functional requirements.
- Define the MVP.
- Identify constraints, assumptions and risks.
- Investigate external dependencies.
- Clarify important uncertainties.
- Establish measurable acceptance criteria.

Do not begin implementation while critical requirements remain unresolved.

Clearly distinguish confirmed requirements from assumptions and unverified capabilities.

## 2. Architecture

Invoke `architecture-design`.

Responsibilities:

- Select an appropriate technology stack.
- Define system components and responsibilities.
- Design database architecture where applicable.
- Define API contracts where applicable.
- Identify external integrations.
- Define important data flows.
- Evaluate security and reliability.
- Document significant architectural decisions and trade-offs.

Validate the feasibility of important external integrations before committing to their implementation.

Do not introduce unnecessary complexity or infrastructure.

Obtain approval for major architectural decisions when they materially affect cost, security, scope or project direction.

## 3. Implementation Planning

Invoke `implementation-planning`.

Responsibilities:

- Divide development into phases and milestones.
- Create actionable development tasks.
- Define task dependencies.
- Establish acceptance criteria.
- Define verification requirements.
- Identify suitable specialist agents.
- Identify parallel execution opportunities.
- Document risks and blockers.

Ensure that the implementation plan is consistent with the approved architecture.

Do not delegate tasks with unresolved dependencies or ambiguous responsibilities.

## 4. Project Foundation

Establish the initial project environment according to the approved architecture and implementation plan.

Responsibilities:

- Establish the repository structure.
- Configure the development environment.
- Initialize dependencies.
- Configure environment variables safely.
- Establish the testing framework.
- Configure development and build scripts.
- Prepare initial documentation.
- Verify that the project can build and run.

Inspect the repository before creating or modifying files.

Preserve existing user work.

Do not introduce unnecessary dependencies or infrastructure.

Verify the project foundation before proceeding to feature implementation.

## 5. Implementation

Coordinate implementation through `engineering-orchestrator`.

Delegate to relevant specialist agents:

- `frontend-engineer`: Frontend implementation.
- `backend-engineer`: Backend services and APIs.
- `database-engineer`: Database design and implementation.
- `qa-engineer`: Test planning and verification.
- `code-reviewer`: Independent code review.
- `security-engineer`: Security assessment.

Use only the agents relevant to the project.

Implementation rules:

- Follow approved architecture and task dependencies.
- Assign clear responsibilities and file ownership.
- Define shared interfaces before parallel implementation.
- Implement in manageable, verifiable increments.
- Integrate completed components incrementally.
- Run relevant tests after integration.
- Resolve conflicts before accepting agent changes.
- Avoid unnecessary parallel execution.
- Preserve existing working functionality.

The orchestrator must review agent outputs and remain responsible for overall integration.

## 6. Verification and Quality Assurance

Invoke `qa-engineer` throughout development, not only at the end.

Responsibilities:

- Run relevant unit tests.
- Run integration tests.
- Verify API contracts.
- Verify database behavior.
- Test important user journeys.
- Perform regression testing.
- Verify build and deployment readiness where applicable.
- Report failures with reproducible evidence.

Request independent code review through `code-reviewer`.

Request security review through `security-engineer` where appropriate.

Resolve identified defects and repeat relevant verification.

Do not mark functionality complete merely because implementation was generated.

## 7. Iterative Correction

When verification or integration fails:

1. Identify the failure.
2. Collect relevant logs and evidence.
3. Determine the responsible component.
4. Assign a focused correction task.
5. Implement the correction.
6. Rerun the failed verification.
7. Run relevant regression checks.
8. Update documentation and task status.

Use bounded correction attempts.

If a failure cannot be resolved safely, report the blocker rather than repeatedly making speculative changes.

Never conceal failed tests or weaken verification criteria merely to obtain a passing result.

## 8. Documentation

Maintain `docs/Project_Notes.md` as the persistent project context.

Record:

- Project overview.
- Confirmed requirements.
- Technology stack.
- System architecture.
- Project workflow.
- Database and API design.
- Technical decisions.
- Development progress.
- Verification results.
- Known limitations.
- Pending work.

Update documentation as meaningful changes occur.

Preserve historical development entries.

Ensure documentation reflects the actual implementation rather than planned or assumed functionality.

## 9. Git and Version Control

Follow the repository's Git and Documentation Standards.

- Inspect Git status before modifications.
- Preserve unrelated user changes.
- Stage only task-related files.
- Run relevant verification before committing.
- Create meaningful local commits after successful development milestones.
- Report commit hashes and messages.
- Never automatically push to a remote repository.
- Never perform destructive Git operations without appropriate authorization.

## 10. Milestone Management

Track progress across all development milestones.

For each milestone, maintain:

- Objective.
- Included tasks.
- Dependencies.
- Current status.
- Verification results.
- Outstanding issues.

Use clear statuses such as:

- Not started.
- In progress.
- Blocked.
- Verification pending.
- Completed.

A milestone is complete only when its acceptance criteria and required verification have passed.

## 11. Completion and Handoff

Before reporting the initial project as complete:

- Verify the agreed MVP scope.
- Confirm required features are implemented.
- Confirm relevant tests and builds pass.
- Complete appropriate code and security reviews.
- Update project documentation.
- Review the Git diff.
- Create the appropriate local commit.
- Record known limitations and remaining work.

Provide a final report containing:

1. Project summary.
2. Implemented functionality.
3. Architecture and technology stack.
4. Completed milestones.
5. Verification results.
6. Git commit information.
7. Known limitations.
8. Remaining tasks.

Do not describe the entire product as complete when only the MVP has been delivered.

## Completion Criteria

The initial project is ready when:

- Discovery and requirements are documented.
- Architecture is approved.
- The implementation plan is actionable.
- The project foundation is verified.
- The agreed MVP has been implemented.
- Relevant verification has been performed.
- Documentation is current.
- Git changes are appropriately committed.
- Development status and remaining limitations are accurately reported.