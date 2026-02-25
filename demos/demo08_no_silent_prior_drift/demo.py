"""
Demo08: No Silent Prior Drift (N25)

Invariant:
Priors must not change unless an explicit prior-update path is invoked.
"""


def run(fixture: dict) -> dict:
    priors_before = dict(fixture["priors_before"])
    proposed_priors_after = dict(fixture["proposed_priors_after"])
    explicit_update = bool(fixture["explicit_update"])

    drift_attempted = proposed_priors_after != priors_before

    if explicit_update:
        allowed = True
        priors_after = dict(proposed_priors_after)
    else:
        if drift_attempted:
            allowed = False
            priors_after = dict(priors_before)
        else:
            allowed = True
            priors_after = dict(priors_before)

    expected_priors_after = dict(fixture["expected_priors_after"])
    expected_allowed = bool(fixture["expected_allowed"])

    passed = (allowed == expected_allowed) and (priors_after == expected_priors_after)

    if not allowed:
        decision = "REJECT_SILENT_PRIOR_DRIFT"
    elif explicit_update:
        decision = "APPLY_PRIOR_UPDATE"
    else:
        decision = "NO_CHANGE_OK"

    priors_keys = sorted(set(list(priors_before.keys()) + list(proposed_priors_after.keys())))
    priors_keys_repr = "" if len(priors_keys) == 0 else ",".join(priors_keys)

    rationale = (
        f"explicit_update={explicit_update}; drift_attempted={drift_attempted}; "
        f"allowed={allowed}; priors_after_keys={sorted(list(priors_after.keys()))}"
    )

    evidence = [
        f"explicit_update:{str(explicit_update).lower()}",
        f"drift_attempted:{str(drift_attempted).lower()}",
        f"allowed:{str(allowed).lower()}",
        f"priors_keys:{priors_keys_repr}",
    ]

    return {
        "normative_ids": ["N25"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
