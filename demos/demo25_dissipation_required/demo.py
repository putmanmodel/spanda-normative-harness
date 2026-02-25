"""
Demo25: Dissipation Required (N10)

Invariant:
Strong coupling without sufficient dissipation is flagged as risk.
"""


def run(fixture: dict) -> dict:
    coupling_strength = float(fixture["coupling_strength"])
    dissipation_capacity = float(fixture["dissipation_capacity"])
    risk_threshold = float(fixture["risk_threshold"])

    risk_score = coupling_strength - dissipation_capacity
    risk_flagged = risk_score > risk_threshold

    expected_risk_flagged = bool(fixture["expected_risk_flagged"])
    passed = (risk_flagged == expected_risk_flagged)

    decision = "RISK_FLAGGED" if risk_flagged else "NO_RISK"

    rationale = (
        f"coupling_strength={coupling_strength}; dissipation_capacity={dissipation_capacity}; "
        f"risk_threshold={risk_threshold}; risk_score={risk_score}; risk_flagged={risk_flagged}"
    )

    evidence = [
        f"coupling_strength:{coupling_strength}",
        f"dissipation_capacity:{dissipation_capacity}",
        f"risk_threshold:{risk_threshold}",
        f"risk_score:{risk_score}",
        f"risk_flagged:{str(risk_flagged).lower()}",
    ]

    return {
        "normative_ids": ["N10"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
