"""
Demo05: Residual Activation Bounded (N07)

Invariant:
Prevent unbounded residual activation accumulation.
If residual_before + residual_delta exceeds cap, clamp to cap and emit
residual_clamped:true. Otherwise apply normally with residual_clamped:false.
"""


def run(fixture: dict) -> dict:
    residual_before = float(fixture["residual_before"])
    residual_delta = float(fixture["residual_delta"])
    cap = float(fixture["cap"])

    proposed = residual_before + residual_delta
    clamped = proposed > cap
    residual_after = cap if clamped else proposed

    expected_residual_after = float(fixture["expected_residual_after"])
    expected_clamped = bool(fixture["expected_clamped"])

    passed = (residual_after == expected_residual_after) and (clamped == expected_clamped)
    decision = "CLAMP_RESIDUAL" if clamped else "APPLY_RESIDUAL"

    rationale = (
        f"residual_before={residual_before} + residual_delta={residual_delta} "
        f"=> proposed={proposed}; cap={cap}; clamped={clamped}"
    )

    evidence = [
        f"residual_before:{residual_before}",
        f"residual_delta:{residual_delta}",
        f"cap:{cap}",
        f"residual_after:{residual_after}",
        f"residual_clamped:{str(clamped).lower()}",
    ]

    return {
        "normative_ids": ["N07"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
