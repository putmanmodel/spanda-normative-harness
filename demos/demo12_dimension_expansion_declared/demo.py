"""
Demo12: Dimension Expansion Declared (N09)

Invariant:
Any dimension expansion must be explicitly declared.
Undeclared new dimensions are rejected.
"""


def run(fixture: dict) -> dict:
    declared_dimensions = [str(x) for x in fixture["declared_dimensions"]]
    new_dimensions = [str(x) for x in fixture["new_dimensions"]]

    undeclared = sorted(set(new_dimensions) - set(declared_dimensions))
    allowed = len(undeclared) == 0

    expected_allowed = bool(fixture["expected_allowed"])
    expected_undeclared = sorted([str(x) for x in fixture["expected_undeclared"]])

    passed = (allowed == expected_allowed) and (undeclared == expected_undeclared)
    decision = "ALLOW_DIMENSION_EXPANSION" if allowed else "REJECT_UNDECLARED_DIMENSIONS"

    declared_repr = "" if len(declared_dimensions) == 0 else ",".join(declared_dimensions)
    new_repr = "" if len(new_dimensions) == 0 else ",".join(new_dimensions)
    undeclared_repr = "none" if len(undeclared) == 0 else ",".join(undeclared)

    rationale = (
        f"declared_count={len(declared_dimensions)}; new_count={len(new_dimensions)}; "
        f"undeclared={undeclared}; allowed={allowed}"
    )

    evidence = [
        f"declared_dimensions:{declared_repr}",
        f"new_dimensions:{new_repr}",
        f"undeclared_dimensions:{undeclared_repr}",
        f"allowed:{str(allowed).lower()}",
    ]

    return {
        "normative_ids": ["N09"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
