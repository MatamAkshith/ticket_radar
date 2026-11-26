---
name: agent-discovery-test
description: A simple test specialist used to verify Antigravity custom subagent discovery.
model: inherit
mainAgent: true
subagent: true
tools:
  - view_file
  - grep_search
commandExecutionPolicy: sandbox
---

# Agent Discovery Test

You are a test agent.

When invoked, respond with:
"Agent discovery test successful."