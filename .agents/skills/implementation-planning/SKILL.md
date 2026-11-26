
---
name: implementation-planning
description: Converts software requirements and approved architecture into actionable development plans, task breakdowns, dependencies, milestones and acceptance criteria. Use before implementing features, starting development or organizing an autonomous engineering sprint.
---

# Implementation Planning Skill

## Objective

Transform approved requirements and architecture into a structured, executable development plan.

The plan should allow an AI orchestrator or development team to implement the project in manageable stages.

## 1. Review Project Context

Before planning:

- Read docs/Project_Notes.md.
- Review project requirements.
- Review the approved architecture.
- Inspect the existing repository when applicable.
- Identify implemented functionality.
- Identify incomplete functionality.
- Review technical constraints and dependencies.

Do not plan work that has already been completed unless changes are required.

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

## 4. Define Dependencies

Identify:

- Tasks that can run independently.
- Tasks that require previous implementation.
- Shared components.
- API dependencies.
- Database dependencies.
- Integration dependencies.

Establish implementation order.

Do not parallelize tasks that depend on unfinished work.

## 5. Define Acceptance Criteria

Every meaningful feature should have clear acceptance criteria.

Criteria should describe observable results.

Examples:

- An authenticated user can update their own profile.
- Invalid input is rejected with an appropriate error.
- Unauthorized users cannot access protected resources.
- Data remains available after application restart.

Avoid vague criteria such as "feature works correctly."

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

Select checks appropriate to the feature.

## 7. Plan Delegation

When specialist agents are available:

- Identify independent tasks.
- Assign clear responsibilities.
- Define file ownership where necessary.
- Define expected inputs and outputs.
- Specify dependencies.
- Avoid conflicting modifications.
- Reserve integration and final verification for the orchestrator.

Use parallel execution only when it provides a genuine benefit.

## 8. Define Milestones

Group related tasks into meaningful milestones.

Each milestone should have:

- A clear objective.
- A list of included tasks.
- Dependencies.
- Completion criteria.
- Verification requirements.

Milestones should represent useful, verifiable development progress.

## 9. Prepare the Development Plan

Produce a structured plan containing:

1. Project objectives.
2. Development phases.
3. Task breakdown.
4. Task dependencies.
5. Priorities.
6. Acceptance criteria.
7. Testing strategy.
8. Delegation opportunities.
9. Milestones.
10. Risks and blockers.

## 10. Update Project Documentation

When planning a Foundation-based project:

- Update docs/Project_Notes.md when authorized.
- Add planned milestones.
- Update pending work.
- Record important dependencies.
- Keep completed and planned work separate.
- Never mark planned functionality as completed.

## 11. Execution Readiness

Before implementation begins, ensure:

- Requirements are sufficiently clear.
- Architecture is approved.
- Tasks are actionable.
- Dependencies are understood.
- Acceptance criteria exist.
- Required tools and resources are available.
- Important risks are documented.

If important information is missing, identify it before execution.

## Completion Criteria

Implementation planning is complete when:

- Development phases are defined.
- Tasks are actionable.
- Dependencies are mapped.
- Acceptance criteria are established.
- Verification requirements are identified.
- Delegation opportunities are understood.
- Milestones are defined.
- The plan is ready for execution.
