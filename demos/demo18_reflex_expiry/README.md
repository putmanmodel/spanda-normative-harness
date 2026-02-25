# demo18_reflex_expiry

**Normative:** N23  
**Goal:** Ensure reflex activations expire unless re-triggered under short-horizon conditions.

## Invariant
Reflex events MUST expire automatically unless re-triggered.
If `age_steps > ttl_steps` and `retriggered` is false, `reflex_active_after` must be false.

## Rules
- If `reflex_active_before` is false: `reflex_active_after = false`
- Else (was active):
  - If `retriggered` is true: `reflex_active_after = true`
  - Else if `age_steps > ttl_steps`: `reflex_active_after = false`
  - Else: `reflex_active_after = true`

## Decision mapping
- `REFLEX_ACTIVE` if `reflex_active_after` is true
- `REFLEX_EXPIRED` if `reflex_active_after` is false and `reflex_active_before` was true
- `REFLEX_INACTIVE` if `reflex_active_before` was false

## Fixtures
- `proof.json`
  - `reflex_active_before: true`, `age_steps <= ttl_steps`, `retriggered: false`
  - Expected: `reflex_active_after: true`
- `break.json`
  - `reflex_active_before: true`, `age_steps > ttl_steps`, `retriggered: false`
  - Expected: `reflex_active_after: false`

## Run
```bash
python3 harness/run_demo.py --demo demo18_reflex_expiry --mode proof
python3 harness/run_demo.py --demo demo18_reflex_expiry --mode break
```

## Pass condition
`pass` is true iff `reflex_active_after == expected_reflex_active_after`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
