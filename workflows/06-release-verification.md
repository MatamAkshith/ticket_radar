# Workflow 06 — Release Verification

## Purpose

Define a structured process for assessing whether a project or significant implementation milestone is ready for release.

The workflow verifies build quality, functional correctness, security, documentation and release integrity.

Release verification does not automatically authorize deployment, publication or distribution.

## Primary Skill

`release-verification`

## Supporting Skills

- `repository-audit` — Inspect repository state and implementation.
- `bug-fixing` — Investigate and resolve release-blocking defects.
- `feature-development` — Address incomplete implementation when authorized.

Invoke supporting skills according to the findings.

## Responsible Agents

- Engineering Orchestrator
- QA Engineer
- Code Reviewer
- Security Engineer
- Relevant Development Engineers
- Database Engineer, when database changes are involved

## Workflow

### 1. Establish Release Context

- Read `AGENTS.md`.
- Read `docs/Project_Notes.md`.
- Inspect the current Git state.
- Identify the intended release scope.
- Identify the branch and exact commit under verification.
- Review completed features and known issues.
- Identify the target environment.
- Review release acceptance criteria.
- Identify required external services and integrations.

Preserve existing user changes.

Do not assume the repository is release-ready because previous milestones passed verification.

### 2. Build Verification

- Verify the required runtime and development environment.
- Install or verify dependencies using the project's established process.
- Run the project's build process.
- Confirm that the application compiles or packages successfully.
- Verify required configuration and environment variables without exposing secrets.
- Review build errors and warnings.
- Record the exact commands and results.

For applicable projects, verify database migration generation and execution in a safe test environment.

Do not modify production data during release verification.

### 3. Automated Testing

- Run unit tests.
- Run integration tests.
- Run relevant end-to-end tests.
- Verify critical application workflows.
- Run regression tests.
- Check test coverage where available and relevant.
- Record test results and failures.

Distinguish:

- Passed
- Failed
- Skipped
- Blocked
- Not executed

Do not represent skipped or unexecuted tests as successful.

### 4. Functional Verification

- Verify release acceptance criteria.
- Check important user journeys.
- Test error handling and edge cases.
- Confirm that previously working functionality remains intact.
- Verify frontend and backend integration.
- Verify persistence and data integrity where applicable.
- Check external integrations using safe test methods.

For Ticket Radar, where applicable, additionally verify:

- Booking-release detection.
- Showtime and screening-format collection.
- Seat availability observations.
- Availability change detection.
- Duplicate event prevention.
- Telegram notification delivery.
- Handling of stale, failed and unavailable monitoring data.

Never treat a monitoring failure or unknown result as confirmed unavailability.

Do not bypass external platform access restrictions during verification.

### 5. Database and Configuration Verification

When applicable:

- Review pending database migrations.
- Verify schema compatibility.
- Check migration execution in a safe environment.
- Verify required indexes and constraints.
- Check configuration consistency across environments.
- Verify that secrets are supplied securely.
- Review backup and recovery requirements where relevant.

Record unresolved migration, configuration or data-integrity risks.

### 6. Security Review

- Check for accidentally committed secrets.
- Review authentication and authorization behavior.
- Check input validation and error handling.
- Review dependency security using available tools.
- Inspect exposed endpoints and sensitive data handling.
- Review permissions and access boundaries.
- Check logging for accidental exposure of credentials or personal data.
- Record unresolved security risks.

Do not expose secret values in reports or logs.

### 7. Code Review

- Inspect the release diff.
- Check for incomplete implementations.
- Identify duplicated or unnecessary code.
- Review error handling and maintainability.
- Check architecture and engineering-rule compliance.
- Confirm that tests cover important changes.
- Confirm that documentation matches implementation.
- Report issues that should block release.

The Code Reviewer provides findings; the Engineering Orchestrator makes the final readiness assessment using verification evidence.

### 8. Documentation and Release Notes

- Update `docs/Project_Notes.md`.
- Document completed functionality.
- Record known limitations.
- Document relevant architecture and configuration changes.
- Prepare release notes.
- Record relevant version and commit information.
- Record verification results.

Preserve historical development records.

Ensure documentation reflects actual implementation.

### 9. Release Decision

Classify the result as:

- **Ready:** Required verification passes and no release-blocking issues remain.
- **Ready with limitations:** Required release criteria pass, but explicitly documented non-blocking limitations remain.
- **Not ready:** Important tests fail, required verification is incomplete, or release-blocking issues remain.

The Engineering Orchestrator must explain:

- The selected classification.
- Evidence supporting the decision.
- Failed, skipped or blocked checks.
- Outstanding risks and limitations.
- Any conditions that must be satisfied before release.

Missing required verification must not be silently treated as a pass.

### 10. Git Operations

Follow `.agents/rules/06-git-documentation.md`.

- Review the final Git diff.
- Confirm the branch and commit being assessed.
- Stage only release-related documentation or verification changes.
- Preserve unrelated user modifications.
- Create a local commit only when appropriate.
- Record commit hashes and messages.
- Do not create tags or publish releases unless authorized.
- Do not push without explicit user authorization.

Do not rewrite history or perform destructive Git operations without approval.

The release report must identify the exact commit that was verified.

### 11. Release Report

Provide:

- Release scope.
- Verified branch and commit.
- Build results.
- Automated test results.
- Functional verification results.
- Database and configuration findings.
- Security review findings.
- Code review findings.
- Skipped or blocked checks.
- Known limitations and risks.
- Release readiness classification.
- Git commit details.
- Recommended next steps.

Clearly distinguish verification from actual deployment or publication.

## Autonomy Boundaries

- Do not expand the release scope without authorization.
- Do not deploy or publish without explicit authorization.
- Do not push changes without explicit authorization.
- Do not create release tags without authorization.
- Do not modify production infrastructure or production data.
- Do not expose secrets or credentials.
- Do not bypass security controls.
- Do not conceal failed or incomplete verification.
- Do not weaken tests to obtain a successful result.
- Stop when a release decision depends on a user decision or unavailable authorization.

## Completion Criteria

- Release scope and commit are identified.
- Build verification is complete.
- Required tests have been executed.
- Critical functionality has been checked.
- Database and configuration checks are complete where applicable.
- Security and code reviews are complete.
- Documentation is updated.
- Release readiness is clearly classified.
- Local Git state is reviewed.
- Final release report is provided.

A readiness assessment does not itself authorize release execution.