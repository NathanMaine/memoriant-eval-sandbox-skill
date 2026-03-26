from __future__ import annotations

import json
from pathlib import Path

from .models import RunRecord


def ensure_out_dirs(out_dir: Path) -> tuple[Path, Path]:
    runs_dir = out_dir / "runs"
    runs_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir, runs_dir


def write_run_artifacts(run: RunRecord, out_dir: Path) -> tuple[Path, Path]:
    out_dir, runs_dir = ensure_out_dirs(out_dir)
    run_path = runs_dir / f"{run.run_id}.json"
    run_path.write_text(json.dumps(run.__dict__, indent=2))

    evidence_path = out_dir / "evidence.jsonl"
    with evidence_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "run_id": run.run_id,
            "scenario_id": run.scenario_id,
            "summary": run.summary,
            "success": run.success,
            "outputs": run.outputs,
        }) + "\n")

    return run_path, evidence_path
