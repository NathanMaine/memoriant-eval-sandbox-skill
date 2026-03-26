from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from .models import Role, Scenario, Step

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    yaml = None


def _read_structured_file(path: Path) -> Dict[str, Any]:
    text = path.read_text()
    if path.suffix.lower() in {".yaml", ".yml"} and yaml is not None:
        return yaml.safe_load(text)  # pragma: no cover - exercised when PyYAML present
    # Fallback to JSON for both .json and simple YAML-as-JSON cases
    return json.loads(text)


def load_scenario(path: Path) -> Scenario:
    data = _read_structured_file(path)
    if not isinstance(data, dict):
        raise ValueError("Scenario file must contain a JSON/YAML object")

    scenario_id = str(data.get("id", "scenario"))
    title = str(data.get("title", "Untitled Scenario"))
    description = str(data.get("description", ""))

    roles_data: List[dict] = data.get("roles", []) or []
    steps_data: List[dict] = data.get("steps", []) or []

    roles = [Role(name=str(r.get("name", "Role")), description=str(r.get("description", ""))) for r in roles_data]
    steps = [Step(id=str(s.get("id", f"step-{i}")), goal=str(s.get("goal", ""))) for i, s in enumerate(steps_data, start=1)]

    if not steps:
        raise ValueError("Scenario must include at least one step")

    return Scenario(id=scenario_id, title=title, description=description, roles=roles, steps=steps)
