
---
name: release-verification
description: Performs comprehensive pre-release verification of software projects, including build checks, testing, security review, database validation, documentation review and release readiness assessment. Use before preparing or approving a software release.
---

# Release Verification

## Objective

Determine whether a software project or development milestone is ready for release based on actual verification evidence.

This skill performs verification and assessment, not automatic production deployment.

## 1. Understand Release Scope

Before verification:

- Read AGENTS.md.
- Read docs/Project_Notes.md.
- Understand the release objectives.
- Identify included features.
- Review completed development tasks.
- Identify known issues.
- Inspect the current Git state.

Understand what is intended to be released.

## 2. Repository and Git Review

Inspect:

- Current branch.
- Working tree status.
- Recent commits.
- Uncommitted changes.
- Release-related changes.

Check for:

- Accidental files.
- Debug code.
- Temporary files.
- Secrets or credentials.
- Unrelated modifications.

Never discard user changes.

Do not automatically push or publish the release.

## 3. Build Verification

Run the appropriate build process.

Check:

- Dependency installation state.
- Build configuration.
- Compilation.
- Type checking.
- Linting.
- Production build output.

Record actual results.

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

Compare implementation against acceptance criteria.

## 5. Automated Testing

Execute relevant:

- Unit tests.
- Integration tests.
- API tests.
- Database tests.
- End-to-end tests.
- Regression tests.

Identify failed, skipped and unavailable tests.

Never fabricate results or bypass failures to obtain a passing status.

## 6. Frontend Verification

When applicable:

- Verify responsive layouts.
- Inspect important interactions.
- Check loading and error states.
- Check navigation.
- Inspect browser console errors.
- Verify accessibility fundamentals.
- Check for broken visual elements.

Use browser automation when available.

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

Never perform destructive production database tests.

## 8. Security Review

Request review from security-engineer when appropriate.

Inspect:

- Authentication.
- Authorization.
- Input validation.
- Secret management.
- Sensitive data handling.
- Dependency risks.
- API security.
- Database permissions.

Record unresolved security findings.

Do not claim the application is completely secure.

## 9. Code Review

Request code-reviewer to inspect release-related changes.

Evaluate:

- Correctness.
- Maintainability.
- Architecture consistency.
- Error handling.
- Performance concerns.
- Testing quality.
- Unresolved defects.

Resolve blocking findings before recommending release.

## 10. Documentation Review

Check that documentation reflects the actual release.

Review:

- README.md.
- docs/Project_Notes.md.
- System architecture.
- API documentation.
- Database documentation.
- Setup instructions.
- Environment configuration.
- Known limitations.

Do not include secrets in documentation.

## 11. Release Readiness Assessment

Classify the result as:

READY:
Required verification has passed and no unresolved blocking issues remain.

READY WITH WARNINGS:
The release can be considered with explicitly documented non-blocking issues.

NOT READY:
Important verification failures, unresolved blocking defects or critical risks remain.

Do not hide failed checks behind a positive overall status.

## 12. Release Report

Produce a structured report containing:

1. Release scope.
2. Build results.
3. Test results.
4. Functional verification.
5. Frontend verification.
6. Backend verification.
7. Database verification.
8. Security findings.
9. Code review findings.
10. Documentation status.
11. Known limitations.
12. Release readiness assessment.
13. Recommended next actions.

## 13. Release Boundaries

- Do not automatically deploy to production.
- Do not automatically publish releases.
- Do not automatically push to GitHub.
- Do not modify production infrastructure.
- Do not perform destructive operations.
- Request explicit authorization for privileged release operations.

## Completion Criteria

Release verification is complete when all applicable checks have been executed, results have been documented and a clear readiness assessment has been produced.
