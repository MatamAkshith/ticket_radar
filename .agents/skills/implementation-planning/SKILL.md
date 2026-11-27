---
name: implementation-planning
description: Converts software requirements and approved architecture into actionable development plans, task breakdowns, dependencies, milestones and acceptance criteria. Use before implementing features, starting development or organizing an autonomous engineering sprint.
---

# Implementation Planning Skill

## Objective

Transform approved requirements and architecture into a structured, executable development plan.

The plan should allow an AI orchestrator or development team to implement the project in manageable stages, with clear dependencies, ownership and verification gates.

## 1. Review Project Context

Before planning:

- Read `docs/Project_Notes.md`.
- Review project requirements.
- Review the approved architecture.
- Inspect the existing repository when applicable.
- Identify implemented functionality.
- Identify incomplete functionality.
- Review existing tests and verification scripts.
- Review technical constraints and dependencies.
- Identify unresolved architectural decisions and external integration uncertainties.

Do not plan work that has already been completed unless changes are required.

Distinguish existing implementation from planned functionality.

## 2. Define Development Phases

Divide the project into logical phases.

Typical phases may include:

1. Project foundation and configuration.
2. Database and backend foundation.
3. Authentication and authorization.
4. Core application functionality.
5. Frontend implementation.
6. Integrations and external services.
7. Testing and quality assurance.
8. Deployment preparation.

Adapt phases to the actual project.

For Ticket Radar, consider a progression such as:

1. Project setup and technical validation.
2. Backend and database foundation.
3. Monitoring configuration and execution engine.
4. Platform adapter implementation.
5. Availability normalization and change detection.
6. Notification system.
7. Dashboard and frontend integration.
8. End-to-end verification and deployment preparation.

Do not force this sequence if validated architecture or dependencies require a different order.

## 3. Break Phases into Tasks

Each task should contain:

- Task ID.
- Task name.
- Objective.
- Description.
- Relevant modules or files.
- Dependencies.
- Priority.
- Acceptance criteria.
- Verification requirements.
- Estimated complexity when useful.

Keep tasks small enough to implement and verify independently.

Avoid tasks that combine unrelated features or modify too many shared components.

## 4. Define Dependencies

Identify:

- Tasks that can run independently.
- Tasks that require previous implementation.
- Shared components.
- API dependencies.
- Database dependencies.
- Integration dependencies.
- Testing dependencies.

Establish implementation order.

Do not parallelize tasks that depend on unfinished work.

Define clear interfaces and contracts before delegating tasks that interact with one another.

## 5. Define Acceptance Criteria

Every meaningful feature should have clear acceptance criteria.

Criteria should describe observable results.

Examples:

- An authenticated user can update their own profile.
- Invalid input is rejected with an appropriate error.
- Unauthorized users cannot access protected resources.
- Data remains available after application restart.
- Duplicate events are not generated for unchanged observations.
- Failed monitoring runs do not generate false availability notifications.
- A notification delivery failure is recorded and handled appropriately.

Avoid vague criteria such as "feature works correctly."

Acceptance criteria must be testable and aligned with the actual requirements.

## 6. Plan Testing

Identify verification requirements for each task:

- Unit tests.
- Integration tests.
- API tests.
- Database tests.
- UI tests.
- Browser tests.
- Security checks.
- Build verification.
- Regression tests.
- End-to-end tests.

Select checks appropriate to the feature.

For Ticket Radar:

- Test platform adapters independently using controlled fixtures or mocks.
- Test availability normalization.
- Test change detection and duplicate prevention.
- Test stale observations and monitoring failures.
- Test notification delivery and retry behavior.
- Avoid aggressive or unauthorized live platform testing.

Do not treat successful mock tests as proof that an external platform integration works in production.

## 7. Plan Delegation

When specialist agents are available:

- Identify independent tasks.
- Assign clear responsibilities.
- Define file ownership where necessary.
- Define expected inputs and outputs.
- Specify dependencies.
- Provide relevant architecture and API contracts.
- Avoid conflicting modifications.
- Reserve integration and final verification for the orchestrator.

Use parallel execution only when it provides a genuine benefit.

The orchestrator must coordinate shared interfaces and resolve integration conflicts.

Do not delegate implementation before the required design decisions and dependencies are sufficiently clear.

## 8. Define Milestones

Group related tasks into meaningful milestones.

Each milestone should have:

- A clear objective.
- A list of included tasks.
- Dependencies.
- Completion criteria.
- Verification requirements.
- Known risks or blockers.

Milestones should represent useful, verifiable development progress.

A milestone must not be marked complete merely because its implementation tasks were attempted.

## 9. Prepare the Development Plan

Produce a structured plan containing:

1. Project objectives.
2. Current implementation baseline.
3. Development phases.
4. Task breakdown.
5. Task dependencies.
6. Priorities.
7. Acceptance criteria.
8. Testing strategy.
9. Delegation opportunities.
10. Milestones.
11. Risks and blockers.
12. Verification gates.

Clearly distinguish proposed work from completed work.

## 10. Update Project Documentation

When planning a Foundation-based project:

- Update `docs/Project_Notes.md` when authorized.
- Add planned milestones.
- Update pending work.
- Record important dependencies.
- Keep completed and planned work separate.
- Record significant planning decisions.
- Never mark planned functionality as completed.
- Preserve historical development entries.

## 11. Execution Readiness

Before implementation begins, ensure:

- Requirements are sufficiently clear.
- Architecture is approved.
- Tasks are actionable.
- Dependencies are understood.
- Acceptance criteria exist.
- Verification requirements are defined.
- Required tools and resources are available.
- Important risks are documented.
- External integrations have a feasible and permitted implementation approach.

If important information is missing, identify it before execution.

Do not silently turn an unresolved technical assumption into an implementation commitment.

## 12. Execution Control

During implementation:

- Follow the approved task dependencies.
- Track task and milestone status.
- Verify completed tasks before marking them complete.
- Reassess the plan when implementation reveals new constraints.
- Update affected tasks and documentation.
- Avoid expanding scope without justification.
- Escalate blockers that require user decisions.

Changes to the plan must preserve completed work and explain why the original plan changed.

## Completion Criteria

Implementation planning is complete when:

- Development phases are defined.
- The current implementation baseline is understood.
- Tasks are actionable.
- Dependencies are mapped.
- Acceptance criteria are established.
- Verification requirements are identified.
- Delegation opportunities are understood.
- Milestones and verification gates are defined.
- Risks and blockers are documented.
- The plan is ready for execution.