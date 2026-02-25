# demo20_post_instability_stabilization_window

**Normative:** N30  
**Goal:** Enforce a bounded stabilization window after instability before updates resume.

## Invariant
After instability, the system MUST enforce a stabilization window before baseline updates resume.
If `steps_since_instability < stabilization_window`, requested updates are rejected.

## Rules
- If `update_requested` is `false`: `allowed = true`
- Else if `instability_recent` is `true` and `steps_since_instability < stabilization_window`: `allowed = false`
- Else: `allowed = true`

## Decision mapping
- `ALLOW_BASELINE_UPDATE` if allowed
- `REJECT_UPDATE_STABILIZATION_WINDOW` if not allowed

## Fixtures
- `proof.json`
  - `instability_recent: true`
  - `steps_since_instability >= stabilization_window`
  - `update_requested: true`
  - Expected: `allowed: true`
- `break.json`
  - `instability_recent: true`
  - `steps_since_instability < stabilization_window`
  - `update_requested: true`
  - Expected: `allowed: false`

## Run
```bash
python3 harness/run_demo.py --demo demo20_post_instability_stabilization_window --mode proof
python3 harness/run_demo.py --demo demo20_post_instability_stabilization_window --mode break
```

## Pass condition
`pass` is true iff `allowed == expected_allowed`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
