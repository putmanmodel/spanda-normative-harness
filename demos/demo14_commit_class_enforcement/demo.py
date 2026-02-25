"""
Demo14: Commit Class Enforcement (N20)

Invariant:
Canonical and associative memory writes remain distinct.
Canonical writes require explicit promotion.
"""


def run(fixture: dict) -> dict:
    commit_class = str(fixture["commit_class"])
    promotion_explicit = bool(fixture["promotion_explicit"])

    if commit_class == "ASSOCIATIVE":
        allowed = True
        decision = "ALLOW_ASSOCIATIVE_WRITE"
    elif commit_class == "CANONICAL":
        allowed = promotion_explicit is True
        if allowed:
            decision = "ALLOW_CANONICAL_WRITE"
        else:
            decision = "REJECT_CANONICAL_NO_PROMOTION"
    else:
        allowed = False
        decision = "REJECT_CANONICAL_NO_PROMOTION"

    expected_allowed = bool(fixture["expected_allowed"])
    passed = (allowed == expected_allowed)

    rationale = (
        f"commit_class={commit_class}; promotion_explicit={promotion_explicit}; allowed={allowed}"
    )

    evidence = [
        f"commit_class:{commit_class}",
        f"promotion_explicit:{str(promotion_explicit).lower()}",
        f"allowed:{str(allowed).lower()}",
    ]

    return {
        "normative_ids": ["N20"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
