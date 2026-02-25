"""
Demo22: Drift Inputs Must Be Accessible (N13)

Invariant:
Drift detection must use only interaction-accessible inputs.
"""


def run(fixture: dict) -> dict:
    inputs = list(fixture["inputs"])
    drift_decision_requested = bool(fixture["drift_decision_requested"])

    blocked = [str(inp["name"]) for inp in inputs if not bool(inp.get("accessible", False))]

    if not drift_decision_requested:
        allowed = True
        blocked = []
    else:
        allowed = len(blocked) == 0

    expected_allowed = bool(fixture["expected_allowed"])
    expected_blocked_inputs = sorted([str(x) for x in fixture["expected_blocked_inputs"]])

    passed = (allowed == expected_allowed) and (sorted(blocked) == expected_blocked_inputs)

    decision = "ALLOW_DRIFT_DECISION" if allowed else "REJECT_DRIFT_USES_INACCESSIBLE_INPUTS"

    blocked_repr = "none" if len(blocked) == 0 else ",".join(blocked)

    rationale = (
        f"drift_decision_requested={drift_decision_requested}; blocked={sorted(blocked)}; "
        f"allowed={allowed}"
    )

    evidence = [
        f"drift_decision_requested:{str(drift_decision_requested).lower()}",
        f"blocked_inputs:{blocked_repr}",
        f"allowed:{str(allowed).lower()}",
    ]

    return {
        "normative_ids": ["N13"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
