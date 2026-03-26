# Memoriant Eval Sandbox Skill

Scenario-driven AI agent evaluation skills for coding agents.

## Available Skills

### eval-sandbox
Design and run structured AI agent evaluations with Doer/Judge/Adversary/Observer multi-role simulations. Score satisfaction probabilistically. Generate append-only JSONL audit trails with integrity hash chains. Apply holdout evaluation methodology for regression testing.

Skill file: `skills/eval-sandbox/SKILL.md`

## Available Agents

### eval-sandbox-runner
Agentic evaluation specialist. Designs scenarios, executes multi-role simulations, generates adversarial prompts, scores results on a 0.0–1.0 satisfaction scale, and produces compliance-grade audit evidence.

Agent file: `agents/eval-sandbox-runner.md`

## Usage

### Claude Code
```bash
/install NathanMaine/memoriant-eval-sandbox-skill
/eval-sandbox
```

### OpenAI Codex CLI
```bash
git clone https://github.com/NathanMaine/memoriant-eval-sandbox-skill.git ~/.codex/skills/eval-sandbox
codex --enable skills
```

### Gemini CLI
```bash
gemini extensions install https://github.com/NathanMaine/memoriant-eval-sandbox-skill.git --consent
```
