
---
trigger: always_on
description: Code quality, readability and maintainability standards.
---

# Coding Standards

## General Principles

- Write clean, readable and maintainable code.
- Follow the language and framework conventions of the project.
- Use meaningful variable, function and class names.
- Keep functions focused on a single responsibility.
- Avoid unnecessary code duplication.
- Handle errors explicitly.
- Avoid unnecessary dependencies.
- Prefer simple solutions over complicated ones.
- Add comments when they clarify non-obvious logic.
- Do not modify unrelated code.
- Follow existing formatting and linting conventions.
- Do not leave unfinished placeholder implementations without reporting them.

## Code Organization

- Keep modules focused on clearly defined responsibilities.
- Separate business logic, presentation and data access.
- Reuse existing utilities and components where appropriate.
- Avoid tightly coupled modules.
- Keep configuration separate from application logic.
- Follow established project directory conventions.

## Data and API Handling

- Validate all external and user-provided input.
- Treat external platform responses as untrusted data.
- Handle missing, malformed and incomplete information safely.
- Follow approved API contracts.
- Use consistent error and response structures.
- Avoid hardcoding external service assumptions.
- Use idempotent operations where repeated execution could create duplicate records or events.

## Reliability

- Handle network and external service failures explicitly.
- Use bounded retries where appropriate.
- Avoid uncontrolled background execution.
- Preserve data integrity during updates.
- Distinguish unavailable information from confirmed negative results.
- Avoid silently swallowing exceptions.

## Security

- Never hardcode passwords, API keys or tokens.
- Use approved environment configuration or secret-management mechanisms.
- Never expose sensitive information in logs or responses.
- Follow established security standards.
- Do not weaken security controls to make functionality work.

## Ticket Radar-Specific Practices

- Keep platform-specific code isolated in appropriate adapters.
- Avoid mixing monitoring logic with notification delivery.
- Avoid generating duplicate availability events.
- Preserve observation timestamps where relevant.
- Do not fabricate or assume ticket availability.
- Respect platform access restrictions and monitoring limits.

## Code Completion

- Remove temporary debugging code before completion.
- Report unfinished implementations and known limitations.
- Ensure relevant tests are updated.
- Verify changes before declaring them complete.
- Document meaningful implementation decisions.