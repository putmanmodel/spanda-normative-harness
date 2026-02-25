"""
Demo09: Cross-Tier Write Requires Gate (N12)

Invariant:
Writes between memory tiers require an explicit gate signal.
If the gate is closed, cross-tier transfer is rejected.
"""


def run(fixture: dict) -> dict:
    source_tier = str(fixture["source_tier"])
    target_tier = str(fixture["target_tier"])
    cross_tier = bool(fixture["cross_tier"])
    gate_open = bool(fixture["gate_open"])

    if not cross_tier:
        transferred = False
    else:
        transferred = bool(gate_open)

    expected_transferred = bool(fixture["expected_transferred"])
    passed = (transferred == expected_transferred)

    if transferred:
        decision = "TRANSFER_ALLOWED"
    elif cross_tier and (not gate_open):
        decision = "REJECT_CROSS_TIER_NO_GATE"
    else:
        decision = "NO_TRANSFER_SAME_TIER"

    rationale = (
        f"source_tier={source_tier}; target_tier={target_tier}; cross_tier={cross_tier}; "
        f"gate_open={gate_open} => transferred={transferred}"
    )

    evidence = [
        f"source_tier:{source_tier}",
        f"target_tier:{target_tier}",
        f"cross_tier:{str(cross_tier).lower()}",
        f"gate_open:{str(gate_open).lower()}",
        f"transferred:{str(transferred).lower()}",
    ]

    return {
        "normative_ids": ["N12"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
