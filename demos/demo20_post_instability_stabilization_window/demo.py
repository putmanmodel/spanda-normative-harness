"""
Demo20: Post-Instability Stabilization Window (N30)

Invariant:
After instability, baseline updates are blocked until stabilization window is met.
"""


def run(fixture: dict) -> dict:
    instability_recent = bool(fixture["instability_recent"])
    steps_since_instability = int(fixture["steps_since_instability"])
    stabilization_window = int(fixture["stabilization_window"])
    update_requested = bool(fixture["update_requested"])

    if not update_requested:
        allowed = True
    elif instability_recent and (steps_since_instability < stabilization_window):
        allowed = False
    else:
        allowed = True

    expected_allowed = bool(fixture["expected_allowed"])
    passed = (allowed == expected_allowed)

    decision = "ALLOW_BASELINE_UPDATE" if allowed else "REJECT_UPDATE_STABILIZATION_WINDOW"

    rationale = (
        f"instability_recent={instability_recent}; steps_since_instability={steps_since_instability}; "
        f"stabilization_window={stabilization_window}; update_requested={update_requested}; allowed={allowed}"
    )

    evidence = [
        f"instability_recent:{str(instability_recent).lower()}",
        f"steps_since_instability:{steps_since_instability}",
        f"stabilization_window:{stabilization_window}",
        f"update_requested:{str(update_requested).lower()}",
        f"allowed:{str(allowed).lower()}",
    ]

    return {
        "normative_ids": ["N30"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
