
# Feature Development Workflow

## Purpose
Define a consistent process for implementing new features in an existing project while preserving its architecture, coding standards, and existing functionality.

## Primary Skill
`feature-development`

## Supporting Skills
- `repository-audit`
- `architecture-design`
- `implementation-planning`
- `release-verification`

## Responsible Agents
- Engineering Orchestrator
- Frontend Engineer
- Backend Engineer
- Database Engineer
- QA Engineer
- Code Reviewer
- Security Engineer

## Workflow

### 1. Understand the Feature
- Identify the requested functionality.
- Clarify expected behavior and acceptance criteria.
- Identify affected modules and dependencies.
- Review relevant project documentation.

### 2. Inspect the Existing System
- Read `docs/Project_Notes.md`.
- Inspect relevant source files.
- Understand existing architecture and conventions.
- Identify reusable components and services.
- Check existing tests.

### 3. Plan the Implementation
- Break the feature into manageable tasks.
- Identify frontend, backend, and database changes.
- Identify API and data model changes.
- Identify security implications.
- Define verification criteria.

### 4. Implement the Feature
- Delegate work to relevant specialist agents.
- Follow existing project conventions.
- Avoid unrelated modifications.
- Keep changes modular and maintainable.

### 5. Verify the Implementation
- Run relevant automated tests.
- Perform integration testing.
- Verify acceptance criteria.
- Check for regressions.
- Review error handling and edge cases.

### 6. Review and Document
- Perform code review.
- Review security implications.
- Update relevant documentation.
- Update `docs/Project_Notes.md`.

### 7. Git Operations
- Review the complete Git diff.
- Stage only feature-related files.
- Create a local commit after successful verification.
- Do not push without explicit user authorization.

## Completion Criteria
- Feature meets acceptance criteria.
- Relevant tests pass.
- No known regressions remain.
- Documentation is updated.
- Local Git commit is created.
- Final implementation report is provided.
