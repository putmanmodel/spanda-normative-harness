# demo08_no_silent_prior_drift

**Normative:** N25  
**Goal:** Ensure priors never drift without explicit prior-update invocation.

## Invariant
Priors MUST NOT change unless an explicit prior-update path is invoked.
When `explicit_update` is `false`, any attempted prior change is rejected and priors remain unchanged.

## Rules
- If `explicit_update` is `true`: `allowed = true`, `priors_after = proposed_priors_after`
- If `explicit_update` is `false`:
  - If `proposed_priors_after != priors_before`: `allowed = false`, `priors_after = priors_before`
  - If `proposed_priors_after == priors_before`: `allowed = true`, `priors_after = priors_before`

## Decision mapping
- `APPLY_PRIOR_UPDATE` if allowed and explicit update path used
- `NO_CHANGE_OK` if allowed with no explicit update and no drift attempt
- `REJECT_SILENT_PRIOR_DRIFT` if drift attempt occurs without explicit update

## Fixtures
- `proof.json`
  - `explicit_update: false`
  - `proposed_priors_after == priors_before`
  - Expected: `allowed: true`, `priors_after` unchanged
- `break.json`
  - `explicit_update: false`
  - `proposed_priors_after != priors_before`
  - Expected: `allowed: false`, `priors_after` unchanged

## Run
```bash
python3 harness/run_demo.py --demo demo08_no_silent_prior_drift --mode proof
python3 harness/run_demo.py --demo demo08_no_silent_prior_drift --mode break
```

## Pass condition
`pass` is true iff:
- `allowed == expected_allowed`, and
- computed `priors_after` deep-equals `expected_priors_after`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
