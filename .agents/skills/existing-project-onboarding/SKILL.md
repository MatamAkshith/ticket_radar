---
name: existing-project-onboarding
description: Onboards Foundation into an existing software repository by inspecting its architecture, technology stack, implementation, documentation, dependencies and development status. Use when starting work on an existing project.
---

# Existing Project Onboarding

## Objective

Understand an existing software project before making changes or introducing Foundation workflows.

Establish an accurate picture of the repository, its architecture, implementation status, engineering practices and development risks.

The initial onboarding process is inspection-first and must preserve existing project work.

## 1. Initial Inspection

Invoke `repository-audit`.

Inspect:

- Repository structure.
- Languages and frameworks.
- Dependencies and configuration.
- Application entry points.
- Important modules.
- Existing engineering rules and agent configurations.
- Build and test scripts.
- Git branch, remotes and working tree status.

Identify staged, unstaged and untracked changes.

Do not modify application code during the initial audit.

Preserve existing user modifications.

Do not assume the repository is clean or that its documentation is accurate.

## 2. Understand Existing Architecture

Identify:

- Frontend architecture.
- Backend architecture.
- Database architecture.
- Authentication and authorization.
- API communication.
- External integrations.
- Background processing.
- Deployment configuration.
- Logging and monitoring.

Document how important components interact.

Base architectural findings on actual repository evidence.

Clearly distinguish implemented architecture from proposed or documented architecture.

## 3. Assess Current Implementation

Identify:

- Completed features.
- Partially completed features.
- Missing features.
- Known defects.
- Technical debt.
- Existing tests.
- Build and deployment status.
- Security concerns.
- Incomplete integrations.

Compare the actual implementation against existing documentation.

Do not mark a feature complete solely because it appears in a README or project plan.

## 4. Establish Project Context

Inspect existing documentation.

If `docs/Project_Notes.md` exists:

- Read it.
- Compare it with the actual implementation.
- Identify outdated information.
- Preserve useful technical decisions and historical entries.
- Record discrepancies that need clarification.

If it does not exist:

- Initialize it using Foundation's Project Notes template.
- Populate it using verified repository information.
- Mark unknown information clearly instead of guessing.
- Preserve existing project documentation.

Do not silently replace established project documentation with generic Foundation templates.

## 5. Identify Next Steps

Identify:

- Important technical risks.
- Incomplete functionality.
- Existing defects.
- Blockers and dependencies.
- Missing verification.
- Security concerns.
- Opportunities for improvement.

Prioritize development opportunities based on project requirements and actual implementation status.

Recommend the next actionable milestone.

Avoid proposing a rewrite when incremental improvements are sufficient.

## 6. Introduce Foundation Standards

Apply relevant engineering rules without unnecessarily restructuring the existing project.

- Adapt Foundation's standards to the project's actual technology stack.
- Preserve existing architecture unless a justified change is approved.
- Preserve existing build systems, package managers and tooling where practical.
- Avoid replacing established dependencies without a clear reason.
- Introduce missing standards incrementally.
- Identify conflicts between Foundation rules and existing project conventions.
- Document necessary adaptations.

Do not blindly replace existing tools, architecture or workflows.

## 7. Verification

Run safe and relevant baseline checks:

- Existing tests.
- Build verification.
- Linting.
- Type checking.
- Configuration checks.
- Static analysis where available.

Before executing checks:

- Inspect their commands and potential side effects.
- Avoid destructive operations.
- Do not overwrite existing databases or user data.
- Do not expose secrets.
- Avoid live external integrations unless explicitly required and permitted.

Record actual results.

Distinguish:

- Passed.
- Failed.
- Not run.
- Blocked.
- Not applicable.

Do not fix unrelated defects during onboarding unless specifically requested.

## 8. Git and Repository Safety

Follow Foundation's Git and Documentation Standards.

- Inspect Git state before and after onboarding.
- Preserve all existing user changes.
- Do not discard, reset or overwrite uncommitted work.
- Do not change branches or remotes without authorization.
- Do not automatically push changes.
- Do not commit onboarding changes unless they are part of an explicitly authorized task.

Report the repository's initial and final Git state.

## 9. Final Report

Provide:

1. Repository overview.
2. Technology stack.
3. Architecture summary.
4. Existing functionality.
5. Incomplete functionality.
6. Testing and build status.
7. Git state.
8. Documentation status.
9. Identified risks and blockers.
10. Foundation compatibility findings.
11. Recommended next development milestone.

Support important findings with relevant file paths or verification evidence.

Clearly distinguish confirmed facts, assumptions and recommendations.

## Completion Criteria

Onboarding is complete when:

- The repository has been inspected.
- Existing architecture is understood.
- Current implementation status is assessed.
- Existing documentation is reviewed.
- Project context is established.
- Git state and user changes are preserved.
- Relevant baseline checks are recorded.
- Important risks and blockers are documented.
- A clear next development milestone is identified.