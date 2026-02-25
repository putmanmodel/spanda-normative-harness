def run(fixture: dict) -> dict:
    invariant_supported = bool(fixture.get("invariant_supported", False))
    narrative_only = bool(fixture.get("narrative_only", False))

    if invariant_supported and not narrative_only:
        return {
            "normative_ids": ["N01", "N02", "N03"],
            "pass": True,
            "decision": "ACCEPT_INVARIANT_HYPOTHESIS",
            "rationale": "Hypothesis traceable to invariant boundary effects; no narrative projection required.",
            "evidence": fixture.get("evidence", ["constraint_surface:invariants"])
        }

    return {
        "normative_ids": ["N01", "N02", "N03"],
        "pass": (not narrative_only),
        "decision": "REJECT_OR_FLAG_PROJECTION",
        "rationale": "Hypothesis relies on narrative attribution without invariant support; flagged/rejected.",
        "evidence": fixture.get("evidence", ["constraint_surface:missing_invariants"])
    }
