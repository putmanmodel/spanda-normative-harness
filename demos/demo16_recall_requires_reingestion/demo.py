"""
Demo16: Recall Requires Reingestion (N28)

Invariant:
Recall-derived signals must be re-ingested as a new Event before promotion.
"""


def run(fixture: dict) -> dict:
    source = str(fixture["source"])
    reingested = bool(fixture["reingested"])
    promotion_requested = bool(fixture["promotion_requested"])

    if not promotion_requested:
        allowed = True
    else:
        if source == "RECALL" and not reingested:
            allowed = False
        else:
            allowed = True

    expected_allowed = bool(fixture["expected_allowed"])
    passed = (allowed == expected_allowed)

    decision = "ALLOW_PROMOTION" if allowed else "REJECT_PROMOTION_RECALL_NOT_REINGESTED"

    rationale = (
        f"source={source}; reingested={reingested}; promotion_requested={promotion_requested}; "
        f"allowed={allowed}"
    )

    evidence = [
        f"source:{source}",
        f"reingested:{str(reingested).lower()}",
        f"promotion_requested:{str(promotion_requested).lower()}",
        f"allowed:{str(allowed).lower()}",
    ]

    return {
        "normative_ids": ["N28"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
