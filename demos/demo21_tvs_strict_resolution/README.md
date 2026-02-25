# demo21_tvs_strict_resolution

**Normative:** N19  
**Goal:** Enforce strict TVS tag resolution with required provenance.

## Invariant
If TVS tags are used, they MUST resolve against a versioned dictionary and carry provenance.
If any tag is unresolved, the request is rejected.

## Rules
- `provenance_present = (provenance is dict and has at least one key)`
- `unresolved = [t for t in tags if t not in dictionary]`
- `allowed = (len(unresolved) == 0) AND provenance_present`

## Decision mapping
- `ALLOW_TVS_TAGS` if allowed
- `REJECT_TVS_UNRESOLVED_OR_NO_PROVENANCE` if not allowed

## Fixtures
- `proof.json`
  - all tags resolve
  - provenance present
  - expected: `allowed: true`, `expected_unresolved: []`
- `break.json`
  - includes unknown tag(s)
  - expected: `allowed: false`, `expected_unresolved` lists unknown tags

## Run
```bash
python3 harness/run_demo.py --demo demo21_tvs_strict_resolution --mode proof
python3 harness/run_demo.py --demo demo21_tvs_strict_resolution --mode break
```

## Pass condition
`pass` is true iff:
- `allowed == expected_allowed`, and
- `sorted(unresolved) == sorted(expected_unresolved)`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
