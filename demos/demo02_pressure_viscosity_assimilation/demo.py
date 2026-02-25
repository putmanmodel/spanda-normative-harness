"""
Demo02: Pressure + Viscosity Assimilation (N06)

Goal:
- Consolidation (ME -> US) requires BOTH:
  1) Pressure >= pressure_threshold
  2) Exposure_count >= viscosity_exposure_min

Interpretation:
- "pressure" = intensity / salience at the moment
- "viscosity" = how resistant the tier boundary is; modeled here as requiring repeat exposure

Deterministic:
- No randomness
- Pure function from fixture -> result
"""

def run(fixture: dict) -> dict:
    pressure = float(fixture["pressure"])
    exposures = int(fixture["exposures"])
    pressure_threshold = float(fixture.get("pressure_threshold", 0.75))
    viscosity_exposure_min = int(fixture.get("viscosity_exposure_min", 3))

    should_consolidate = (pressure >= pressure_threshold) and (exposures >= viscosity_exposure_min)

    expected = bool(fixture.get("expected_consolidate"))
    passed = (should_consolidate == expected)

    decision = "CONSOLIDATE_ME_TO_US" if should_consolidate else "DO_NOT_CONSOLIDATE"

    rationale = (
        f"pressure={pressure} (thresh={pressure_threshold}), "
        f"exposures={exposures} (min={viscosity_exposure_min}) => consolidate={should_consolidate}"
    )

    evidence = [
        f"pressure:{pressure}",
        f"exposures:{exposures}",
        f"pressure_threshold:{pressure_threshold}",
        f"viscosity_exposure_min:{viscosity_exposure_min}",
    ]

    return {
        "normative_ids": ["N06"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
