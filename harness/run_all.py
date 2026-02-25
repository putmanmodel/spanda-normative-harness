import subprocess
import sys
from pathlib import Path

PHASE1 = [
    "demo01_constraint_boundary",
    "demo02_pressure_viscosity_assimilation",
    "demo03_reflex_non_persistent",
    "demo04_guarded_update_freeze",
]

def run_demo(python_exe: str, demo: str, mode: str) -> int:
    cmd = [python_exe, "harness/run_demo.py", "--demo", demo, "--mode", mode]
    print("\n$ " + " ".join(cmd))
    p = subprocess.run(cmd)
    return p.returncode

def main():
    repo_root = Path(__file__).resolve().parents[1]
    python_exe = sys.executable
    failures = 0

    for demo in PHASE1:
        for mode in ("proof", "break"):
            rc = run_demo(python_exe, demo, mode)
            if rc != 0:
                failures += 1
                print(f"[FAIL] {demo} {mode} (rc={rc})")

    if failures == 0:
        print("\n[ALL OK] Phase 1 demos ran clean.")
        raise SystemExit(0)

    print(f"\n[DONE] Failures: {failures}")
    raise SystemExit(1)

if __name__ == "__main__":
    main()
