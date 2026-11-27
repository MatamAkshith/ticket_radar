
---
trigger: always_on
description: Software architecture, system design and modularity standards.
---

# Architecture Standards

## General Principles

- Understand the existing architecture before proposing changes.
- Prefer modular, maintainable and scalable designs.
- Follow separation of concerns.
- Keep business logic separate from presentation and infrastructure.
- Avoid unnecessary abstractions and overengineering.
- Reuse existing components and services where appropriate.
- Define clear boundaries between modules.
- Consider scalability, reliability and maintainability.
- Document significant architectural decisions.
- Explain the impact of major architectural changes before implementing them.

## System Design

- Define component responsibilities clearly.
- Establish explicit interfaces between components.
- Avoid unnecessary coupling.
- Define shared contracts before parallel implementation.
- Keep platform-specific implementation details isolated.
- Consider failure handling and recovery as part of architecture.
- Avoid introducing infrastructure without a demonstrated requirement.

## Ticket Radar Architecture Principles

- Keep platform-specific integrations isolated through dedicated adapters.
- Separate monitoring orchestration from platform data collection.
- Separate availability snapshots from change detection and event generation.
- Keep notification delivery independent of monitoring logic.
- Maintain clear boundaries between frontend, backend, database and external services.
- Treat external platform information as untrusted input.
- Distinguish confirmed observations from unknown, unavailable or failed data.
- Ensure monitoring failures do not automatically become availability changes.
- Design monitoring operations to handle repeated execution safely.
- Respect external platform access restrictions and reasonable request limits.

## Integration and Dependencies

- Define API contracts and shared data structures before independent component development.
- Document dependencies between components.
- Avoid duplicated business logic.
- Ensure components can be tested independently where practical.
- Communicate architectural changes to affected specialists.

## Architecture Decisions

- Record significant decisions in `docs/Project_Notes.md` or relevant architecture documents.
- Document alternatives and trade-offs where appropriate.
- Distinguish proposed architecture from approved architecture.
- Verify external service capabilities before designing around assumed functionality.
- Revisit decisions when new evidence invalidates previous assumptions.

## Restrictions

- Do not introduce unnecessary architectural complexity.
- Do not assume platform capabilities without verification.
- Do not bypass external platform restrictions.
- Do not make major architectural changes without communicating their impact.
- Do not document proposed designs as implemented systems.