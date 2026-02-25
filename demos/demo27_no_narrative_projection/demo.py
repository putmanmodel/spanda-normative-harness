"""
Demo27: No Narrative Projection (N02)

Invariant:
Do not attribute intention/agency/purpose without invariant support.
Unsupported attribution is flagged as projection.
"""


def run(fixture: dict) -> dict:
    hypothesis = str(fixture["hypothesis"])
    invariant_support = bool(fixture["invariant_support"])

    if invariant_support:
        accepted = True
        flagged_projection = False
        decision = "ACCEPT_HYPOTHESIS"
    else:
        accepted = False
        flagged_projection = True
        decision = "FLAG_PROJECTION"

    expected_accepted = bool(fixture["expected_accepted"])
    expected_flagged_projection = bool(fixture["expected_flagged_projection"])

    passed = (
        accepted == expected_accepted
        and flagged_projection == expected_flagged_projection
    )

    rationale = (
        f"hypothesis={hypothesis}; invariant_support={invariant_support}; "
        f"accepted={accepted}; flagged_projection={flagged_projection}"
    )

    evidence = [
        f"hypothesis:{hypothesis}",
        f"invariant_support:{str(invariant_support).lower()}",
        f"accepted:{str(accepted).lower()}",
        f"flagged_projection:{str(flagged_projection).lower()}",
    ]

    return {
        "normative_ids": ["N02"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
