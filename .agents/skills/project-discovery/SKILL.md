---
name: project-discovery
description: Analyzes new software ideas, requirements, user needs, project goals, scope and constraints. Use when starting a new project, exploring an idea, gathering requirements or clarifying what needs to be built.
---

# Project Discovery Skill

## Objective

Understand the software project before implementation begins.

Transform an initial idea into a clear, structured and actionable understanding of the product.

Discovery must establish what should be built, why it matters, who will use it, and which constraints affect implementation.

Do not confuse an attractive product idea with a technically validated solution.

## 1. Understand the Idea

Identify:

- What problem is being solved?
- Why does the problem matter?
- Who experiences this problem?
- What solution is being proposed?
- What makes the solution useful?
- What outcome should the user achieve?

Do not assume that an initial idea contains all necessary requirements.

## 2. Identify Users

Determine:

- Primary user groups.
- Their goals.
- Their main problems.
- Their expected interactions with the application.
- Their permissions and responsibilities.

Create user personas only when they provide meaningful value.

## 3. Gather Functional Requirements

Identify what the application must do.

Organize requirements into:

- Core functionality.
- User authentication and authorization.
- Main application features.
- Data management.
- External integrations.
- Notifications and background processes.
- Administrative functionality.

For Ticket Radar, explicitly investigate:

- Movie and cinema selection.
- City and location preferences.
- Booking release detection.
- Showtime and screening-format availability.
- Seat availability monitoring, where permitted and technically supported.
- Availability change detection.
- Notification preferences and delivery.
- Monitoring history and event history.
- Dashboard functionality.
- Monitoring failure and recovery behavior.

Do not treat every proposed feature as confirmed or feasible.

## 4. Gather Non-Functional Requirements

Identify relevant requirements concerning:

- Performance.
- Scalability.
- Reliability.
- Security.
- Privacy.
- Accessibility.
- Maintainability.
- Compatibility.
- Monitoring frequency and resource consumption.
- Data freshness and accuracy.
- Failure recovery.

For monitoring applications, distinguish between data freshness and guaranteed real-time availability.

## 5. Define Scope

Separate requirements into:

- MVP: Essential functionality for the first working version.
- Future Features: Useful additions that can be implemented later.
- Out of Scope: Features that are intentionally excluded.

Avoid unnecessary feature expansion.

For Ticket Radar, preserve the explicit boundary that the application informs users about availability but does not automatically book tickets or make payments.

## 6. Identify Constraints

Record:

- Required technology preferences.
- Budget limitations.
- Time constraints.
- Available infrastructure.
- External dependencies.
- Regulatory or privacy requirements.
- Existing project constraints.
- Platform access restrictions and permitted integration methods.

For Ticket Radar, investigate BookMyShow and PVR/INOX access separately.

Do not assume that public website visibility means automated access is permitted.

Do not assume that seat-level information is accessible through a supported interface.

Do not propose bypassing CAPTCHAs, authentication, rate limits or anti-bot protections.

Distinguish confirmed requirements from assumptions.

## 7. Identify Risks and Unknowns

Document:

- Unclear requirements.
- Technical uncertainties.
- External service dependencies.
- Security concerns.
- Potential implementation difficulties.
- Platform availability and access limitations.
- Notification delivery dependencies.
- Data accuracy and freshness limitations.

For Ticket Radar, explicitly investigate:

- Whether booking-release information can be obtained reliably.
- Whether showtimes and screening formats can be monitored.
- Whether seat-level availability is accessible through permitted methods.
- Whether platform changes could break integrations.
- Whether monitoring frequency can remain within permitted limits.
- How the system will distinguish confirmed unavailability from failed or incomplete checks.

Ask focused clarification questions when missing information materially affects the solution.

Do not invent answers or claim external integration feasibility without evidence.

## 8. Validate External Dependencies

Before treating an external integration as an implementation requirement:

1. Identify the platform or service.
2. Investigate its official APIs and documented integration options.
3. Review relevant terms, access restrictions and rate limits.
4. Identify the data actually available.
5. Record technical and operational limitations.
6. Identify fallback options where appropriate.

Classify findings as:

- Confirmed: Supported by reliable evidence.
- Unverified: Requires further investigation.
- Unsupported: No permitted or practical integration method has been established.
- Blocked: Access or implementation is currently prevented by a known constraint.

Do not begin implementation of an unverified integration as though its feasibility were established.

## 9. Produce Discovery Documents

Prepare a structured discovery summary containing:

1. Project overview.
2. Problem statement.
3. Target users.
4. User goals and expected workflows.
5. Functional requirements.
6. Non-functional requirements.
7. MVP scope.
8. Future features.
9. Out-of-scope functionality.
10. Constraints.
11. Confirmed requirements and assumptions.
12. External dependency findings.
13. Risks and open questions.
14. Acceptance criteria.

## 10. Handoff

Provide discovery results to the architecture-design and implementation-planning skills.

Clearly communicate:

- Confirmed requirements.
- Unresolved questions.
- Feasibility findings.
- Platform restrictions.
- MVP boundaries.
- Major technical risks.

Do not begin major implementation merely because discovery is complete.

Architecture decisions must be based on discovery findings rather than assumptions.

## Completion Criteria

Project discovery is complete when:

- The problem is understood.
- Target users are identified.
- Core requirements are documented.
- MVP scope is defined.
- Important constraints are recorded.
- External dependencies have been assessed.
- Critical unknowns are identified.
- Acceptance criteria are established.
- The results are ready for architecture design.