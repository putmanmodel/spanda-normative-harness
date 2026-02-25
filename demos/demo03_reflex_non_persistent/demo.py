"""
Demo03: Reflex Non-Persistent (N22)

Rule:
Reflex MUST NOT:
- write memory
- update baselines
- modify priors
- trigger irreversible actions

We model the system state as dictionaries passed in fixture.
The demo passes if reflex output contains NO persistent mutations and NO irreversible action.
"""

FORBIDDEN_MUTATIONS = ("memory_writes", "baseline_updates", "prior_updates", "irreversible_actions")

def run(fixture: dict) -> dict:
    reflex_triggered = bool(fixture.get("reflex_triggered", False))

    attempted = fixture.get("attempted", {})
    state = fixture.get("state", {"memory": [], "baseline": {}, "priors": {}})

    violations = []
    if reflex_triggered:
        for k in FORBIDDEN_MUTATIONS:
            v = attempted.get(k, None)
            if v:
                violations.append(f"forbidden:{k}")

    pass_expected = bool(fixture.get("expected_pass", True))
    passed = (len(violations) == 0) and pass_expected

    if len(violations) == 0:
        decision = "REFLEX_FLAG_ONLY"
        rationale = "Reflex fired; emitted attention flag only. No persistent writes or irreversible actions."
        evidence = ["reflex:triggered" if reflex_triggered else "reflex:not_triggered"]
    else:
        decision = "REFLEX_VIOLATION_REJECTED"
        rationale = "Reflex attempted forbidden persistent mutation or irreversible action; rejected/flagged."
        evidence = ["reflex:triggered"] + violations

    return {
        "normative_ids": ["N22"],
        "pass": passed if pass_expected else (len(violations) > 0),
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
