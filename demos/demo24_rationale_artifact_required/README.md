# demo24_rationale_artifact_required

**Normative:** N17  
**Goal:** Enforce rationale artifact presence for governance events.

## Invariant
Any governance event MUST produce a rationale artifact sufficient for deterministic replay.
If rationale pointers are missing or empty, the event must be rejected.

## Rules
- If `governance_event` is `false`: `allowed = true`, `missing = false`
- Else:
  - `missing = (rationale_pointers is null OR len(rationale_pointers) == 0)`
  - `allowed = (missing == false)`

## Decision mapping
- `ALLOW_GOVERNANCE_EVENT` if allowed
- `REJECT_GOVERNANCE_MISSING_RATIONALE` if not allowed

## Fixtures
- `proof.json`
  - `governance_event: true`
  - `rationale_pointers` has at least one item
  - expected: `allowed: true`, `missing: false`
- `break.json`
  - `governance_event: true`
  - `rationale_pointers` empty (or null)
  - expected: `allowed: false`, `missing: true`

## Run
```bash
python3 harness/run_demo.py --demo demo24_rationale_artifact_required --mode proof
python3 harness/run_demo.py --demo demo24_rationale_artifact_required --mode break
```

## Pass condition
`pass` is true iff:
- `allowed == expected_allowed`, and
- `missing == expected_missing`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
