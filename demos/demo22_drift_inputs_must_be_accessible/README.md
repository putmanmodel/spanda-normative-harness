# demo22_drift_inputs_must_be_accessible

**Normative:** N13  
**Goal:** Ensure drift decisions only use interaction-accessible inputs.

## Invariant
Drift detection MUST use interaction-accessible inputs only.
If any input is marked `accessible: false`, the drift decision must be rejected.

## Rules
- `blocked = [name for each input where accessible == false]`
- If `drift_decision_requested` is `false`: `allowed = true`, `blocked = []`
- Else: `allowed = (len(blocked) == 0)`

## Decision mapping
- `ALLOW_DRIFT_DECISION` if allowed
- `REJECT_DRIFT_USES_INACCESSIBLE_INPUTS` if not allowed

## Fixtures
- `proof.json`
  - all inputs accessible
  - `drift_decision_requested: true`
  - expected: `allowed: true`, `blocked: []`
- `break.json`
  - includes at least one inaccessible input
  - expected: `allowed: false`, blocked includes that input name

## Run
```bash
python3 harness/run_demo.py --demo demo22_drift_inputs_must_be_accessible --mode proof
python3 harness/run_demo.py --demo demo22_drift_inputs_must_be_accessible --mode break
```

## Pass condition
`pass` is true iff:
- `allowed == expected_allowed`, and
- `sorted(blocked) == sorted(expected_blocked_inputs)`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
