"""
Demo10: Baseline Update Requires Stability Window (N16)

Invariant:
Baseline updates require a minimum stability window.
Without sufficient consecutive stable steps, updates are rejected.
"""


def run(fixture: dict) -> dict:
    stable_steps = int(fixture["stable_steps"])
    stability_required = int(fixture["stability_required"])
    baseline_before = dict(fixture["baseline_before"])
    proposed_update = dict(fixture["proposed_update"])

    applied = stable_steps >= stability_required
    baseline_after = dict(proposed_update) if applied else dict(baseline_before)

    expected_baseline_after = dict(fixture["expected_baseline_after"])
    expected_applied = bool(fixture["expected_applied"])

    passed = (applied == expected_applied) and (baseline_after == expected_baseline_after)
    decision = "APPLY_BASELINE_UPDATE" if applied else "REJECT_UPDATE_INSUFFICIENT_STABILITY"

    baseline_keys = sorted(set(list(baseline_before.keys()) + list(proposed_update.keys())))
    baseline_keys_repr = "" if len(baseline_keys) == 0 else ",".join(baseline_keys)

    rationale = (
        f"stable_steps={stable_steps}; stability_required={stability_required}; "
        f"applied={applied}; baseline_after_keys={sorted(list(baseline_after.keys()))}"
    )

    evidence = [
        f"stable_steps:{stable_steps}",
        f"stability_required:{stability_required}",
        f"applied:{str(applied).lower()}",
        f"baseline_keys:{baseline_keys_repr}",
    ]

    return {
        "normative_ids": ["N16"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
