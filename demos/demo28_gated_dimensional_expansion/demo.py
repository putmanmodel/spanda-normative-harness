"""
Demo28: Gated Dimensional Expansion (N03)

Invariant:
Latent dimensions may be introduced only when they reduce inconsistency and
remain traceable to constraint-accessible invariants.
"""


def run(fixture: dict) -> dict:
    introduce_dimension = bool(fixture["introduce_dimension"])
    reduces_inconsistency = bool(fixture["reduces_inconsistency"])
    traceable_to_invariants = bool(fixture["traceable_to_invariants"])

    if not introduce_dimension:
        allowed = True
    else:
        allowed = reduces_inconsistency and traceable_to_invariants

    if introduce_dimension and allowed:
        decision = "ALLOW_DIMENSION"
    elif introduce_dimension and (not allowed):
        decision = "REJECT_SILENT_DIMENSION"
    else:
        decision = "NO_DIMENSION_CHANGE"

    expected_allowed = bool(fixture["expected_allowed"])
    passed = (allowed == expected_allowed)

    rationale = (
        f"introduce_dimension={introduce_dimension}; reduces_inconsistency={reduces_inconsistency}; "
        f"traceable_to_invariants={traceable_to_invariants}; allowed={allowed}"
    )

    evidence = [
        f"introduce_dimension:{str(introduce_dimension).lower()}",
        f"reduces_inconsistency:{str(reduces_inconsistency).lower()}",
        f"traceable_to_invariants:{str(traceable_to_invariants).lower()}",
        f"allowed:{str(allowed).lower()}",
    ]

    return {
        "normative_ids": ["N03"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
