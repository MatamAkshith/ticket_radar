
---
trigger: always_on
description: Database architecture, schema design, migrations and data integrity.
---

# Database Standards

## General Principles

- Understand the existing database schema before making changes.
- Design schemas with clear relationships and constraints.
- Use appropriate primary and foreign keys.
- Maintain data integrity.
- Use migrations for schema changes where appropriate.
- Review migrations before applying them.
- Avoid unnecessary database queries.
- Consider indexing for frequently queried fields.
- Use transactions when multiple operations must succeed together.
- Apply appropriate database access controls.
- Never reset, truncate or delete production data without explicit approval.
- Test important database operations.

## Schema Design

- Use meaningful table and column names.
- Define appropriate uniqueness and integrity constraints.
- Avoid unnecessary duplication.
- Model relationships explicitly.
- Consider query patterns when designing schemas.
- Distinguish persistent entities from time-dependent observations.
- Store timestamps consistently and handle time zones appropriately.

## Ticket Radar Data Standards

### Historical Monitoring Observations

- Treat availability information as time-dependent observations.
- Preserve observation timestamps.
- Associate observations with their source platform and relevant show.
- Avoid overwriting historical observations when they are required for change detection.
- Distinguish confirmed availability from unknown, unavailable or failed observations.
- Never interpret missing information as confirmed unavailability.

### Snapshot Consistency

- Maintain consistent relationships between shows and availability snapshots.
- Prevent duplicate observations where uniqueness constraints are appropriate.
- Ensure repeated monitoring executions do not corrupt historical records.
- Use transactions when snapshot persistence and related event generation must remain consistent.

### Event Integrity

- Associate monitoring events with the relevant observation or change.
- Prevent duplicate event generation through appropriate constraints and idempotent operations.
- Preserve event timestamps and source information.
- Avoid creating availability events from failed monitoring attempts.

### Notification Records

- Maintain appropriate relationships between events and notifications.
- Track delivery status where required.
- Prevent duplicate notification records.
- Never store Telegram bot tokens or other credentials in ordinary database records.

## Migration Standards

- Review existing migrations before making changes.
- Prefer reversible migrations where practical.
- Test migrations in development environments.
- Review the impact of migrations on historical monitoring data.
- Avoid destructive schema changes without approval.
- Never reset, truncate or delete production data without explicit approval.
- Document significant schema changes.

## Query Performance

- Avoid unnecessary database queries.
- Consider indexes for frequently queried fields.
- Use pagination for large result sets.
- Avoid unbounded queries over historical monitoring data.
- Measure performance before introducing complex optimizations.
- Evaluate archival or retention strategies when justified by actual data growth.

## Data Retention

- Define retention requirements before deleting historical observations.
- Preserve data required for event history and monitoring reliability.
- Do not introduce automatic deletion without an approved retention policy.
- Document archival and cleanup procedures.

## Security

- Apply appropriate database access controls.
- Protect sensitive information.
- Never expose database credentials.
- Follow least-privilege access.
- Avoid storing unnecessary personal information.
- Never use production administrative access unnecessarily.

## Testing

- Test important database operations.
- Verify schema migrations.
- Test relationships and constraints.
- Verify transaction behavior.
- Test uniqueness and duplicate prevention.
- Verify historical observation preservation.
- Test concurrent writes where relevant.
- Validate database access policies.
