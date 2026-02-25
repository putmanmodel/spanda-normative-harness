# demo29_invariant_based_embodiment_transfer

**Normative:** N04  
**Goal:** Allow embodiment transfer only via invariant abstractions.

## Invariant
Policy transfer across embodiments MUST occur via shared constraint abstractions (invariants),
not raw sensor equivalence.

## Rules
- `allowed = true` iff `transfer_method == "INVARIANT_ABSTRACTION"`
- Otherwise `allowed = false`

## Decision mapping
- `ALLOW_POLICY_TRANSFER` if allowed
- `REJECT_RAW_SENSOR_TRANSFER` if not allowed

## Fixtures
- `proof.json`
  - `transfer_method: INVARIANT_ABSTRACTION`
  - expected: `allowed: true`
- `break.json`
  - `transfer_method: RAW_SENSOR_EQUIVALENCE`
  - expected: `allowed: false`

## Run
```bash
python3 harness/run_demo.py --demo demo29_invariant_based_embodiment_transfer --mode proof
python3 harness/run_demo.py --demo demo29_invariant_based_embodiment_transfer --mode break
```

## Pass condition
`pass` is true iff `allowed == expected_allowed`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
