
# Release Verification Workflow

## Purpose
Define a structured process for assessing whether a project or a significant implementation milestone is ready for release.

## Primary Skill
`release-verification`

## Supporting Skills
- `repository-audit`
- `bug-fixing`
- `feature-development`

## Responsible Agents
- Engineering Orchestrator
- QA Engineer
- Code Reviewer
- Security Engineer
- Relevant Development Engineers

## Workflow

### 1. Establish Release Context
- Read `docs/Project_Notes.md`.
- Inspect the current Git state.
- Identify the intended release scope.
- Review completed features and known issues.
- Identify the target environment.

### 2. Build Verification
- Install or verify dependencies.
- Run the project's build process.
- Confirm that the application compiles or packages successfully.
- Record build errors and warnings.

### 3. Automated Testing
- Run unit tests.
- Run integration tests.
- Run relevant end-to-end tests.
- Verify critical application workflows.
- Record test results.

### 4. Functional Verification
- Verify release acceptance criteria.
- Check important user journeys.
- Test error handling and edge cases.
- Confirm that previously working functionality remains intact.

### 5. Security Review
- Check for accidentally committed secrets.
- Review authentication and authorization behavior.
- Check input validation and error handling.
- Review dependencies for known security concerns using available tools.
- Record unresolved security risks.

### 6. Code Review
- Inspect the release diff.
- Check for incomplete implementations.
- Identify duplicated or unnecessary code.
- Confirm that documentation matches implementation.
- Report issues that should block release.

### 7. Documentation and Release Notes
- Update `docs/Project_Notes.md`.
- Document completed functionality.
- Record known limitations.
- Prepare release notes.
- Record relevant version and commit information.

### 8. Release Decision

Classify the result as:

- **Ready:** Required verification passes and no release-blocking issues remain.
- **Ready with limitations:** Release can proceed with explicitly documented non-blocking limitations.
- **Not ready:** Important tests fail or release-blocking issues remain.

The Engineering Orchestrator must explain the reason for the classification.

### 9. Git Operations
- Review the final Git diff.
- Stage only release-related changes.
- Create a local commit after successful verification.
- Do not create tags or publish releases unless authorized.
- Do not push without explicit user authorization.

### 10. Release Report

Provide:
- Release scope.
- Build results.
- Test results.
- Functional verification results.
- Security review findings.
- Known limitations.
- Release readiness classification.
- Git commit details.
- Recommended next steps.

## Completion Criteria
- Build verification is complete.
- Required tests have been executed.
- Critical functionality has been checked.
- Security and code reviews are complete.
- Documentation is updated.
- Release readiness is clearly classified.
- Local Git state is reviewed.
- Final release report is provided.
