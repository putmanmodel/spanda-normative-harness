"""
Demo30: Stratified Persistence Required (N05)

Invariant:
Temporally extended agency requires stratified memory layers.
"""


def run(fixture: dict) -> dict:
    layers_present = [str(x) for x in fixture["layers_present"]]
    required_layers = [str(x) for x in fixture["required_layers"]]

    missing_layers = [layer for layer in required_layers if layer not in layers_present]
    compliant = len(missing_layers) == 0

    expected_compliant = bool(fixture["expected_compliant"])
    passed = (compliant == expected_compliant)

    decision = "COMPLIANT_STRATIFIED" if compliant else "NONCOMPLIANT_SINGLE_LAYER"

    layers_present_repr = "" if len(layers_present) == 0 else ",".join(layers_present)
    required_layers_repr = "" if len(required_layers) == 0 else ",".join(required_layers)
    missing_layers_repr = "none" if len(missing_layers) == 0 else ",".join(missing_layers)

    rationale = (
        f"layers_present={layers_present}; required_layers={required_layers}; "
        f"missing_layers={missing_layers}; compliant={compliant}"
    )

    evidence = [
        f"layers_present:{layers_present_repr}",
        f"required_layers:{required_layers_repr}",
        f"missing_layers:{missing_layers_repr}",
        f"compliant:{str(compliant).lower()}",
    ]

    return {
        "normative_ids": ["N05"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
