
# Foundation — AI Engineering System

## 1. Purpose

Foundation is a reusable AI Engineering Framework designed to help AI agents plan, develop, test, review and maintain software projects reliably.

It establishes consistent engineering standards, reusable skills, workflows, specialist agents and quality gates across different projects and technology stacks.

## 2. Core Engineering Principles

All agents working with Foundation must follow these principles:

- Understand before implementing.
- Inspect before modifying.
- Plan before significant development.
- Follow existing project architecture and conventions.
- Prefer simple, maintainable solutions.
- Make incremental and controlled changes.
- Verify implementations through actual tests.
- Protect existing user work.
- Prioritize security and data integrity.
- Document important decisions and changes.
- Never claim something works without evidence.

## 3. Engineering Workflow

Every significant development task should follow this lifecycle:

1. Understand the requirements.
2. Read the project's documentation.
3. Inspect the existing repository.
4. Identify constraints and dependencies.
5. Define acceptance criteria.
6. Create an implementation plan.
7. Delegate independent tasks when appropriate.
8. Implement incrementally.
9. Run relevant tests.
10. Review the implementation.
11. Fix identified issues.
12. Update project documentation.
13. Complete the appropriate local Git commit.
14. Report the final results.

## 4. Repository Inspection

Before making changes:

- Inspect the repository structure.
- Read relevant project documentation.
- Identify the technology stack.
- Understand existing architecture.
- Inspect relevant source files.
- Check existing dependencies.
- Inspect Git status and existing changes.
- Identify relevant tests and build commands.

Never assume that a project is empty or that a particular architecture exists without inspection.

## 5. Code Modification Standards

- Follow existing language and framework conventions.
- Use meaningful variable, function and class names.
- Keep functions focused on their responsibilities.
- Avoid unnecessary abstractions.
- Avoid unnecessary dependencies.
- Reuse existing functionality where appropriate.
- Handle errors explicitly.
- Avoid modifying unrelated files.
- Preserve existing user changes.
- Explain significant architectural modifications.

## 6. Testing and Verification

- Identify acceptance criteria before implementation.
- Write tests for important functionality.
- Include edge cases and error scenarios.
- Run relevant tests after changes.
- Run integration tests when components interact.
- Verify builds where applicable.
- Test important user journeys.
- Investigate failures instead of hiding them.
- Report skipped, failed and unavailable tests honestly.
- Never fabricate verification results.

## 7. Security and Privacy

- Never expose API keys, passwords or secrets.
- Never hardcode sensitive credentials.
- Use environment variables or approved secret-management systems.
- Validate untrusted input.
- Apply authentication and authorization where required.
- Follow least-privilege access principles.
- Protect sensitive user information.
- Avoid logging private data.
- Review dependencies for security concerns.
- Never weaken security controls merely to make functionality work.

## 8. Database Standards

- Understand the existing database schema before modifying it.
- Design schemas with clear relationships and constraints.
- Use appropriate primary and foreign keys.
- Maintain data integrity.
- Use migrations where appropriate.
- Review migrations before applying them.
- Avoid unnecessary database queries.
- Consider indexes for frequently queried fields.
- Use transactions when necessary.
- Never reset, truncate or delete production data without explicit approval.

## 9. Git and Version Control

Follow the dedicated rules in:

.agents/rules/06-git-documentation.md

Important requirements:

- Inspect Git status before development.
- Preserve unrelated user changes.
- Automatically create local commits after verified development tasks.
- Stage only files belonging to the completed task.
- Never commit secrets or known failing implementations.
- Never automatically push to a remote repository.
- Wait for explicit user authorization before remote operations.
- Never force-push.

## 10. Persistent Project Context

Every project using Foundation should maintain a central documentation file:

docs/Project_Notes.md

Before starting a development task:

1. Locate and read Project_Notes.md.
2. Review the current development status.
3. Understand the system architecture.
4. Understand the project workflow.
5. Review the technology stack.
6. Review previous architectural decisions.
7. Check completed and pending tasks.
8. Inspect the actual codebase before making assumptions.

After completing a development task:

1. Update the current development status.
2. Update architecture documentation when affected.
3. Update workflow documentation when affected.
4. Record important technical decisions.
5. Update the completed progress tracker.
6. Update pending work.
7. Append a meaningful development log entry.
8. Record actual verification results.

Project documentation must remain consistent with the actual implementation.

## 11. Documentation Standards

- Keep documentation understandable and useful.
- Explain why important technical decisions were made.
- Maintain chronological development history.
- Avoid unnecessary code dumps.
- Update affected documentation after implementation.
- Never document unverified functionality as complete.
- Preserve historical development entries.
- Do not fabricate project information.

## 12. Autonomy and Approval Boundaries

Agents may independently perform routine, reversible development tasks within the authorized workspace.

Human approval is required before:

- Production deployments.
- Destructive database operations.
- Force pushes.
- Changes to external infrastructure.
- Operations involving sensitive credentials.
- Actions outside the authorized project scope.
- Remote Git operations.

Local development, testing, documentation updates and verified local commits may be automated.

## 13. Specialist Agent Coordination

When specialist agents are available:

- Assign focused responsibilities.
- Define clear task boundaries.
- Establish interfaces and dependencies before parallel execution.
- Avoid assigning conflicting file ownership.
- Review delegated work before integration.
- Require verification of completed tasks.
- Keep the orchestrator responsible for final integration.

Do not introduce parallel agents when a task is too small to benefit from delegation.

## 14. Completion Requirements

A meaningful development task is complete only when:

- The requested implementation exists.
- Relevant verification has been performed.
- Documentation has been updated.
- The Git diff has been reviewed.
- An appropriate local commit has been created.
- Known issues and limitations are documented.
- The final report accurately describes the result.

Code being written does not automatically mean a task is complete.
