from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Tuple

from .models import RunRecord, Scenario


def simulate_run(scenario: Scenario, run_id: str | None = None) -> RunRecord:
    started_at = datetime.now(timezone.utc)
    generated_run_id = run_id or str(uuid.uuid4())

    events = []
    for step in scenario.steps:
        doer_action = f"doer: completed goal '{step.goal}'"
        judge_action = f"judge: approved '{step.id}'"
        events.append({
            "step_id": step.id,
            "goal": step.goal,
            "doer": doer_action,
            "judge": judge_action,
        })

    summary = f"Executed {len(events)} steps with stubbed Doer/Judge"
    outputs = {
        "score": {
            "success": True,
            "reason": "deterministic stub",
        }
    }

    completed_at = datetime.now(timezone.utc)
    return RunRecord(
        run_id=generated_run_id,
        scenario_id=scenario.id,
        scenario_title=scenario.title,
        summary=summary,
        steps=events,
        outputs=outputs,
        started_at=started_at.isoformat(),
        completed_at=completed_at.isoformat(),
        success=True,
        notes=None,
    )
