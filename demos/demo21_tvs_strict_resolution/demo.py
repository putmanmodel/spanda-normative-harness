"""
Demo21: TVS Strict Resolution (N19)

Invariant:
TVS tags must resolve against a versioned dictionary and include provenance.
"""


def run(fixture: dict) -> dict:
    dictionary_version = str(fixture["dictionary_version"])
    dictionary = dict(fixture["dictionary"])
    tags = [str(t) for t in fixture["tags"]]
    provenance = fixture["provenance"]

    provenance_present = isinstance(provenance, dict) and (len(provenance) > 0)
    unresolved = [t for t in tags if t not in dictionary]

    allowed = (len(unresolved) == 0) and provenance_present

    expected_allowed = bool(fixture["expected_allowed"])
    expected_unresolved = sorted([str(t) for t in fixture["expected_unresolved"]])

    passed = (allowed == expected_allowed) and (sorted(unresolved) == expected_unresolved)

    decision = "ALLOW_TVS_TAGS" if allowed else "REJECT_TVS_UNRESOLVED_OR_NO_PROVENANCE"

    tags_repr = "" if len(tags) == 0 else ",".join(tags)
    unresolved_repr = "none" if len(unresolved) == 0 else ",".join(unresolved)

    rationale = (
        f"dictionary_version={dictionary_version}; tag_count={len(tags)}; "
        f"unresolved={sorted(unresolved)}; provenance_present={provenance_present}; allowed={allowed}"
    )

    evidence = [
        f"dictionary_version:{dictionary_version}",
        f"tags:{tags_repr}",
        f"provenance_present:{str(provenance_present).lower()}",
        f"unresolved:{unresolved_repr}",
        f"allowed:{str(allowed).lower()}",
    ]

    return {
        "normative_ids": ["N19"],
        "pass": passed,
        "decision": decision,
        "rationale": rationale,
        "evidence": evidence,
    }
