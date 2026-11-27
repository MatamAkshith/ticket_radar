
---
trigger: always_on
description: Testing, verification and software quality assurance standards.
---

# Testing Standards

## General Testing Principles

- Identify acceptance criteria before implementation.
- Write tests for important functionality.
- Include edge cases and error scenarios.
- Run relevant tests after changes.
- Run integration tests when components interact.
- Verify application builds where applicable.
- Test important user journeys.
- Investigate failures instead of hiding or bypassing them.
- Never fabricate test results.
- Report skipped, failed and unavailable tests.
- Do not claim completion without appropriate verification.

## Testing Levels

Consider the appropriate combination of:

- Unit testing.
- Integration testing.
- API testing.
- Database testing.
- Frontend and UI testing.
- End-to-end testing.
- Regression testing.
- Performance testing where relevant.
- Security testing where authorized.

## Monitoring System Testing

Ticket Radar must be tested for its core monitoring behavior.

Validate:

- Booking release detection.
- Showtime discovery and changes.
- Screening format identification.
- Seat availability changes where supported.
- Snapshot comparison.
- Event generation.
- Duplicate-event prevention.
- Monitoring execution status.
- Historical observation preservation.

## Change Detection Testing

Use controlled and repeatable test data to verify:

- Unchanged observations do not create unnecessary events.
- Meaningful changes generate the correct events.
- Repeated observations do not create duplicate records.
- Missing data is not interpreted as confirmed unavailability.
- Failed monitoring executions do not generate false availability changes.
- Observation timestamps and data freshness are handled correctly.

## External Integration Testing

- Test platform adapters using controlled fixtures and mocks.
- Verify permitted external integrations separately from internal application logic.
- Test malformed and incomplete responses.
- Test timeouts and network failures.
- Verify bounded retry behavior.
- Ensure one unavailable source does not unnecessarily interrupt other monitoring operations.
- Do not perform aggressive or unauthorized live platform testing.
- Never claim live platform integration has been verified when only mocked responses were tested.

## Notification Testing

Verify:

- Correct event-to-notification mapping.
- Telegram notification generation.
- Duplicate notification prevention.
- Delivery failure handling.
- Retry behavior.
- Accurate notification delivery status.
- Protection of notification credentials.

## Frontend and API Verification

- Test important user interactions.
- Verify API request and response contracts.
- Test loading, empty, error and stale-data states.
- Verify that unavailable information is not presented as current.
- Test dashboard behavior with partial or failed API responses.

## Reliability Testing

Where appropriate, test:

- Concurrent monitoring jobs.
- Scheduler failures.
- Database failures.
- Network interruptions.
- Recovery after temporary failures.
- Repeated executions.
- Background task failures.

## Verification Evidence

For important verification activities, record:

- Test scenario.
- Expected result.
- Actual result.
- Execution status.
- Relevant test output or evidence.
- Known limitations.

Use clear result classifications:

- Passed.
- Failed.
- Skipped.
- Blocked.
- Not tested.

## Completion Requirements

- Run relevant tests after implementation.
- Verify affected integration points.
- Run regression tests when necessary.
- Review failures and unresolved issues.
- Update documentation with actual results.
- Never silently weaken tests to make an implementation pass.
- Do not claim functionality is complete without sufficient evidence.
