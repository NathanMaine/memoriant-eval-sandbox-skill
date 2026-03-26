from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Role:
    name: str
    description: str = ""


@dataclass
class Step:
    id: str
    goal: str


@dataclass
class Scenario:
    id: str
    title: str
    description: str
    roles: List[Role] = field(default_factory=list)
    steps: List[Step] = field(default_factory=list)


@dataclass
class RunRecord:
    run_id: str
    scenario_id: str
    scenario_title: str
    summary: str
    steps: List[dict]
    outputs: dict
    started_at: str
    completed_at: str
    success: bool = True
    notes: Optional[str] = None
