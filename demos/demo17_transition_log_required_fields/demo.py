"""
Demo17: Transition Log Required Fields (N29)

Invariant:
Canonical transitions require complete governance log fields.
"""


def _is_missing_value(value) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return value == ""
    if isinstance(value, (list, dict)):
        return len(value) == 0
    return False


def run(fixture: dict) -> dict:
    transition_requested = bool(fixture["transition_requested"])
    log_record = dict(fixture["log_record"])
    required_fields = [str(x) for x in fixture["required_fields"]]

    if not transition_requested:
        missing_fields = []
        allowed = True
    else:
        missing_fields = []
        for field in required_fields:
            if field not in log_record or _is_missing_value(log_record.get(field)):
                missing_fields.append(field)
        missing_fields = sorted(missing_fields)
        allowed = len(missing_fields) == 0

    expected_allowed = bool(fixture["expected_allowed"])
    expected_missing_fields = sorted([str(x) for x in fixture["expected_missing_fields"]])

    passed = (allowed == expected_allowed) and (missing_fields == expected_missing_fields)
    decision = "ALLOW_TRANSITION_LOGGED" if allowed else "REJECT_TRANSITION_MISSING_LOG_FIELDS"

    required_repr = "" if len(required_fields) == 0 else ",".join(required_fields)
    missing_repr = "none" if len(missing_fields) == 0 else ",".join(missing_fields)

    rationale = (
        f"transition_requested={transition_requested}; required_count={len(required_fields)}; "
        f"missing_fields={missing_fields}; allowed={allowed}"
    )

    evidence = [
        f"transition_requested:{str(transition_requested).lower()}",
        f"required_fields:{required_repr}",
        f"missing_fields:{missing_repr}",
        f"allowed:{str(allowed).lower()}",
    ]

    return {
        "normative_ids": ["N29"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
