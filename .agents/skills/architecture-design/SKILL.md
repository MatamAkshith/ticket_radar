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
- Review `docs/Project_Notes.md` when available.
- Verify which external integrations are confirmed, unverified or unsupported.

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
- Operational complexity.

Explain important technology choices and their trade-offs.

Do not select technologies merely because they are popular.

Do not finalize the proposed Ticket Radar stack until its requirements and external integration constraints have been evaluated.

## 4. Design Application Modules

Break the system into logical modules.

For each module, document:

- Purpose.
- Responsibilities.
- Inputs and outputs.
- Dependencies.
- Interactions with other modules.

Maintain clear separation of concerns.

For Ticket Radar, evaluate the need for separate modules covering:

- Movie and cinema configuration.
- Platform-specific data collection.
- Monitoring orchestration and scheduling.
- Availability normalization.
- Snapshot storage and comparison.
- Availability event generation.
- Notification delivery.
- User preferences.
- Dashboard and API integration.

These are architectural responsibilities, not mandatory separate services.

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
- Define data retention requirements.

For Ticket Radar, consider:

- Monitored movies and cinemas.
- Platform and screening information.
- Monitoring configurations.
- Availability observations and historical snapshots.
- Generated availability events.
- Notification delivery records.
- Monitoring execution status and errors.

Preserve historical observations when they provide value for change detection and debugging.

Prevent duplicate events and duplicate notification delivery through appropriate identifiers, constraints and idempotent processing.

Do not finalize the schema before requirements and data availability are understood.

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

For monitoring applications, expose data freshness and monitoring status where appropriate.

Do not represent stale, failed or unknown observations as confirmed availability.

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

For Ticket Radar, explicitly design the monitoring lifecycle:

1. Load the monitoring configuration.
2. Execute a permitted platform-specific collection process.
3. Normalize the collected information.
4. Validate and timestamp the observation.
5. Store the observation.
6. Compare it with previous valid observations.
7. Generate events only when meaningful changes are confirmed.
8. Deliver eligible notifications.
9. Record execution and delivery results.

A failed monitoring run must never generate a false availability event.

## 8. Platform Integration Architecture

For Ticket Radar, isolate BookMyShow and PVR/INOX integrations behind platform-specific adapters.

Each adapter should:

- Have a clearly defined interface.
- Handle platform-specific data formats.
- Normalize results into a shared internal representation.
- Report collection failures explicitly.
- Respect permitted access methods and documented limits.
- Avoid exposing platform-specific implementation details to unrelated modules.

Do not assume both platforms expose the same information.

Do not assume seat-level availability is accessible.

Do not design integrations that depend on bypassing authentication, CAPTCHAs, rate limits or anti-bot protections.

Keep external platform dependencies replaceable so that changes or discontinued integrations do not require rewriting the entire application.

## 9. Availability and Event Integrity

Define how the system distinguishes:

- Confirmed available.
- Confirmed unavailable.
- Unknown.
- Stale.
- Collection failed.

Establish rules for:

- Observation freshness.
- Meaningful availability changes.
- Duplicate event prevention.
- Repeated monitoring runs.
- Notification retries.
- Partial platform failures.

Only verified changes should generate availability notifications.

Preserve enough execution evidence to explain why an event was generated.

## 10. Address Security and Reliability

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
- External integration resilience.

Security must be considered during design, not added as an afterthought.

## 11. Evaluate Trade-offs

For significant architectural decisions, document:

- Decision.
- Alternatives considered.
- Reason for selection.
- Advantages.
- Disadvantages.
- Future implications.

Avoid presenting subjective preferences as technical facts.

Prefer the simplest architecture that satisfies the validated requirements.

## 12. Produce Architecture Documents

Prepare relevant documents:

- System architecture.
- Component/module architecture.
- Database design.
- API contracts.
- Data flow diagrams.
- Technology stack rationale.
- Architecture Decision Records.

Only create documents relevant to the project.

## 13. Update Project Context

When working on a Foundation-based project:

- Update `docs/Project_Notes.md` with approved architectural decisions.
- Keep architecture and database sections synchronized.
- Record important trade-offs.
- Do not silently overwrite previous decisions.
- Preserve historical architectural changes.
- Clearly distinguish proposed decisions from approved decisions.

## 14. Handoff

Provide the approved architecture to implementation-planning.

Identify dependencies, technical risks and implementation constraints.

Highlight unresolved integration questions and architectural assumptions.

Do not begin large-scale implementation until the architecture is sufficiently clear.

## Completion Criteria

Architecture design is complete when:

- Major system components are defined.
- Technology choices are justified.
- Module responsibilities are clear.
- External integrations have been assessed.
- Database design is documented when applicable.
- API contracts are defined when applicable.
- Important data flows are understood.
- Availability and event integrity are addressed where applicable.
- Security and reliability concerns are addressed.
- Major decisions and trade-offs are recorded.
- The design is ready for implementation planning.