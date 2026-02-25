"""
Demo31: Identity as Multiplier (N08)

Invariant:
Identity must be expressed via persistence weighting/hysteresis multiplier effects,
not a metaphysical identity flag.
"""


def run(fixture: dict) -> dict:
    base_weight = float(fixture["base_weight"])
    identity_multiplier = float(fixture["identity_multiplier"])
    identity_flag_used = bool(fixture["identity_flag_used"])

    effective_weight = base_weight * identity_multiplier
    compliant = not identity_flag_used

    expected_effective_weight = float(fixture["expected_effective_weight"])
    expected_compliant = bool(fixture["expected_compliant"])

    passed = (
        effective_weight == expected_effective_weight
        and compliant == expected_compliant
    )

    decision = "COMPLIANT_MULTIPLIER" if compliant else "NONCOMPLIANT_IDENTITY_FLAG"

    rationale = (
        f"base_weight={base_weight}; identity_multiplier={identity_multiplier}; "
        f"effective_weight={effective_weight}; identity_flag_used={identity_flag_used}; "
        f"compliant={compliant}"
    )

    evidence = [
        f"base_weight:{base_weight}",
        f"identity_multiplier:{identity_multiplier}",
        f"effective_weight:{effective_weight}",
        f"identity_flag_used:{str(identity_flag_used).lower()}",
        f"compliant:{str(compliant).lower()}",
    ]

    return {
        "normative_ids": ["N08"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
