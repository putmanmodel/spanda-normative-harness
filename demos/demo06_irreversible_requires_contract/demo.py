"""
Demo06: Irreversible Requires Contract (N11)

Invariant:
Irreversible actions require a valid contract token.
If valid_contract is false for an irreversible action, the action is rejected.
"""


def run(fixture: dict) -> dict:
    action = str(fixture["action"])
    irreversible = bool(fixture["irreversible"])
    valid_contract = bool(fixture["valid_contract"])

    if irreversible and not valid_contract:
        allowed = False
    else:
        allowed = True

    expected_allowed = bool(fixture["expected_allowed"])
    passed = (allowed == expected_allowed)

    decision = "ALLOW_ACTION" if allowed else "REJECT_ACTION_NO_CONTRACT"
    rationale = (
        f"action={action}; irreversible={irreversible}; "
        f"valid_contract={valid_contract} => allowed={allowed}"
    )

    evidence = [
        f"action:{action}",
        f"irreversible:{str(irreversible).lower()}",
        f"valid_contract:{str(valid_contract).lower()}",
        f"allowed:{str(allowed).lower()}",
    ]

    return {
        "normative_ids": ["N11"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
