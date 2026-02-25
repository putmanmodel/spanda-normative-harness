"""
Demo29: Invariant-Based Embodiment Transfer (N04)

Invariant:
Policy transfer across embodiments must use shared constraint abstractions,
not raw sensor equivalence.
"""


def run(fixture: dict) -> dict:
    source_embodiment = str(fixture["source_embodiment"])
    target_embodiment = str(fixture["target_embodiment"])
    transfer_method = str(fixture["transfer_method"])

    allowed = transfer_method == "INVARIANT_ABSTRACTION"

    expected_allowed = bool(fixture["expected_allowed"])
    passed = (allowed == expected_allowed)

    decision = "ALLOW_POLICY_TRANSFER" if allowed else "REJECT_RAW_SENSOR_TRANSFER"

    rationale = (
        f"source_embodiment={source_embodiment}; target_embodiment={target_embodiment}; "
        f"transfer_method={transfer_method}; allowed={allowed}"
    )

    evidence = [
        f"source_embodiment:{source_embodiment}",
        f"target_embodiment:{target_embodiment}",
        f"transfer_method:{transfer_method}",
        f"allowed:{str(allowed).lower()}",
    ]

    return {
        "normative_ids": ["N04"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
