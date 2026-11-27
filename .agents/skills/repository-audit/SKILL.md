---
name: repository-audit
description: Inspects existing software repositories, source code, architecture, dependencies, configuration, database structure, tests and technical debt. Use before modifying an existing project or when evaluating an unfamiliar codebase.
---

# Repository Audit Skill

## Objective

Understand the current state of a software repository before planning or implementing changes.

Never assume that the repository matches its documentation perfectly.

The audit is read-only. Its purpose is to establish an evidence-based understanding of the codebase without modifying application code or disrupting existing work.

## 1. Inspect Repository Structure

Identify:

- Main application directories.
- Frontend and backend components.
- Configuration files.
- Documentation.
- Test directories.
- Scripts and automation.
- Deployment configuration.
- Agent and engineering workflow configuration.

Provide a concise overview of the directory structure.

Identify important files and explain their apparent responsibilities.

Do not recursively inspect irrelevant dependency directories or generated build artifacts unless necessary.

## 2. Identify the Technology Stack

Inspect relevant dependency and configuration files.

Identify:

- Programming languages.
- Frameworks and libraries.
- Package managers.
- Runtime versions.
- Build tools.
- Database technologies.
- Authentication systems.
- External services.
- Development and deployment tooling.

Do not infer installed dependencies from documentation alone.

Distinguish declared dependencies from verified installed dependencies.

Identify outdated, duplicated or potentially incompatible dependencies when evidence supports the finding.

## 3. Understand the Architecture

Investigate:

- Application entry points.
- Main modules and responsibilities.
- Component relationships.
- API structure.
- Data flow.
- Authentication and authorization.
- External integrations.
- Background processes.
- Configuration and environment handling.

Trace important execution paths when necessary.

Identify actual dependencies between modules rather than relying only on directory names.

Document architectural inconsistencies and unnecessary coupling when found.

## 4. Inspect the Database

When applicable, examine:

- Schema definitions.
- Models and entities.
- Relationships.
- Migrations.
- Constraints and indexes.
- Database access patterns.
- Security policies.
- Data validation.
- Transaction handling.

Identify schema inconsistencies and potential data-integrity risks.

Never modify, reset, migrate or delete data from a database during an audit.

Do not expose credentials or sensitive database contents in the report.

## 5. Inspect Existing Functionality

Identify:

- Implemented features.
- Partially implemented features.
- Missing functionality.
- Existing application workflows.
- Known defects.
- Unfinished placeholders.
- Incomplete integrations.

Compare the implementation against available project documentation.

Distinguish implemented functionality from planned functionality.

Do not mark features complete merely because their UI, API endpoint or documentation exists.

## 6. Inspect Quality and Testing

Identify:

- Available test suites.
- Test frameworks.
- Build commands.
- Linting and formatting tools.
- Type checking.
- Existing CI configuration.
- Current verification coverage.

Run safe, relevant checks when authorized and practical.

Before executing commands, inspect their potential side effects.

Avoid destructive commands, production data modifications and unauthorized external operations.

Report actual results using clear statuses:

- Passed.
- Failed.
- Not run.
- Blocked.
- Not applicable.

Do not claim that a build or test passed without executing it or examining reliable execution evidence.

## 7. Inspect Git State

Examine:

- Current branch.
- Configured remotes.
- Working tree status.
- Staged changes.
- Unstaged changes.
- Untracked files.
- Recent commits when useful.
- Relevant project history.

Preserve all existing user modifications.

Do not:

- Create commits during an audit.
- Push changes.
- Switch branches.
- Reset or clean the working tree.
- Discard or overwrite user modifications.
- Modify Git configuration.

Report the initial Git state accurately.

## 8. Inspect Security and Dependencies

Look for potential issues involving:

- Exposed secrets or credentials.
- Unsafe configuration.
- Authentication and authorization.
- Input validation.
- Dependency vulnerabilities.
- Insecure external integrations.
- Unsafe file handling.
- Sensitive data exposure.
- Excessive permissions.
- Missing security controls.

Do not print secret values in audit reports.

Do not modify dependencies or configuration during the audit.

Distinguish verified vulnerabilities from potential risks requiring further investigation.

## 9. Identify Risks and Technical Debt

Look for:

- Security weaknesses.
- Dependency problems.
- Architectural inconsistencies.
- Duplicate implementations.
- Performance concerns.
- Missing tests.
- Documentation mismatches.
- Technical debt.
- Fragile integrations.
- Incomplete error handling.

Classify findings by severity:

- Critical: Immediate and substantial risk to security, data integrity or core functionality.
- High: Significant defect or risk requiring prompt attention.
- Medium: Meaningful issue that should be addressed during planned development.
- Low: Minor improvement or maintainability concern.
- Informational: Observation that does not currently require corrective action.

For each important finding, include:

- Description.
- Relevant file path or component.
- Supporting evidence.
- Potential impact.
- Recommended next step.

Distinguish confirmed defects from potential concerns.

## 10. Produce Audit Report

Prepare a report containing:

1. Repository overview.
2. Technology stack.
3. Architecture summary.
4. Important modules.
5. Database overview.
6. Implemented functionality.
7. Testing and build status.
8. Git working state.
9. Security and dependency findings.
10. Identified risks.
11. Technical debt.
12. Documentation mismatches.
13. Recommended next steps.

Prioritize findings by severity and impact.

Support important conclusions with repository evidence.

Clearly distinguish verified facts, assumptions and recommendations.

## 11. Update Project Context

When auditing a project that uses Foundation:

- Read `docs/Project_Notes.md` first.
- Compare documentation with the actual repository.
- Report outdated or incorrect documentation.
- Update project notes only when authorized or as part of the assigned task.
- Never silently replace documented decisions.
- Preserve historical development information.

An audit must remain read-only unless a separate task explicitly authorizes documentation changes.

## 12. Handoff

Provide audit findings to the engineering orchestrator.

Identify:

- Existing implementation that should be preserved.
- Critical issues requiring attention.
- Missing requirements or documentation.
- Architectural concerns.
- Verification gaps.
- Recommended next development tasks.

Do not begin implementation as part of the audit.

## Completion Criteria

An audit is complete when:

- Repository structure is understood.
- Technology stack is identified.
- Major architectural components are mapped.
- Existing functionality is assessed.
- Database structure is understood where applicable.
- Git state is understood.
- Relevant quality checks are recorded.
- Security and dependency risks are assessed.
- Findings include supporting evidence.
- Risks are prioritized.
- Recommendations are presented clearly.

No application code or existing user work has been modified during the audit.