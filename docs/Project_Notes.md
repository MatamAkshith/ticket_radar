# Ticket Radar — Project Notes

> Central source of truth for project context, architecture, development progress and technical decisions. Update this document whenever a meaningful project decision, implementation or verification occurs.

## 1. Project Overview

- **Project Name:** Ticket Radar
- **Project Purpose:** Build a movie ticket availability monitoring system that detects booking releases, new showtimes, screening formats and seat availability, then notifies users about relevant changes.
- **Problem Being Solved:** Moviegoers currently need to repeatedly check multiple ticket-booking platforms to discover when bookings open or desirable seats and premium screening formats become available. Popular shows and seats may sell out quickly.
- **Target Users:** Moviegoers who want timely information about booking releases, showtimes and ticket availability.
- **Initial Movie:** Avengers: Doomsday
- **Initial Location:** Hyderabad, India
- **Current Version:** Initial project setup — no application implementation yet.

### Initial Platform Scope

- BookMyShow
- PVR / INOX

### Confirmed User Requirements

1. Monitor advance booking releases.
2. Detect newly announced showtimes.
3. Track screening formats:
   - IMAX
   - Dolby Atmos
   - 4DX
   - Standard
4. Monitor seat availability where technically and legitimately possible.
5. Identify desirable available seats without requiring a fixed seat number.
6. Send notifications through Telegram.
7. Provide a web dashboard for monitoring configuration, status and event history.

### Project Boundaries

- Ticket Radar will notify users; it will not automatically book tickets or make payments.
- Platform access must respect applicable terms, access restrictions and reasonable request limits.
- CAPTCHA, authentication and anti-bot protections must not be bypassed.
- Monitoring capabilities must be based on verified data availability and permitted access methods.

## 2. Current Development Status

- **Current Phase:** Phase 0 — Repository Initialization and Project Discovery.
- **Current Milestone:** Project-specific documentation and engineering environment setup.
- **Current Development State:** Foundation baseline transferred into the Ticket Radar repository. README updated. Project Notes being customized.
- **Last Updated:** 2026-11-27

### Current Progress

- [x] Create Ticket Radar GitHub repository.
- [x] Clone repository locally.
- [x] Transfer Foundation baseline.
- [x] Preserve Ticket Radar repository Git configuration.
- [x] Update project README.
- [ ] Complete Project Notes.
- [ ] Audit inherited Foundation configuration.
- [ ] Establish product requirements.
- [ ] Research platform feasibility.
- [ ] Finalize system architecture.
- [ ] Establish implementation roadmap.

## 3. Technology Stack

The following is the initially proposed stack. These choices are not finalized and must be evaluated during architecture design and platform feasibility research.

| Component | Proposed Technology | Status |
|---|---|---|
| Frontend | React + Vite | Proposed |
| Backend | Python + FastAPI | Proposed |
| Browser Automation | Playwright | Proposed |
| HTML Parsing | BeautifulSoup | Proposed |
| Background Scheduling | APScheduler | Proposed |
| Database | SQLite initially | Proposed |
| Notifications | Telegram Bot API | Required integration; implementation pending |
| API Communication | REST | Proposed |
| Deployment | To be determined | Pending |

### Technology Selection Principles

- Prefer a simple and maintainable architecture.
- Avoid unnecessary infrastructure and external costs.
- Verify platform access before committing to scraping or browser automation.
- Keep monitoring logic modular and independent of the user interface.
- Introduce additional infrastructure only when justified by requirements.

## 4. System Architecture

### Proposed High-Level Components

1. **Frontend Dashboard**
   - Configure movies, locations, cinemas and monitoring preferences.
   - Display monitoring status and detected events.
   - Show relevant booking and availability changes.

2. **Backend API**
   - Manage application configuration.
   - Expose monitoring data to the frontend.
   - Coordinate monitoring operations.

3. **Platform Adapters**
   - Separate integrations for BookMyShow and PVR / INOX.
   - Retrieve permitted and accessible booking information.
   - Normalize platform-specific data into a common format.

4. **Monitoring Scheduler**
   - Trigger periodic monitoring jobs.
   - Manage monitoring intervals.
   - Handle failures and retries responsibly.

5. **Change Detection Engine**
   - Compare newly collected information against stored snapshots.
   - Identify meaningful changes.
   - Prevent duplicate events and notifications.

6. **Notification Service**
   - Send relevant updates through Telegram.
   - Handle notification failures and delivery status.

7. **Database**
   - Store monitored movies, cinemas, shows, availability snapshots, events and user preferences.

### Architecture Status

The above is a conceptual architecture, not an approved implementation design.

Detailed component boundaries, data flows, database relationships and API contracts will be documented after platform feasibility research.

## 5. Project Workflow

### Expected User Workflow

1. User configures a movie and monitoring location.
2. User selects supported platforms and monitoring preferences.
3. Ticket Radar begins monitoring supported sources.
4. The system retrieves available booking information.
5. The system compares new information with previously stored data.
6. Meaningful changes are recorded as events.
7. Telegram notifications are sent when relevant changes occur.
8. The dashboard displays monitoring status and event history.
9. The user visits the ticket-booking platform to complete the booking manually.

### Expected Event Types

- Booking opened.
- New showtime detected.
- Screening format detected.
- Relevant seat availability change.
- Availability change or show removal.
- Monitoring or source failure.

These event types will be refined during requirements and architecture design.

## 6. Database Design

**Status:** Not designed.

Potential entities to investigate during architecture design:

- Movie
- City / Location
- Cinema
- Platform
- Screen / Screening Format
- Show
- Seat Availability Snapshot
- Monitoring Configuration
- Event
- Notification
- Monitoring Execution

The final schema, relationships, constraints and migration strategy must be established before implementation.

## 7. API Design

**Status:** Not designed.

Potential API areas:

- Movie and cinema management.
- Monitoring configuration.
- Monitoring status.
- Showtimes and availability.
- Event history.
- Notification configuration.
- Health and monitoring execution status.

Endpoint names, request and response formats, validation rules and error handling will be documented after architecture design.

## 8. Architecture Decision Log

| Date | Decision | Reason | Impact |
|---|---|---|---|
| 2026-11-27 | Project named Ticket Radar | Establish a dedicated identity for the monitoring application | Repository and project documentation |
| 2026-11-27 | Initial monitoring location is Hyderabad | Establish the initial geographical scope | Platform and cinema discovery |
| 2026-11-27 | Initial platforms are BookMyShow and PVR / INOX | Define the first integration targets | Platform feasibility research |
| 2026-11-27 | Telegram selected for notifications | Provide timely booking and availability updates | Notification integration |
| 2026-11-27 | Automated booking and payment excluded | Keep booking under user control | Application scope and security |
| 2026-11-27 | Foundation will be used as the engineering baseline | Validate the reusable engineering framework on a real project | Development workflow |

## 9. Completed Progress Tracker

| Task ID | Description | Status | Verification |
|---|---|---|---|
| TR-001 | Create GitHub repository | Completed | Repository created |
| TR-002 | Clone repository locally | Completed | Local repository and remote inspected |
| TR-003 | Transfer Foundation baseline | Completed | Directory structure inspected |
| TR-004 | Update README | Completed | User confirmed |
| TR-005 | Customize Project Notes | In Progress | Pending |
| TR-006 | Audit inherited Foundation configuration | Pending | Not started |
| TR-007 | Product requirements discovery | Pending | Not started |
| TR-008 | Platform feasibility research | Pending | Not started |
| TR-009 | Architecture design | Pending | Not started |

## 10. Pending Work

### Repository Initialization
- Complete this Project Notes document.
- Inspect inherited AGENTS.md.
- Audit inherited agents, rules, skills and workflows.
- Identify required Ticket Radar-specific modifications.
- Preserve reusable Foundation capabilities.

### Product Discovery
- Define detailed functional requirements.
- Establish monitoring preferences and configuration.
- Define what constitutes desirable seat availability.
- Define notification triggers and duplicate prevention.
- Identify edge cases and failure scenarios.

### Platform Feasibility
- Investigate permitted access methods for BookMyShow.
- Investigate permitted access methods for PVR / INOX.
- Determine which booking, showtime, format and seat details are accessible.
- Evaluate reliability, rate limits and platform restrictions.
- Document limitations before selecting implementation methods.

### Architecture and Implementation Planning
- Finalize the technology stack.
- Design component architecture.
- Design database schema.
- Define API contracts.
- Define monitoring and change-detection strategies.
- Establish milestones and acceptance criteria.

## 11. Development Log

Maintain a chronological record of meaningful project activities.

### Development Entry Template

**Date:**

**Task / Feature:**

**Objective:**

**Implementation Summary:**

**Files Changed:**

**Architecture Changes:**

**Verification Performed:**

**Results:**

**Git Commit:**

**Issues / Limitations:**

**Next Steps:**

### Initial Development Entry

**Date:** 2026-11-27

**Task / Feature:** Ticket Radar repository initialization.

**Objective:** Establish a project-specific repository using the reusable Foundation engineering baseline.

**Implementation Summary:**
- Created and cloned the Ticket Radar repository.
- Transferred the Foundation directory structure.
- Preserved the Ticket Radar Git repository configuration.
- Replaced the Foundation README with Ticket Radar project documentation.
- Began converting the Foundation Project Notes template into a project-specific source of truth.

**Files Changed:**
- README.md
- docs/Project_Notes.md

**Architecture Changes:** None.

**Verification Performed:**
- Inspected Git remote and repository status.
- Inspected transferred directory structure.
- Confirmed README update.

**Results:** Repository initialization is underway. Application development has not started.

**Git Commit:** Pending.

**Issues / Limitations:** Platform feasibility and technical architecture remain unverified.

**Next Steps:** Complete project documentation, audit Foundation configuration and begin product discovery.

## 12. Important Project References

- **GitHub Repository:** https://github.com/MatamAkshith/ticket_radar
- **Local Repository:** `~/Documents/projects/ticket_radar`
- **Engineering Baseline:** Foundation
- **Initial Monitoring Location:** Hyderabad, India
- **Initial Platforms:** BookMyShow and PVR / INOX
- **Notification Channel:** Telegram

### Documentation References

- `README.md` — Project introduction and overview.
- `AGENTS.md` — Project-level engineering instructions.
- `docs/Project_Notes.md` — Central project source of truth.
- `docs/architecture/` — Architecture documentation.
- `docs/guides/` — Development and operational guides.
- `docs/standards/` — Project engineering standards.

Never store passwords, API keys, bot tokens or private credentials in this document or in version control.
