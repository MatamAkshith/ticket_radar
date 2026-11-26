
---
name: existing-project-onboarding
description: Onboards Foundation into an existing software repository by inspecting its architecture, technology stack, implementation, documentation, dependencies and development status. Use when starting work on an existing project.
---

# Existing Project Onboarding

## Objective

Understand an existing software project before making changes or introducing Foundation workflows.

## 1. Initial Inspection

- Invoke repository-audit.
- Inspect repository structure.
- Identify languages and frameworks.
- Inspect dependencies and configuration.
- Identify application entry points.
- Inspect important modules.
- Understand the current Git state.

Do not modify application code during the initial audit.

## 2. Understand Existing Architecture

Identify:

- Frontend architecture.
- Backend architecture.
- Database architecture.
- Authentication.
- API communication.
- External integrations.
- Deployment configuration.

Document how important components interact.

## 3. Assess Current Implementation

Identify:

- Completed features.
- Partially completed features.
- Missing features.
- Known defects.
- Technical debt.
- Existing tests.
- Build and deployment status.

Compare the actual implementation against existing documentation.

## 4. Establish Project Context

Inspect existing documentation.

If docs/Project_Notes.md exists:

- Read it.
- Compare it with the actual implementation.
- Identify outdated information.

If it does not exist:

- Initialize it using Foundation's Project Notes template.
- Populate it using verified repository information.
- Mark unknown information clearly instead of guessing.

Preserve useful existing project documentation.

## 5. Identify Next Steps

- List important technical risks.
- Identify incomplete functionality.
- Identify blockers and dependencies.
- Prioritize development opportunities.
- Recommend the next actionable milestone.

## 6. Introduce Foundation Standards

Apply relevant engineering rules without unnecessarily restructuring the existing project.

Adapt Foundation's standards to the project's actual technology stack.

Do not blindly replace existing tools or architecture.

## 7. Verification

Run safe and relevant baseline checks:

- Existing tests.
- Build verification.
- Linting.
- Type checking.
- Configuration checks.

Record actual results.

Do not fix unrelated defects during onboarding unless specifically requested.

## 8. Final Report

Provide:

- Repository overview.
- Technology stack.
- Architecture summary.
- Existing functionality.
- Testing status.
- Git state.
- Documentation status.
- Identified risks.
- Recommended next steps.

## Completion Criteria

Onboarding is complete when the repository is understood, project context is established, important risks are documented and a clear next development milestone is identified.
