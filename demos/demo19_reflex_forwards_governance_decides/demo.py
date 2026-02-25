"""
Demo19: Reflex Forwards, Governance Decides (N24)

Invariant:
Reflex may forward, but governance independently authorizes actions.
"""


def run(fixture: dict) -> dict:
    reflex_triggered = bool(fixture["reflex_triggered"])
    forward_requested = bool(fixture["forward_requested"])
    governance_approved = bool(fixture["governance_approved"])

    forwarded = reflex_triggered and forward_requested
    action_allowed = governance_approved

    if forwarded and action_allowed:
        decision = "FORWARD_AND_ALLOW_ACTION"
    elif forwarded and (not action_allowed):
        decision = "FORWARD_ONLY_GOVERNANCE_PENDING"
    elif (not forwarded) and action_allowed:
        decision = "ALLOW_ACTION_NO_FORWARD"
    else:
        decision = "NO_FORWARD_NO_ACTION"

    expected_forwarded = bool(fixture["expected_forwarded"])
    expected_action_allowed = bool(fixture["expected_action_allowed"])

    passed = (forwarded == expected_forwarded) and (action_allowed == expected_action_allowed)

    rationale = (
        f"reflex_triggered={reflex_triggered}; forward_requested={forward_requested}; "
        f"forwarded={forwarded}; governance_approved={governance_approved}; "
        f"action_allowed={action_allowed}"
    )

    evidence = [
        f"reflex_triggered:{str(reflex_triggered).lower()}",
        f"forward_requested:{str(forward_requested).lower()}",
        f"forwarded:{str(forwarded).lower()}",
        f"governance_approved:{str(governance_approved).lower()}",
        f"action_allowed:{str(action_allowed).lower()}",
    ]

    return {
        "normative_ids": ["N24"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
