---
trigger: always_on
description: Security, privacy, access control and sensitive-data protection.
---

# Security Standards

## General Security Principles

- Never expose API keys, passwords or secrets.
- Never hardcode sensitive credentials.
- Use environment variables or approved secret-management systems.
- Validate and sanitize untrusted inputs.
- Apply authentication and authorization where required.
- Follow the principle of least privilege.
- Protect sensitive user information.
- Avoid logging passwords, tokens or private data.
- Review dependencies for known security concerns.
- Never disable security controls merely to make tests pass.
- Ask for approval before sensitive or destructive operations.

## External Platform Security

Ticket Radar interacts with external movie ticket-booking platforms.

- Respect applicable platform terms and access restrictions.
- Investigate permitted data access methods before implementation.
- Never bypass authentication, CAPTCHAs or anti-bot protections.
- Do not access unauthorized private endpoints.
- Use reasonable monitoring intervals and request limits.
- Avoid excessive or unnecessary requests.
- Treat external platform responses as untrusted input.
- Validate external data before processing or storing it.
- Do not assume that seat-level availability or other platform data is accessible.
- Document platform-specific security limitations.

## Browser Automation Security

- Protect browser sessions and authentication information.
- Never expose cookies, session tokens or credentials.
- Avoid executing untrusted external content.
- Restrict automation to authorized monitoring activities.
- Do not use browser automation to bypass platform access restrictions.
- Avoid storing unnecessary browser session data.

## Notification Security

Telegram is the initial notification channel.

- Protect Telegram bot tokens and chat configuration.
- Never commit notification credentials.
- Do not expose credentials in application logs or API responses.
- Validate notification configuration.
- Restrict access to notification settings.
- Handle external notification API failures safely.

## Data Protection

- Collect only information necessary for application functionality.
- Avoid storing unnecessary personal information.
- Protect database credentials.
- Apply appropriate access controls.
- Protect stored monitoring and notification records.
- Avoid exposing sensitive information through error messages.
- Ensure sensitive configuration is not included in monitoring logs.

## Monitoring and Automation Security

- Apply reasonable limits to background monitoring jobs.
- Prevent uncontrolled retries and repeated execution.
- Validate data before generating availability events.
- Avoid interpreting failed monitoring attempts as confirmed availability changes.
- Ensure external data cannot trigger arbitrary code execution.
- Protect scheduled jobs and their execution permissions.
- Handle external service failures without weakening security controls.

## Dependency and Infrastructure Security

- Review dependencies for known vulnerabilities.
- Avoid unnecessary dependencies.
- Use secure configuration practices.
- Apply least-privilege permissions.
- Protect database and deployment credentials.
- Review security-sensitive configuration changes.
- Do not expose development or administrative interfaces unintentionally.

## Security Operations

- Perform security reviews before important releases.
- Investigate suspected vulnerabilities.
- Document security findings and remediation.
- Obtain approval before production security testing or sensitive operations.
- Never claim a system is completely secure.