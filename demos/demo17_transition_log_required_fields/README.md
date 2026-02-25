# demo17_transition_log_required_fields

**Normative:** N29  
**Goal:** Require complete canonical transition logs with all mandated fields populated.

## Invariant
Every canonical transition MUST emit a log record containing required fields:
`timestamp`, `event_ids`, `predicate_vector`, `governance_token`, `signer_tag`.
If any required field is missing or empty, the transition is rejected.

## Rules
- If `transition_requested` is false:
  - `allowed = true`
  - `missing_fields = []`
- If `transition_requested` is true:
  - For each required field, missing if:
    - field is absent, or
    - value is `null`, or
    - value is `""`, or
    - value is an empty list/dict
  - `allowed = (len(missing_fields) == 0)`

## Decision mapping
- `ALLOW_TRANSITION_LOGGED` if allowed
- `REJECT_TRANSITION_MISSING_LOG_FIELDS` if not allowed

## Fixtures
- `proof.json`
  - Transition requested with all required fields present and non-empty
  - Expected: `allowed: true`, `missing_fields: []`
- `break.json`
  - Transition requested with at least one missing/empty required field
  - Expected: `allowed: false`, `missing_fields` includes that field

## Run
```bash
python3 harness/run_demo.py --demo demo17_transition_log_required_fields --mode proof
python3 harness/run_demo.py --demo demo17_transition_log_required_fields --mode break
```

## Pass condition
`pass` is true iff:
- `allowed == expected_allowed`, and
- `missing_fields == sorted(expected_missing_fields)`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
