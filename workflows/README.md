# Foundation — Engineering Workflows

This directory contains the standardized engineering workflows used by Foundation.

These documents define how engineering activities should be planned, coordinated, executed, verified and completed.

## Available Workflows

| Workflow | Purpose |
|---|---|
| 01 - New Project | Discover, design and develop a new software project |
| 02 - Existing Project | Audit, understand and onboard an existing repository |
| 03 - Feature Development | Implement and verify individual features |
| 04 - Bug Fixing | Investigate, resolve and verify software defects |
| 05 - Autonomous Sprint | Coordinate and execute a bounded set of development tasks |
| 06 - Release Verification | Assess software release readiness |

## How Workflows Are Used

- The Engineering Orchestrator identifies and coordinates the appropriate workflow.
- Relevant Skills provide detailed execution procedures.
- Specialist Agents perform focused engineering responsibilities.
- Engineering Rules establish project-wide implementation standards.
- `docs/Project_Notes.md` maintains persistent project context, decisions and progress.

Workflows are selected according to the task. They are not necessarily executed sequentially or all required for every development activity.

## Standard Engineering Lifecycle

UNDERSTAND → INSPECT → PLAN → IMPLEMENT → INTEGRATE → VERIFY → DOCUMENT → COMMIT → REPORT

The lifecycle may be adapted according to project requirements and task complexity.

## Autonomy and Approval

Foundation supports autonomous execution within approved project scope.

User approval is required for consequential actions outside established autonomy boundaries, including:

- Remote Git pushes.
- Deployment and publication.
- Destructive operations.
- Production infrastructure or data changes.
- Decisions that materially change project scope or architecture.

## Git Policy

Foundation supports automated local commits after successful verification.

- Stage only relevant changes.
- Preserve unrelated user modifications.
- Inspect the final Git diff.
- Remote pushes require explicit user authorization.

## Important

These documents define engineering processes. They do not independently execute commands or create agent capabilities.

Actual execution depends on the Engineering Orchestrator, available Skills, configured Agents, permitted tools and the project's engineering environment.