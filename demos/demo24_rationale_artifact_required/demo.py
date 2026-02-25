"""
Demo24: Rationale Artifact Required (N17)

Invariant:
Governance events must include rationale artifacts for deterministic replay.
"""


def run(fixture: dict) -> dict:
    event_id = str(fixture["event_id"])
    governance_event = bool(fixture["governance_event"])
    rationale_pointers = fixture["rationale_pointers"]

    if not governance_event:
        missing = False
        allowed = True
    else:
        missing = (rationale_pointers is None) or (len(rationale_pointers) == 0)
        allowed = not missing

    expected_allowed = bool(fixture["expected_allowed"])
    expected_missing = bool(fixture["expected_missing"])

    passed = (allowed == expected_allowed) and (missing == expected_missing)

    decision = "ALLOW_GOVERNANCE_EVENT" if allowed else "REJECT_GOVERNANCE_MISSING_RATIONALE"

    rationale_present = not missing
    pointer_count = 0 if rationale_pointers is None else len(rationale_pointers)
    rationale = (
        f"event_id={event_id}; governance_event={governance_event}; "
        f"rationale_pointer_count={pointer_count}; missing={missing}; allowed={allowed}"
    )

    evidence = [
        f"event_id:{event_id}",
        f"governance_event:{str(governance_event).lower()}",
        f"rationale_present:{str(rationale_present).lower()}",
        f"allowed:{str(allowed).lower()}",
    ]

    return {
        "normative_ids": ["N17"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
