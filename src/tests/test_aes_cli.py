import json
import sys
from pathlib import Path

# Allow running tests without installing the package globally
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
sys.path.append(str(SRC_ROOT))

from aes.cli import main  # noqa: E402


def test_run_creates_outputs(tmp_path):
    scenario = Path(__file__).parent / "fixtures" / "example.yaml"
    out_dir = tmp_path / "out"

    exit_code = main(["run", "--scenario", str(scenario), "--out", str(out_dir)])

    assert exit_code == 0
    run_files = list((out_dir / "runs").glob("*.json"))
    assert run_files, "expected a run artifact"

    evidence = out_dir / "evidence.jsonl"
    assert evidence.exists()

    data = json.loads(run_files[0].read_text())
    assert data["steps"], "steps should be recorded"
    assert data["success"] is True
