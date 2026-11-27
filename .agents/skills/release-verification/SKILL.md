---
name: release-verification
description: Performs comprehensive pre-release verification of software projects, including build checks, testing, security review, database validation, documentation review and release readiness assessment. Use before preparing or approving a software release.
---

# Release Verification

## Objective

Determine whether a software project or development milestone is ready for release based on actual verification evidence.

This skill performs verification and assessment, not automatic production deployment.

The Engineering Orchestrator is responsible for coordinating verification and producing the final release recommendation.

## 1. Understand Release Scope

Before verification:

- Read `AGENTS.md`.
- Read `docs/Project_Notes.md`.
- Understand the release objectives.
- Identify included features.
- Review completed development tasks.
- Identify known issues.
- Review relevant acceptance criteria.
- Inspect the current Git state.

Understand exactly what is intended to be released.

Distinguish implemented functionality from planned functionality.

## 2. Repository and Git Review

Inspect:

- Current branch.
- Working tree status.
- Recent commits.
- Staged and unstaged changes.
- Untracked files.
- Release-related changes.

Check for:

- Accidental files.
- Debug code.
- Temporary files.
- Secrets or credentials.
- Unrelated modifications.
- Uncommitted changes.
- Missing documentation.

Never discard user changes.

Do not automatically push or publish the release.

Verify that the code being assessed corresponds to the intended release commit.

Record the commit identifier used for verification.

If the working tree contains relevant uncommitted changes, clearly report that the tested state may differ from the committed release state.

## 3. Build Verification

Run the appropriate build process.

Check:

- Dependency installation state.
- Build configuration.
- Compilation.
- Type checking.
- Linting.
- Production build output.
- Configuration consistency.

Record actual results.

Distinguish successful builds from checks that were not executed or could not be completed.

## 4. Functional Testing

Verify:

- Core application functionality.
- Important user journeys.
- Authentication.
- Authorization.
- Data persistence.
- API integrations.
- Error handling.
- Edge cases.
- Acceptance criteria.

Compare implementation against the approved requirements.

Do not treat the presence of an interface or endpoint as proof that the underlying functionality works.

## 5. Automated Testing

Execute relevant:

- Unit tests.
- Integration tests.
- API tests.
- Database tests.
- End-to-end tests.
- Regression tests.

Identify:

- Passed tests.
- Failed tests.
- Skipped tests.
- Unavailable tests.
- Blocked tests.

Never fabricate results or bypass failures to obtain a passing status.

Investigate failures and determine whether they are release-blocking.

## 6. Frontend Verification

When applicable:

- Verify responsive layouts.
- Inspect important interactions.
- Check loading and error states.
- Check navigation.
- Inspect browser console errors.
- Verify accessibility fundamentals.
- Check for broken visual elements.
- Verify frontend and backend integration.

Use browser automation when available and appropriate.

## 7. Backend and Database Verification

When applicable:

- Verify important API endpoints.
- Check authentication and authorization.
- Validate request handling.
- Verify database constraints.
- Review migrations.
- Check important data relationships.
- Verify transaction behavior.
- Review access policies.
- Check error handling and logging.

Never perform destructive production database tests.

Verify that database migrations and application versions are compatible.

## 8. External Integration Verification

For applications depending on external platforms or services:

- Verify integration configuration.
- Check permitted access methods.
- Validate response handling.
- Test timeout and failure behavior.
- Verify retry behavior.
- Check rate-limit handling.
- Identify external service dependencies.
- Document limitations and unsupported capabilities.

Do not claim an external integration works based only on mocked tests.

Do not bypass platform access restrictions or anti-bot protections.

## 9. Ticket Radar-Specific Verification

When verifying Ticket Radar, additionally check:

- Movie and cinema monitoring configuration.
- BookMyShow and PVR/INOX adapter behavior where implemented.
- Booking-release detection.
- Showtime and screening-format normalization.
- Seat availability handling where permitted and supported.
- Availability observation timestamps.
- Stale observation handling.
- Distinction between available, unavailable, unknown and failed states.
- Availability change detection.
- Duplicate event prevention.
- Telegram notification delivery.
- Notification failure and retry handling.
- Monitoring execution history.
- Recovery after monitoring failures.

A failed or incomplete monitoring run must never be presented as confirmed unavailability or availability.

Do not claim real-time monitoring reliability without appropriate evidence.

## 10. Security Review

Request review from `security-engineer` when appropriate.

Inspect:

- Authentication.
- Authorization.
- Input validation.
- Secret management.
- Sensitive data handling.
- Dependency risks.
- API security.
- Database permissions.
- External integration security.
- Logging and information exposure.

Record unresolved security findings.

Do not claim the application is completely secure.

## 11. Code Review

Request `code-reviewer` to inspect release-related changes.

Evaluate:

- Correctness.
- Maintainability.
- Architecture consistency.
- Error handling.
- Performance concerns.
- Testing quality.
- Unresolved defects.
- Unnecessary complexity.

Resolve blocking findings before recommending release.

## 12. Documentation Review

Check that documentation reflects the actual release.

Review:

- `README.md`.
- `docs/Project_Notes.md`.
- System architecture.
- API documentation.
- Database documentation.
- Setup instructions.
- Environment configuration.
- Known limitations.
- Deployment instructions where applicable.

Do not include secrets in documentation.

Ensure planned features are not incorrectly described as implemented.

## 13. Release Readiness Assessment

Classify the result as:

**READY**

Required verification has passed and no unresolved blocking issues remain.

**READY WITH WARNINGS**

Required release checks have passed, but explicitly documented non-blocking issues remain.

**NOT READY**

Important verification failures, unresolved blocking defects, critical security risks or incomplete release requirements remain.

Every assessment must be supported by evidence.

Do not hide failed or unexecuted checks behind a positive overall status.

A check that was not run must never be reported as passed.

## 14. Release Report

Produce a structured report containing:

1. Release scope.
2. Verified commit identifier.
3. Repository and Git status.
4. Build results.
5. Test results.
6. Functional verification.
7. Frontend verification.
8. Backend verification.
9. Database verification.
10. External integration verification.
11. Security findings.
12. Code review findings.
13. Documentation status.
14. Known limitations.
15. Failed, skipped and unexecuted checks.
16. Release readiness assessment.
17. Recommended next actions.

Include relevant evidence and distinguish confirmed results from assumptions.

## 15. Release Boundaries

- Do not automatically deploy to production.
- Do not automatically publish releases.
- Do not automatically push to GitHub.
- Do not modify production infrastructure.
- Do not perform destructive operations.
- Do not expose credentials.
- Do not bypass security controls.
- Request explicit authorization for privileged release operations.

A READY assessment is a technical recommendation, not authorization to deploy or publish.

## Completion Criteria

Release verification is complete when:

- The release scope is understood.
- The tested code state is identified.
- All applicable checks have been executed or explicitly classified.
- Build and test results are documented.
- Functional requirements are assessed.
- Security and code reviews are considered.
- Documentation is reviewed.
- Known limitations are recorded.
- A clear evidence-based readiness assessment is produced.