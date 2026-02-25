"""
Demo11: Evidence Supports Decision (N21)

Invariant:
A decision must be supported by its evidence. Contradictions are flagged.
"""


def run(fixture: dict) -> dict:
    claimed_decision = str(fixture["claimed_decision"])
    evidence_in = dict(fixture["evidence"])
    evidence_allowed = bool(evidence_in["allowed"])
    reason = str(evidence_in["reason"])

    if claimed_decision == "ALLOW_ACTION":
        supported = evidence_allowed is True
    elif claimed_decision == "REJECT_ACTION":
        supported = evidence_allowed is False
    else:
        supported = False

    expected_supported = bool(fixture["expected_supported"])
    passed = (supported == expected_supported)

    decision = "EVIDENCE_SUPPORTS_DECISION" if supported else "EVIDENCE_CONTRADICTS_DECISION"

    rationale = (
        f"claimed_decision={claimed_decision}; evidence_allowed={evidence_allowed}; "
        f"supported={supported}; reason={reason}"
    )

    evidence = [
        f"claimed_decision:{claimed_decision}",
        f"evidence_allowed:{str(evidence_allowed).lower()}",
        f"supported:{str(supported).lower()}",
        f"reason:{reason}",
    ]

    return {
        "normative_ids": ["N21"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
