# 🎟️ Ticket Radar

**Never miss the moment ticket bookings open.**

Ticket Radar is a movie ticket availability monitoring system designed to track advance booking releases, showtime announcements, screening formats, and seat availability across supported ticket-booking platforms.

The initial focus is on monitoring *Avengers: Doomsday* in Hyderabad, helping users identify booking opportunities and find desirable seats and premium screening experiences before they sell out.

## 🎯 Project Vision

Movie tickets for highly anticipated releases can become available with little notice. Popular shows, premium formats, and desirable seats may sell out quickly.

Ticket Radar aims to solve this problem through automated monitoring and timely notifications, allowing users to make informed booking decisions without repeatedly checking multiple platforms.

## ✨ Planned Features

### 1. Booking Release Monitoring
- Monitor supported platforms for advance booking announcements.
- Detect when bookings become available.
- Notify users when a monitored movie opens for booking.

### 2. Showtime Monitoring
- Detect newly announced showtimes.
- Track show availability across supported cinemas.
- Identify changes in screening schedules.

### 3. Premium Format Monitoring
Track availability of screening formats such as:
- IMAX
- Dolby Atmos
- 4DX
- Standard

### 4. Seat Availability Monitoring
- Monitor available seats for selected shows where supported.
- Identify desirable available seating options.
- Detect relevant availability changes.

### 5. Notifications
- Telegram notifications for important booking and availability updates.
- Avoid duplicate notifications for unchanged information.

### 6. Monitoring Dashboard
A web dashboard is planned to provide:
- Movie and cinema monitoring configuration.
- Monitoring status.
- Booking and showtime updates.
- Seat and format availability.
- Event history.

## 🌐 Initial Platform Scope

The initial monitoring targets are:

| Platform | Status |
|---|---|
| BookMyShow | Planned |
| PVR / INOX | Planned |

**Initial monitoring location:** Hyderabad, India.

Platform access methods, data availability, and permitted monitoring approaches will be investigated before implementation. The project will respect platform terms, access restrictions, and reasonable request limits.

## 🏗️ Proposed Technology Stack

The following technologies are initial architectural candidates, not finalized implementation decisions.

| Component | Proposed Technology |
|---|---|
| Backend | Python, FastAPI |
| Browser Automation | Playwright |
| HTML Parsing | BeautifulSoup |
| Scheduling | APScheduler |
| Database | SQLite initially |
| Frontend | React, Vite |
| Notifications | Telegram Bot API |
| API Communication | REST |

The final stack and architecture will be established during the project discovery and architecture phases.

## ⚙️ How It Is Expected to Work

1. The user configures a movie, location, platforms, and monitoring preferences.
2. The monitoring system periodically checks supported sources.
3. Platform-specific adapters collect relevant booking and availability information.
4. The system compares newly collected information with previously stored snapshots.
5. Relevant changes generate events.
6. Telegram notifications inform the user about important updates.
7. The dashboard presents monitoring status and event history.

## 🔐 Project Principles

- **Human-controlled booking:** Ticket Radar will notify users but will not automatically purchase tickets or make payments.
- **Responsible monitoring:** Respect platform terms, rate limits, authentication requirements, and access restrictions.
- **Modular architecture:** Keep platform-specific monitoring logic separate.
- **Reliable notifications:** Detect meaningful changes and avoid duplicate alerts.
- **Maintainability:** Document architectural decisions, implementation progress, and verification results.
- **Verified development:** Features are considered complete only after appropriate testing and verification.

## 🧠 Development Approach

Ticket Radar is being developed using the **Foundation autonomous engineering framework**.

Foundation provides the reusable engineering standards, project workflows, specialist agents, documentation templates, and verification practices that will guide development.

The goal is to use Ticket Radar as a real-world project to validate and improve Foundation's autonomous engineering capabilities.

## 📁 Repository Structure

This repository inherits the initial engineering structure from Foundation.

```text
ticket_radar/
├── .agents/
│   ├── agents/
│   ├── rules/
│   └── skills/
├── docs/
│   ├── architecture/
│   ├── guides/
│   ├── standards/
│   └── Project_Notes.md
├── scripts/
├── templates/
├── workflows/
├── AGENTS.md
├── README.md
└── LICENSE
```

Application-specific source directories will be introduced during implementation.

## 🚧 Current Project Status

<ins>Phase 0 — Repository Initialization and Project Discovery</ins>

- [x] Create the Ticket Radar GitHub repository.
- [x] Clone the repository locally.
- [x] Transfer the Foundation engineering baseline.
- [ ] Replace Foundation-specific project documentation.
- [ ] Establish Ticket Radar requirements.
- [ ] Research platform access and monitoring feasibility.
- [ ] Finalize architecture and technology choices.
- [ ] Create the implementation roadmap.

**Current status:** Repository initialization and documentation.

No application implementation is considered complete at this stage.

## 🔮 Long-Term Goal

Build a reliable, extensible movie ticket monitoring platform that can monitor multiple movies, cinemas, locations, and ticket-booking platforms while delivering timely and useful availability notifications.

---

*Ticket Radar — Be ready when the tickets drop.*