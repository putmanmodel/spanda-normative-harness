# demo10_baseline_update_requires_stability_window

**Normative:** N16  
**Goal:** Ensure baseline updates are only applied after a sufficient stability window.

## Invariant
Baseline updates MUST require at least `stability_required` consecutive stable steps.
If stability is insufficient, update is rejected and baseline remains unchanged.

## Rules
- `applied = (stable_steps >= stability_required)`
- If `applied` is true: `baseline_after = proposed_update`
- If `applied` is false: `baseline_after = baseline_before`

## Decision mapping
- `APPLY_BASELINE_UPDATE` if `applied` is true
- `REJECT_UPDATE_INSUFFICIENT_STABILITY` if `applied` is false

## Fixtures
- `proof.json`
  - `stable_steps >= stability_required`
  - Expected: `expected_applied: true`, `expected_baseline_after == proposed_update`
- `break.json`
  - `stable_steps < stability_required`
  - Expected: `expected_applied: false`, `expected_baseline_after == baseline_before`

## Run
```bash
python3 harness/run_demo.py --demo demo10_baseline_update_requires_stability_window --mode proof
python3 harness/run_demo.py --demo demo10_baseline_update_requires_stability_window --mode break
```

## Pass condition
`pass` is true iff:
- `applied == expected_applied`, and
- computed `baseline_after` deep-equals `expected_baseline_after`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
