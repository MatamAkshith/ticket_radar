
---
name: repository-audit
description: Inspects existing software repositories, source code, architecture, dependencies, configuration, database structure, tests and technical debt. Use before modifying an existing project or when evaluating an unfamiliar codebase.
---

# Repository Audit Skill

## Objective

Understand the current state of a software repository before planning or implementing changes.

Never assume that the repository matches its documentation perfectly.

## 1. Inspect Repository Structure

Identify:

- Main application directories.
- Frontend and backend components.
- Configuration files.
- Documentation.
- Test directories.
- Scripts and automation.
- Deployment configuration.

Provide a concise overview of the directory structure.

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

Do not infer installed dependencies from documentation alone.

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

Trace important execution paths when necessary.

## 4. Inspect the Database

When applicable, examine:

- Schema definitions.
- Models and entities.
- Relationships.
- Migrations.
- Constraints and indexes.
- Database access patterns.
- Security policies.

Never modify or reset a database during an audit.

## 5. Inspect Existing Functionality

Identify:

- Implemented features.
- Partially implemented features.
- Missing functionality.
- Existing application workflows.
- Known defects.
- Unfinished placeholders.

Compare the implementation against available project documentation.

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

Report actual results.

## 7. Inspect Git State

Examine:

- Current branch.
- Working tree status.
- Existing uncommitted changes.
- Recent commits when useful.
- Relevant project history.

Preserve all existing user modifications.

Do not create commits during an audit.

## 8. Identify Risks

Look for:

- Security weaknesses.
- Dependency problems.
- Architectural inconsistencies.
- Duplicate implementations.
- Performance concerns.
- Missing tests.
- Documentation mismatches.
- Technical debt.

Distinguish confirmed defects from potential concerns.

## 9. Produce Audit Report

Prepare a report containing:

1. Repository overview.
2. Technology stack.
3. Architecture summary.
4. Important modules.
5. Database overview.
6. Implemented functionality.
7. Testing and build status.
8. Git working state.
9. Identified risks.
10. Technical debt.
11. Recommended next steps.

Prioritize findings by severity and impact.

## 10. Update Project Context

When auditing a project that uses Foundation:

- Read docs/Project_Notes.md first.
- Compare documentation with the actual repository.
- Report outdated or incorrect documentation.
- Update project notes only when authorized or as part of the assigned task.
- Never silently replace documented decisions.

## Completion Criteria

An audit is complete when:

- Repository structure is understood.
- Technology stack is identified.
- Major architectural components are mapped.
- Existing functionality is assessed.
- Git state is understood.
- Relevant risks are documented.
- Findings are presented clearly.

Do not modify application code as part of a read-only audit.
