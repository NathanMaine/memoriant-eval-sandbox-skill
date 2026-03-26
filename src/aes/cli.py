from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .evidence import write_run_artifacts
from .loader import load_scenario
from .runner import simulate_run


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="aes", description="Agentic Evaluation Sandbox CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run a scenario with stubbed Doer/Judge")
    run_parser.add_argument("--scenario", required=True, type=Path, help="Path to scenario YAML/JSON file")
    run_parser.add_argument("--out", default=Path("out"), type=Path, help="Output directory (default: out)")
    run_parser.add_argument("--run-id", default=None, help="Optional run identifier")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "run":
        scenario = load_scenario(args.scenario)
        run_record = simulate_run(scenario, run_id=args.run_id)
        run_path, evidence_path = write_run_artifacts(run_record, args.out)
        print(f"Run saved to {run_path}")
        print(f"Evidence appended to {evidence_path}")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
