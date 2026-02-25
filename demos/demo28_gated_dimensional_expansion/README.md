# demo28_gated_dimensional_expansion

**Normative:** N03  
**Goal:** Prevent silent dimensional expansion by requiring consistency gain and invariant traceability.

## Invariant
Latent variables MAY be introduced only if they reduce observable inconsistency
and remain traceable to constraint-accessible invariants.
Silent dimensional expansion is prohibited.

## Rules
- If `introduce_dimension` is `false`: `allowed = true`
- If `introduce_dimension` is `true`:
  - `allowed = (reduces_inconsistency and traceable_to_invariants)`

## Decision mapping
- `ALLOW_DIMENSION` if allowed and introducing dimension
- `REJECT_SILENT_DIMENSION` if introducing dimension and not allowed
- `NO_DIMENSION_CHANGE` if not introducing dimension

## Fixtures
- `proof.json`
  - `introduce_dimension: true`
  - `reduces_inconsistency: true`
  - `traceable_to_invariants: true`
  - expected: `allowed: true`
- `break.json`
  - `introduce_dimension: true`
  - `reduces_inconsistency: true`
  - `traceable_to_invariants: false`
  - expected: `allowed: false`

## Run
```bash
python3 harness/run_demo.py --demo demo28_gated_dimensional_expansion --mode proof
python3 harness/run_demo.py --demo demo28_gated_dimensional_expansion --mode break
```

## Pass condition
`pass` is true iff `allowed == expected_allowed`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
