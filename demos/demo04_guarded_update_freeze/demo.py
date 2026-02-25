"""
Demo04: Guarded Update / Freeze (N18)

Rule:
Baseline adaptation MUST be suppressed under instability.
"freeze" is a governed mode change.

We model:
- instability: bool
- proposed_updates: dict
- baseline_before: dict

If instability=True -> baseline must NOT change.
If instability=False -> baseline may update as proposed.
"""

def run(fixture: dict) -> dict:
    instability = bool(fixture.get("instability", False))
    baseline_before = dict(fixture.get("baseline_before", {}))
    proposed_updates = dict(fixture.get("proposed_updates", {}))

    baseline_after = dict(baseline_before)

    if not instability:
        baseline_after.update(proposed_updates)

    expected_changed = bool(fixture.get("expected_baseline_changed", False))
    actually_changed = (baseline_after != baseline_before)

    passed = (actually_changed == expected_changed)

    if instability:
        decision = "FREEZE_BASELINE"
        rationale = "Instability detected; baseline updates suppressed (freeze)."
        evidence = ["instability:true", f"proposed_update_keys:{sorted(list(proposed_updates.keys()))}"]
    else:
        decision = "APPLY_BASELINE_UPDATE"
        rationale = "Stable regime; baseline updated using proposed updates."
        evidence = ["instability:false", f"applied_update_keys:{sorted(list(proposed_updates.keys()))}"]

    return {
        "normative_ids": ["N18"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
