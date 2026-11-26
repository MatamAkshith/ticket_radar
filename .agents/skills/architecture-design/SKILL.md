
---
name: architecture-design
description: Designs software system architecture, technology stacks, application modules, database schemas, API contracts, integrations and data flows. Use when designing a new application or making significant architectural changes.
---

# Architecture Design Skill

## Objective

Translate validated product requirements into a practical, maintainable and technically sound software architecture.

Architecture must serve the product requirements rather than introduce unnecessary complexity.

## 1. Review Inputs

Before designing:

- Read the project discovery document.
- Review functional and non-functional requirements.
- Inspect existing architecture when working on an existing project.
- Review technical constraints.
- Identify dependencies and integrations.
- Review docs/Project_Notes.md when available.

Do not design against assumptions that have not been validated.

## 2. Define System Architecture

Identify:

- Major system components.
- Responsibilities of each component.
- Communication between components.
- External services.
- Application boundaries.
- Important execution flows.

Choose an architecture appropriate to the project's scale and complexity.

Avoid unnecessary microservices and distributed infrastructure.

## 3. Select Technology Stack

Evaluate appropriate technologies for:

- Frontend.
- Backend.
- Database.
- Authentication.
- File storage.
- APIs.
- Background processing.
- External integrations.
- Deployment and hosting.

Consider:

- Project requirements.
- Developer familiarity.
- Maintainability.
- Performance.
- Cost.
- Scalability.
- Ecosystem maturity.

Explain important technology choices and their trade-offs.

Do not select technologies merely because they are popular.

## 4. Design Application Modules

Break the system into logical modules.

For each module, document:

- Purpose.
- Responsibilities.
- Inputs and outputs.
- Dependencies.
- Interactions with other modules.

Maintain clear separation of concerns.

## 5. Design Database Architecture

When a database is required:

- Identify entities.
- Define attributes.
- Establish relationships.
- Choose primary and foreign keys.
- Identify constraints.
- Consider indexes.
- Plan migrations.
- Consider access-control requirements.

Explain important database design decisions.

## 6. Design API Contracts

When APIs are required, define:

- Endpoints.
- HTTP methods.
- Request structures.
- Response structures.
- Authentication requirements.
- Authorization rules.
- Validation requirements.
- Error responses.

Maintain consistency across frontend and backend contracts.

## 7. Design Data Flows

Describe how data moves through the system.

Include relevant flows such as:

- User interactions.
- Authentication.
- Database operations.
- External API calls.
- Background jobs.
- Notifications.
- Error handling.

Use architecture diagrams or sequence diagrams when they improve understanding.

## 8. Address Security and Reliability

Consider:

- Authentication and authorization.
- Input validation.
- Data protection.
- Secret management.
- Rate limiting.
- Error handling.
- Logging and monitoring.
- Backup and recovery.
- Failure handling.

Security must be considered during design, not added as an afterthought.

## 9. Evaluate Trade-offs

For significant architectural decisions, document:

- Decision.
- Alternatives considered.
- Reason for selection.
- Advantages.
- Disadvantages.
- Future implications.

Avoid presenting subjective preferences as technical facts.

## 10. Produce Architecture Documents

Prepare relevant documents:

- System architecture.
- Component/module architecture.
- Database design.
- API contracts.
- Data flow diagrams.
- Technology stack rationale.
- Architecture Decision Records.

Only create documents relevant to the project.

## 11. Update Project Context

When working on a Foundation-based project:

- Update docs/Project_Notes.md with approved architectural decisions.
- Keep architecture and database sections synchronized.
- Record important trade-offs.
- Do not silently overwrite previous decisions.
- Preserve historical architectural changes.

## 12. Handoff

Provide the approved architecture to implementation-planning.

Identify dependencies, technical risks and implementation constraints.

Do not begin large-scale implementation until the architecture is sufficiently clear.

## Completion Criteria

Architecture design is complete when:

- Major system components are defined.
- Technology choices are justified.
- Module responsibilities are clear.
- Database design is documented when applicable.
- API contracts are defined when applicable.
- Important data flows are understood.
- Security and reliability concerns are addressed.
- Major decisions and trade-offs are recorded.
- The design is ready for implementation planning.
