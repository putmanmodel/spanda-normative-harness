# demo15_recall_attention_only

**Normative:** N27  
**Goal:** Ensure recall is strictly attention-only and cannot mutate governed state.

## Invariant
Recall MUST be attention-only.
Recall events must NOT mutate canonical memory, baseline, priors, or authorize irreversible actions.
Any attempted side effect is rejected, and state remains unchanged.

## Rules
- If `recall_triggered` is `false`: `allowed = true`; `state_after = state_before`
- If `recall_triggered` is `true`:
  - If any attempted flag is true (`canonical_memory_write`, `baseline_update`, `prior_update`, `irreversible_action`):
    - `allowed = false`
    - `state_after = state_before`
  - Else:
    - `allowed = true`
    - `state_after = state_before`

## Decision mapping
- `RECALL_OK_NO_MUTATION` if allowed
- `RECALL_VIOLATION_REJECTED` if not allowed

## Fixtures
- `proof.json`
  - `recall_triggered: true`
  - all attempted flags false
  - expected: `allowed: true`, `state_after == state_before`
- `break.json`
  - `recall_triggered: true`
  - at least one attempted flag true
  - expected: `allowed: false`, `state_after == state_before`

## Run
```bash
python3 harness/run_demo.py --demo demo15_recall_attention_only --mode proof
python3 harness/run_demo.py --demo demo15_recall_attention_only --mode break
```

## Pass condition
`pass` is true iff:
- `allowed == expected_allowed`, and
- computed `state_after` deep-equals `expected_state_after`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
