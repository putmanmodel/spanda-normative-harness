"""
Demo26: Asymmetric Influence Measurable (N11)

Invariant:
Concentrated reference causes disproportionate influence, and amplification is measurable.
"""


def run(fixture: dict) -> dict:
    base_influence = float(fixture["base_influence"])
    reference_concentration = float(fixture["reference_concentration"])
    concentration_threshold = float(fixture["concentration_threshold"])
    amplification_factor = float(fixture["amplification_factor"])

    if reference_concentration >= concentration_threshold:
        effective_influence = base_influence * amplification_factor
        amplified = True
    else:
        effective_influence = base_influence
        amplified = False

    expected_effective_influence = float(fixture["expected_effective_influence"])
    expected_amplified = bool(fixture["expected_amplified"])

    passed = (
        effective_influence == expected_effective_influence
        and amplified == expected_amplified
    )

    decision = "AMPLIFIED_INFLUENCE" if amplified else "BASELINE_INFLUENCE"

    rationale = (
        f"base_influence={base_influence}; reference_concentration={reference_concentration}; "
        f"concentration_threshold={concentration_threshold}; amplification_factor={amplification_factor}; "
        f"effective_influence={effective_influence}; amplified={amplified}"
    )

    evidence = [
        f"base_influence:{base_influence}",
        f"reference_concentration:{reference_concentration}",
        f"concentration_threshold:{concentration_threshold}",
        f"amplification_factor:{amplification_factor}",
        f"effective_influence:{effective_influence}",
        f"amplified:{str(amplified).lower()}",
    ]

    return {
        "normative_ids": ["N11"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
