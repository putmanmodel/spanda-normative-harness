# demo23_scope_stratified_baselines

**Normative:** N15  
**Goal:** Enforce that baseline updates target only supported stratified scopes.

## Invariant
The system MUST maintain baselines at multiple scopes.
A baseline update request must specify a supported scope; unsupported scopes are rejected.

## Rules
- If `update_requested` is `false`: `allowed = true`
- Else: `allowed = (requested_scope in supported_scopes)`

## Decision mapping
- `ALLOW_SCOPE_UPDATE` if allowed
- `REJECT_UNSUPPORTED_SCOPE` if not allowed

## Fixtures
- `proof.json`
  - `requested_scope: scene` and `scene` is in `supported_scopes`
  - `update_requested: true`
  - expected: `allowed: true`
- `break.json`
  - `requested_scope: org` and `org` is not in `supported_scopes`
  - `update_requested: true`
  - expected: `allowed: false`

## Run
```bash
python3 harness/run_demo.py --demo demo23_scope_stratified_baselines --mode proof
python3 harness/run_demo.py --demo demo23_scope_stratified_baselines --mode break
```

## Pass condition
`pass` is true iff `allowed == expected_allowed`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
