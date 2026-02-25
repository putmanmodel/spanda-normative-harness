# demo13_action_budget_cap

**Normative:** N26  
**Goal:** Enforce a strict action budget cap per cycle.

## Invariant
The system MUST enforce an action budget per cycle.
If requested actions exceed `budget_cap`, excess is clamped so `executed_count <= budget_cap` and clamping is indicated.

## Rules
- `requested_count = len(requested_actions)`
- If `requested_count <= budget_cap`:
  - `executed_count = requested_count`
  - `clamped = false`
- Else:
  - `executed_count = budget_cap`
  - `clamped = true`

## Decision mapping
- `EXECUTE_WITHIN_BUDGET` if not clamped
- `CLAMP_ACTIONS_TO_BUDGET` if clamped

## Fixtures
- `proof.json`
  - Requested actions are within cap
  - Expected: `clamped: false`, `executed_count == requested_count`
- `break.json`
  - Requested actions exceed cap
  - Expected: `clamped: true`, `executed_count == budget_cap`

## Run
```bash
python3 harness/run_demo.py --demo demo13_action_budget_cap --mode proof
python3 harness/run_demo.py --demo demo13_action_budget_cap --mode break
```

## Pass condition
`pass` is true iff:
- `executed_count == expected_executed_count`, and
- `clamped == expected_clamped`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
