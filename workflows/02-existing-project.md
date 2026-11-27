# Workflow 02 — Existing Project Onboarding

## Objective

Understand an existing repository and establish reliable project context before development begins.

The onboarding process is inspection-first and must preserve existing implementation, documentation and user modifications.

The Engineering Orchestrator coordinates the process and remains responsible for the final assessment.

## Participants

- Engineering Orchestrator
- Database Engineer, when required
- Frontend Engineer, when required
- Backend Engineer, when required
- QA Engineer, when required
- Code Reviewer, when required
- Security Engineer, when required

## Process

### Phase 1 — Repository Inspection

Invoke the Repository Audit skill.

- Inspect repository structure.
- Identify technology stack.
- Inspect dependencies.
- Identify application entry points.
- Inspect configuration.
- Identify existing engineering standards and agent configurations.
- Review Git status.
- Identify staged, unstaged and untracked changes.

Do not modify application code during the initial audit.

Preserve all existing user modifications.

### Phase 2 — Architecture Understanding

- Identify frontend and backend components.
- Understand API communication.
- Inspect database architecture.
- Identify authentication and authorization mechanisms.
- Understand external integrations.
- Review background processes.
- Review deployment configuration.
- Map important component relationships.

Base findings on actual repository evidence.

Distinguish implemented architecture from documented or proposed architecture.

### Phase 3 — Implementation Assessment

Identify:

- Completed features.
- Partially completed features.
- Missing functionality.
- Known defects.
- Existing tests.
- Technical debt.
- Current build status.
- Security concerns.
- Incomplete integrations.
- Documentation mismatches.

Compare actual implementation against existing requirements and documentation.

Do not treat planned functionality as completed.

### Phase 4 — Establish Project Context

- Read existing project documentation.
- Locate `docs/Project_Notes.md`.
- If it exists, compare it with the actual implementation.
- If missing, prepare it using the Foundation Project Notes template.
- Populate it only with verified repository information.
- Mark unknown information rather than inventing it.
- Preserve historical development entries.
- Record significant architectural decisions and unresolved questions.

Do not silently replace existing architectural decisions or documentation.

Creating or modifying project documentation must follow the repository's documentation and Git standards.

### Phase 5 — Baseline Verification

Run appropriate existing checks when safe and practical:

- Build.
- Tests.
- Linting.
- Type checking.
- Configuration validation.
- Static analysis where available.

Before running commands, inspect potential side effects.

Do not execute destructive database operations or modify production infrastructure.

Record actual results using clear statuses:

- Passed.
- Failed.
- Not run.
- Blocked.
- Not applicable.

Do not claim successful verification without evidence.

Do not fix unrelated defects during onboarding.

### Phase 6 — Development Readiness

- Identify technical risks.
- Identify outstanding work.
- Identify blockers and dependencies.
- Prioritize next tasks.
- Evaluate Foundation compatibility.
- Recommend the next development milestone.
- Identify decisions requiring user input.

Avoid proposing a complete rewrite when incremental improvements are sufficient.

### Phase 7 — Documentation and Reporting

Update project context with verified findings when authorized.

Ensure `docs/Project_Notes.md` reflects:

- Project overview.
- Actual technology stack.
- Existing architecture.
- Implemented functionality.
- Testing and build status.
- Technical risks.
- Outstanding work.
- Recommended next milestone.

Preserve existing architectural decisions and historical information.

Provide an onboarding report containing:

1. Repository overview.
2. Technology stack.
3. Architecture summary.
4. Existing functionality.
5. Testing and build status.
6. Git working state.
7. Documentation status.
8. Identified risks and blockers.
9. Recommended next milestone.

### Phase 8 — Git and Handoff

Follow Foundation's Git and Documentation Standards.

- Preserve the original working tree and user modifications.
- Review any documentation changes.
- Do not stage unrelated files.
- Do not automatically push changes.
- Do not create commits unless they are part of the authorized onboarding task.

Present the findings to the user and Engineering Orchestrator.

Onboarding completion does not automatically authorize application development.

## Completion Criteria

The repository is understood, existing architecture and implementation are assessed, project context is established, baseline verification is documented and the next development milestone is identified.

Existing user work is preserved.

No application implementation changes are required during onboarding.