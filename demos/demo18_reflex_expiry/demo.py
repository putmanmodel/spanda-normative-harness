"""
Demo18: Reflex Expiry (N23)

Invariant:
Reflex events expire automatically unless re-triggered in the short horizon.
"""


def run(fixture: dict) -> dict:
    reflex_active_before = bool(fixture["reflex_active_before"])
    age_steps = int(fixture["age_steps"])
    ttl_steps = int(fixture["ttl_steps"])
    retriggered = bool(fixture["retriggered"])

    if not reflex_active_before:
        reflex_active_after = False
    else:
        if retriggered:
            reflex_active_after = True
        elif age_steps > ttl_steps:
            reflex_active_after = False
        else:
            reflex_active_after = True

    expected_reflex_active_after = bool(fixture["expected_reflex_active_after"])
    passed = (reflex_active_after == expected_reflex_active_after)

    if reflex_active_after:
        decision = "REFLEX_ACTIVE"
    elif reflex_active_before:
        decision = "REFLEX_EXPIRED"
    else:
        decision = "REFLEX_INACTIVE"

    rationale = (
        f"reflex_active_before={reflex_active_before}; age_steps={age_steps}; ttl_steps={ttl_steps}; "
        f"retriggered={retriggered} => reflex_active_after={reflex_active_after}"
    )

    evidence = [
        f"reflex_active_before:{str(reflex_active_before).lower()}",
        f"age_steps:{age_steps}",
        f"ttl_steps:{ttl_steps}",
        f"retriggered:{str(retriggered).lower()}",
        f"reflex_active_after:{str(reflex_active_after).lower()}",
    ]

    return {
        "normative_ids": ["N23"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
