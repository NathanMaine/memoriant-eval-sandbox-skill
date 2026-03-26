# Dark Factory Scenarios

> *"Code must not be written by humans. Code must not be reviewed by humans."*  
> — StrongDM Software Factory Charter, July 2025

This directory contains holdout scenario sets for validating **dark factory** — Level 5 autonomous software production — agent behavior.

## What Is a Dark Factory Scenario?

In February 2026, StrongDM published their [Software Factory manifesto](https://factory.strongdm.ai/), documenting the most advanced lights-out software production system publicly described. Their core architectural insight:

**Agents will write `return true` to pass tests they can see.**

The solution: scenarios stored *outside* the codebase — holdout sets the agent never sees during development. The Judge evaluates against these hidden criteria after the fact. You can't game what you can't see.

This is the same principle machine learning uses to prevent overfitting: the evaluation set is held out from training.

AES independently arrived at this architecture. The Doer/Judge/Adversary/Observer pattern maps directly to the factory's evaluation needs:

| AES Role | Dark Factory Function |
|---|---|
| **Doer** | The autonomous factory agent — builds, iterates, converges without human review |
| **Judge** | LLM-as-judge — evaluates probabilistic satisfaction across real user trajectories |
| **Adversary** | Red team / fault injector — tests recovery, edge cases, reward-hacking resistance |
| **Observer** | Append-only audit logger — tamper-evident evidence for every factory decision |

## Scenarios in This Directory

### [`dark-factory-fault-escalation.yaml`](./dark-factory-fault-escalation.yaml)
Validates autonomous fault detection → retry → circuit breaker → escalation → recovery — with full tamper-evident audit trail. The factory must stay running and explainable with no human in the loop.

### [`dark-factory-spec-satisfaction.yaml`](./dark-factory-spec-satisfaction.yaml)
Validates the core anti-reward-hacking mechanism: agent builds against spec, Judge evaluates against hidden user trajectories. Satisfaction scored probabilistically — not boolean. Catches `return true` class shortcuts.

### [`dark-factory-digital-twin.yaml`](./dark-factory-digital-twin.yaml)
Validates Digital Twin Universe fidelity and agent behavior against behavioral clones of external services. Zero live production API calls during development cycle. Adversary injects production-class failure modes the twin must faithfully reproduce.

## Satisfaction Scoring

Following StrongDM's approach, these scenarios use **probabilistic satisfaction** rather than boolean pass/fail:

```
satisfaction = (satisfied_trajectories + 0.5 * partial_trajectories) / total_trajectories
```

Threshold: **≥ 0.85** to consider a factory run shippable.

This prevents narrow test gaming. The agent builds the software. The Judge evaluates whether a real user would be satisfied. The agent never sees the evaluation criteria.

## Running Against These Scenarios

```bash
# Clone and setup
git clone https://github.com/NathanMaine/agentic-evaluation-sandbox.git
cd agentic-evaluation-sandbox
pip install -e .

# Run a dark factory scenario
aes run --scenario scenarios/dark-factory-fault-escalation.yaml --out out/

# Run all dark factory scenarios
for f in scenarios/dark-factory-*.yaml; do
  aes run --scenario "$f" --out "out/$(basename $f .yaml)/"
done
```

Output per run:
- `out/runs/<run_id>.json` — full run record with step-by-step satisfaction scores
- `out/evidence.jsonl` — append-only audit log with integrity hashes

## The Architecture Connection

StrongDM's factory validated through their Digital Twin Universe — behavioral clones of Okta, Jira, Slack, Google Docs, Drive, and Sheets — running thousands of scenarios per hour without rate limits or production risk.

AES provides the evaluation harness that sits *around* any factory implementation:

```
Specification
     │
     ▼
┌─────────────┐     ┌──────────────────────────┐
│   Factory   │────►│  AES Evaluation Harness  │
│   (Doer)    │     │  Judge / Adversary /     │
│             │     │  Observer                │
└─────────────┘     └──────────┬───────────────┘
                               │
                    ┌──────────▼───────────────┐
                    │  Holdout Scenarios        │
                    │  (agent never sees these) │
                    └───────────────────────────┘
                               │
                    ┌──────────▼───────────────┐
                    │  Satisfaction Score       │
                    │  Evidence Audit Trail     │
                    └───────────────────────────┘
```

The factory builds. AES validates. Humans evaluate outcomes — not code.

## References

- [StrongDM Software Factory](https://factory.strongdm.ai/) — Justin McCarthy, Jay Taylor, Navan Chauhan
- [How StrongDM's AI team build serious software without even looking at the code](https://simonwillison.net/2026/Feb/7/software-factory/) — Simon Willison
- [Five Levels from Spicy Autocomplete to the Software Factory](https://www.danshapiro.com/blog/2026/02/you-dont-write-the-code/) — Dan Shapiro
- [github.com/strongdm/attractor](https://github.com/strongdm/attractor) — StrongDM's open-source factory agent

---

*Built by [Nathan Maine](https://nathanmaine.com) · [github.com/NathanMaine](https://github.com/NathanMaine)*
