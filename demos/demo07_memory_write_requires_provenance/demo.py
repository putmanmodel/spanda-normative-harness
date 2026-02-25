"""
Demo07: Memory Write Requires Provenance (N14)

Invariant:
Any persistent memory write must include complete provenance metadata.
If provenance is missing or incomplete, reject the write.
"""


def _is_non_empty(value) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value.strip() != ""
    return True


def run(fixture: dict) -> dict:
    write_request_id = str(fixture["write_request_id"])
    persistent_write = bool(fixture["persistent_write"])
    payload = dict(fixture["payload"])
    provenance = fixture["provenance"]
    required_keys = [str(k) for k in fixture["required_keys"]]

    provenance_is_dict = isinstance(provenance, dict)
    provenance_present = provenance_is_dict

    missing_keys = []
    if persistent_write:
        if not provenance_is_dict:
            missing_keys = list(required_keys)
            allowed = False
        else:
            for key in required_keys:
                if key not in provenance or not _is_non_empty(provenance.get(key)):
                    missing_keys.append(key)
            allowed = len(missing_keys) == 0
    else:
        allowed = True

    expected_allowed = bool(fixture["expected_allowed"])
    passed = (allowed == expected_allowed)

    decision = "ALLOW_WRITE" if allowed else "REJECT_WRITE_MISSING_PROVENANCE"

    missing_repr = "none" if len(missing_keys) == 0 else ",".join(missing_keys)
    required_repr = "" if len(required_keys) == 0 else ",".join(required_keys)

    rationale = (
        f"write_request_id={write_request_id}; persistent_write={persistent_write}; "
        f"provenance_present={provenance_present}; missing_keys={missing_repr}; "
        f"payload_keys={sorted(list(payload.keys()))} => allowed={allowed}"
    )

    evidence = [
        f"write_request_id:{write_request_id}",
        f"persistent_write:{str(persistent_write).lower()}",
        f"required_keys:{required_repr}",
        f"provenance_present:{str(provenance_present).lower()}",
        f"provenance_missing_keys:{missing_repr}",
        f"allowed:{str(allowed).lower()}",
    ]

    return {
        "normative_ids": ["N14"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
