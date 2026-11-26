
# Workflow 02 — Existing Project Onboarding

## Objective

Understand an existing repository and establish reliable project context before development begins.

## Participants

- Engineering Orchestrator
- Database Engineer, when required
- Frontend Engineer, when required
- Backend Engineer, when required
- QA Engineer

## Process

### Phase 1 — Repository Inspection

Invoke Repository Audit.

- Inspect repository structure.
- Identify technology stack.
- Inspect dependencies.
- Identify application entry points.
- Inspect configuration.
- Review Git status.

Do not modify application code during the initial audit.

### Phase 2 — Architecture Understanding

- Identify frontend and backend components.
- Understand API communication.
- Inspect database architecture.
- Identify authentication mechanisms.
- Understand external integrations.
- Review deployment configuration.

### Phase 3 — Implementation Assessment

Identify:

- Completed features.
- Partially completed features.
- Missing functionality.
- Known defects.
- Existing tests.
- Technical debt.
- Current build status.

### Phase 4 — Establish Project Context

- Read existing project documentation.
- Locate docs/Project_Notes.md.
- Create it from the Foundation template if missing.
- Compare documentation with actual implementation.
- Record verified architecture and technology details.
- Mark unknown information rather than inventing it.

### Phase 5 — Baseline Verification

Run appropriate existing checks:

- Build.
- Tests.
- Linting.
- Type checking.
- Configuration validation.

Record actual results.

### Phase 6 — Development Readiness

- Identify technical risks.
- Identify outstanding work.
- Prioritize next tasks.
- Establish the next milestone.
- Present the audit findings.

### Phase 7 — Documentation

Update project context with verified findings.

Do not silently replace existing architectural decisions.

## Completion Criteria

The repository is understood, project context is established, baseline verification is documented and the next development milestone is identified.

No application implementation changes are required during onboarding.
