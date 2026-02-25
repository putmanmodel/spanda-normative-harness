# demo26_asymmetric_influence_measurable

**Normative:** N11  
**Goal:** Enforce measurable asymmetric influence under concentrated reference.

## Invariant
Agents with concentrated reference MUST exert disproportionate influence, and amplification MUST be measurable.

## Rules
- If `reference_concentration >= concentration_threshold`:
  - `effective_influence = base_influence * amplification_factor`
  - `amplified = true`
- Else:
  - `effective_influence = base_influence`
  - `amplified = false`

## Decision mapping
- `AMPLIFIED_INFLUENCE` if amplified
- `BASELINE_INFLUENCE` otherwise

## Fixtures
- `proof.json`
  - concentration below threshold
  - expected: no amplification
- `break.json`
  - concentration at threshold
  - expected: amplification

## Run
```bash
python3 harness/run_demo.py --demo demo26_asymmetric_influence_measurable --mode proof
python3 harness/run_demo.py --demo demo26_asymmetric_influence_measurable --mode break
```

## Pass condition
`pass` is true iff:
- `effective_influence == expected_effective_influence` (exact), and
- `amplified == expected_amplified`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
