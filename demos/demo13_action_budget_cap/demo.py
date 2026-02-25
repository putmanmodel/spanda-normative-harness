"""
Demo13: Action Budget Cap (N26)

Invariant:
Action execution per cycle must stay within budget_cap.
Requests above budget are clamped.
"""


def run(fixture: dict) -> dict:
    requested_actions = [str(x) for x in fixture["requested_actions"]]
    budget_cap = int(fixture["budget_cap"])

    requested_count = len(requested_actions)

    if requested_count <= budget_cap:
        executed_count = requested_count
        clamped = False
    else:
        executed_count = budget_cap
        clamped = True

    expected_executed_count = int(fixture["expected_executed_count"])
    expected_clamped = bool(fixture["expected_clamped"])

    passed = (executed_count == expected_executed_count) and (clamped == expected_clamped)
    decision = "EXECUTE_WITHIN_BUDGET" if not clamped else "CLAMP_ACTIONS_TO_BUDGET"

    rationale = (
        f"requested_count={requested_count}; budget_cap={budget_cap}; "
        f"executed_count={executed_count}; clamped={clamped}"
    )

    evidence = [
        f"requested_count:{requested_count}",
        f"budget_cap:{budget_cap}",
        f"executed_count:{executed_count}",
        f"clamped:{str(clamped).lower()}",
    ]

    return {
        "normative_ids": ["N26"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
