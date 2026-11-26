
# Autonomous Sprint Workflow

## Purpose
Define how the Engineering Orchestrator coordinates a bounded development sprint, delegates tasks to specialist agents, verifies results, and maintains project documentation.

## Primary Skill
`autonomous-sprint`

## Supporting Skills
- `repository-audit`
- `implementation-planning`
- `feature-development`
- `bug-fixing`
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

### 1. Establish Sprint Context
- Read `docs/Project_Notes.md`.
- Inspect the current repository state.
- Review existing architecture and technology stack.
- Identify current project status and known issues.
- Understand the sprint objective and boundaries.

### 2. Define Sprint Scope
- Identify the highest-priority tasks.
- Break work into small, independently verifiable tasks.
- Define expected outcomes.
- Identify dependencies and risks.
- Avoid expanding scope without user authorization.

### 3. Plan and Delegate
- Assign tasks to appropriate specialist agents.
- Establish clear responsibilities.
- Identify files and modules likely to be affected.
- Define verification criteria for each task.
- Coordinate dependencies between agents.

### 4. Execute Development
- Implement tasks in a controlled sequence.
- Follow project architecture and engineering rules.
- Preserve existing user changes.
- Avoid unnecessary refactoring.
- Report blockers instead of making risky assumptions.

### 5. Integrate Changes
- Review specialist outputs.
- Integrate completed work.
- Resolve integration conflicts.
- Verify compatibility between components.

### 6. Quality Assurance
- Run relevant tests.
- Check integration behavior.
- Review error handling and edge cases.
- Perform security checks where relevant.
- Verify sprint acceptance criteria.

### 7. Documentation
- Update relevant technical documentation.
- Update `docs/Project_Notes.md`.
- Record completed tasks and remaining work.
- Record important decisions and limitations.

### 8. Git Operations
- Inspect the complete Git diff.
- Stage only sprint-related changes.
- Create local commits after successful verification.
- Do not push without explicit user authorization.

### 9. Sprint Report
Provide:
- Sprint objective.
- Tasks completed.
- Files modified.
- Agents involved.
- Tests and verification results.
- Git commit details.
- Unresolved issues.
- Recommended next tasks.

## Autonomy Boundaries
- Do not introduce new technologies without justification.
- Do not change project architecture without documenting the decision.
- Do not delete important files without authorization.
- Do not expose secrets or credentials.
- Do not push changes without explicit authorization.
- Stop when a blocker requires a user decision.

## Completion Criteria
- Agreed sprint scope is addressed.
- Changes are integrated.
- Relevant verification passes.
- Documentation is updated.
- Local commits are created where appropriate.
- Sprint report is provided.
