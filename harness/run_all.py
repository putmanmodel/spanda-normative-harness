#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path


def list_demos(repo_root: Path) -> list[str]:
    demos_dir = repo_root / "demos"
    demos = sorted([p.name for p in demos_dir.iterdir() if p.is_dir() and p.name.startswith("demo")])
    return demos


def run_demo(python_exe: str, repo_root: Path, demo: str, mode: str) -> int:
    cmd = [python_exe, str(repo_root / "harness" / "run_demo.py"), "--demo", demo, "--mode", mode]
    print("\n$ " + " ".join(cmd))
    p = subprocess.run(cmd)
    return p.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Run all Spanda normative harness demos (proof + break).")
    parser.add_argument("--mode", choices=["proof", "break", "both"], default="both")
    parser.add_argument("--phase1", action="store_true", help="Run only Phase 1 starter demos.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    python_exe = sys.executable

    phase1 = [
        "demo01_constraint_boundary",
        "demo02_pressure_viscosity_assimilation",
        "demo03_reflex_non_persistent",
        "demo04_guarded_update_freeze",
    ]

    demos = phase1 if args.phase1 else list_demos(repo_root)

    modes = ["proof", "break"] if args.mode == "both" else [args.mode]

    failures = 0
    for demo in demos:
        for mode in modes:
            rc = run_demo(python_exe, repo_root, demo, mode)
            if rc != 0:
                failures += 1
                print(f"[FAIL] {demo} {mode} (rc={rc})")

    if failures == 0:
        print(f"\n[ALL OK] Ran {len(demos)} demos × {len(modes)} mode(s) with no failures.")
        return 0

    print(f"\n[DONE] Failures: {failures}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())