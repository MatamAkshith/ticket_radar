# Workflow 01 — New Project Development

## Objective

Establish and develop a new software project from an initial idea to a verified MVP using Foundation's engineering standards, skills and specialist agents.

The Engineering Orchestrator coordinates the entire workflow and remains accountable for integration, verification and final reporting.

## Participants

- Engineering Orchestrator
- Frontend Engineer, when required
- Backend Engineer, when required
- Database Engineer, when required
- QA Engineer
- Code Reviewer
- Security Engineer, when required

Use only the specialists relevant to the project.

## Process

### Phase 1 — Discovery

Read and follow the Project Discovery skill.

- Understand the problem.
- Identify target users.
- Gather functional requirements.
- Gather non-functional requirements.
- Define MVP scope.
- Identify constraints and risks.
- Investigate external dependencies.
- Distinguish confirmed requirements from assumptions.
- Establish acceptance criteria.

Deliverable: Project Discovery Document.

Exit criteria: Requirements and MVP boundaries are sufficiently clear for architecture design.

### Phase 2 — Architecture

Read and follow the Architecture Design skill.

- Evaluate and select the technology stack.
- Define system architecture.
- Identify application modules.
- Design database architecture where applicable.
- Define API contracts where applicable.
- Identify external integrations.
- Evaluate security and reliability.
- Document important decisions and trade-offs.

Deliverable: Approved Architecture Documentation.

Exit criteria: Major architectural decisions are established and critical feasibility questions are addressed.

### Phase 3 — Implementation Planning

Read and follow the Implementation Planning skill.

- Define development phases.
- Break work into actionable tasks.
- Establish dependencies.
- Define acceptance criteria.
- Identify milestones.
- Define verification requirements.
- Identify delegation opportunities.
- Establish integration checkpoints.

Deliverable: Development Plan.

Exit criteria: Tasks are actionable, dependencies are understood and implementation order is established.

### Phase 4 — Project Initialization

Establish the development environment according to the approved architecture and implementation plan.

- Inspect the repository and Git state.
- Establish the required repository structure.
- Configure the development environment.
- Initialize approved dependencies.
- Configure environment variables safely.
- Establish testing infrastructure.
- Configure development and build scripts.
- Initialize project documentation.
- Verify that the project builds and runs.

Deliverable: Working Project Foundation.

Exit criteria: The development environment and initial project structure are verified.

### Phase 5 — Implementation

Coordinate implementation through the Engineering Orchestrator.

- Delegate relevant work to specialist agents.
- Assign clear task responsibilities.
- Define shared interfaces and file ownership.
- Implement incrementally.
- Integrate components.
- Maintain agreed API and database contracts.
- Verify individual tasks.
- Preserve existing functionality.
- Track implementation progress.

Use parallel execution only when tasks are sufficiently independent.

Deliverable: Implemented Features.

Exit criteria: Agreed implementation tasks are completed and ready for integration verification.

### Phase 6 — Integration and Quality Assurance

Coordinate integration and invoke the QA Engineer.

- Integrate completed components.
- Execute relevant unit and integration tests.
- Verify API and database behavior.
- Verify important user journeys.
- Run regression tests.
- Verify acceptance criteria.
- Perform code review.
- Perform security review where appropriate.
- Resolve identified defects.
- Repeat failed verification where necessary.

Do not mark unverified functionality as complete.

Deliverable: Integration and Verification Results.

Exit criteria: Required checks pass or remaining blockers and limitations are explicitly documented.

### Phase 7 — Documentation and Git

Follow Foundation's Git and Documentation Standards.

- Update `docs/Project_Notes.md`.
- Record approved architecture decisions.
- Update completed and pending tasks.
- Update the progress tracker.
- Append development log entries.
- Record actual verification results.
- Review the Git diff.
- Stage only task-related changes.
- Create appropriate verified local Git commits.
- Report commit hashes.

Never automatically push to a remote repository.

Deliverable: Updated Project Documentation and Verified Local Commits.

### Phase 8 — Final Handoff

Prepare a final project report containing:

- Project overview.
- Implemented MVP functionality.
- Technology stack and architecture.
- Completed milestones.
- Verification results.
- Documentation updates.
- Git commit information.
- Known defects and limitations.
- Remaining tasks.
- Recommended next steps.

Clearly distinguish completed functionality from planned functionality.

## Execution Control

Throughout the workflow:

- Maintain `docs/Project_Notes.md` as persistent project context.
- Track task and milestone status.
- Preserve existing user modifications.
- Respect approved project scope.
- Use bounded correction attempts.
- Pause when critical requirements or permissions are missing.
- Do not silently skip blocked tasks.
- Resume interrupted work by inspecting actual repository state.
- Require appropriate approval for consequential decisions and privileged operations.

## Completion Criteria

The agreed MVP scope is implemented, integrated and verified.

Documentation is current, appropriate local commits are created, and outstanding limitations or incomplete tasks are accurately reported.

Completion of the MVP must not be represented as completion of the entire product.