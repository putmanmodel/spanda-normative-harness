"""
Demo15: Recall Attention Only (N27)

Invariant:
Recall is attention-only and must not mutate state or authorize side effects.
"""


def run(fixture: dict) -> dict:
    recall_triggered = bool(fixture["recall_triggered"])
    attempted = dict(fixture.get("attempted", {}))
    state_before = dict(fixture["state_before"])

    canonical_memory_write = bool(attempted.get("canonical_memory_write", False))
    baseline_update = bool(attempted.get("baseline_update", False))
    prior_update = bool(attempted.get("prior_update", False))
    irreversible_action = bool(attempted.get("irreversible_action", False))

    attempted_mutation = (
        canonical_memory_write
        or baseline_update
        or prior_update
        or irreversible_action
    )

    if not recall_triggered:
        allowed = True
        state_after = dict(state_before)
    else:
        if attempted_mutation:
            allowed = False
            state_after = dict(state_before)
        else:
            allowed = True
            state_after = dict(state_before)

    expected_allowed = bool(fixture["expected_allowed"])
    expected_state_after = dict(fixture["expected_state_after"])

    passed = (allowed == expected_allowed) and (state_after == expected_state_after)
    decision = "RECALL_OK_NO_MUTATION" if allowed else "RECALL_VIOLATION_REJECTED"

    rationale = (
        f"recall_triggered={recall_triggered}; attempted_mutation={attempted_mutation}; "
        f"allowed={allowed}; state_keys={sorted(list(state_after.keys()))}"
    )

    evidence = [
        f"recall_triggered:{str(recall_triggered).lower()}",
        f"attempted_mutation:{str(attempted_mutation).lower()}",
        f"allowed:{str(allowed).lower()}",
    ]

    return {
        "normative_ids": ["N27"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
