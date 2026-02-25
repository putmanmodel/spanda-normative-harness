"""
Demo23: Scope-Stratified Baselines (N15)

Invariant:
Baseline updates must target a supported scope in the stratified baseline system.
"""


def run(fixture: dict) -> dict:
    supported_scopes = [str(s) for s in fixture["supported_scopes"]]
    requested_scope = str(fixture["requested_scope"])
    update_requested = bool(fixture["update_requested"])

    # Included to ensure fixture fields are consumed by the demo contract.
    baseline_before = dict(fixture["baseline_before"])
    baseline_update = dict(fixture["baseline_update"])

    if not update_requested:
        allowed = True
    else:
        allowed = requested_scope in supported_scopes

    expected_allowed = bool(fixture["expected_allowed"])
    passed = (allowed == expected_allowed)

    decision = "ALLOW_SCOPE_UPDATE" if allowed else "REJECT_UNSUPPORTED_SCOPE"

    supported_scopes_repr = "" if len(supported_scopes) == 0 else ",".join(supported_scopes)

    rationale = (
        f"update_requested={update_requested}; requested_scope={requested_scope}; "
        f"supported={requested_scope in supported_scopes}; allowed={allowed}; "
        f"baseline_before_keys={sorted(list(baseline_before.keys()))}; "
        f"baseline_update_keys={sorted(list(baseline_update.keys()))}"
    )

    evidence = [
        f"supported_scopes:{supported_scopes_repr}",
        f"requested_scope:{requested_scope}",
        f"update_requested:{str(update_requested).lower()}",
        f"allowed:{str(allowed).lower()}",
    ]

    return {
        "normative_ids": ["N15"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
