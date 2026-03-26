# Security Policy

## What This Plugin Does

This plugin consists entirely of markdown instruction files (SKILL.md and agent .md files). It contains:
- No executable code
- No shell scripts
- No network calls
- No file system modifications beyond what Claude Code normally does

All operations (writing run records, appending audit trail JSONL, reading scenario files) are performed by Claude Code itself using its standard tools, not by any code in this plugin.

## Adversarial Scenario Content

This plugin instructs Claude Code to generate adversarial prompts as part of evaluation scenarios. These prompts are generated in the context of testing AI guardrails — not to cause harm. The adversarial content is:
- Generated only on explicit user request
- Used only within the evaluation simulation context
- Never transmitted to external systems by this plugin

## Audit Trail Handling

The JSONL audit trail written by this skill:
- Contains only run metadata (timestamps, scenario IDs, verdicts, scores) — no raw agent outputs
- Is written in append-only mode
- Uses a hash chain for tamper detection — the chain is local to the user's environment

## Reporting a Vulnerability

If you discover a security issue, please email nathan@memoriant.com (do not open a public issue).

We will respond within 48 hours and provide a fix timeline.

## Auditing This Plugin

This plugin is easy to audit:
1. All files are markdown — readable in any text editor
2. No `node_modules`, no Python packages, no compiled binaries
3. Review `skills/eval-sandbox/SKILL.md` to see exactly what instructions are given to the AI
