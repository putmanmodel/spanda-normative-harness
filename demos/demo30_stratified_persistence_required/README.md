# demo30_stratified_persistence_required

**Normative:** N05  
**Goal:** Enforce stratified persistence across Surface, Intermediate, and Priors layers.

## Invariant
Temporally extended agency MUST use stratified memory:
Surface (short-term), Intermediate (long-term), Priors (archetypal).
Single-layer persistence is non-compliant.

## Rules
- `compliant = true` iff every item in `required_layers` is present in `layers_present`

## Decision mapping
- `COMPLIANT_STRATIFIED` if compliant
- `NONCOMPLIANT_SINGLE_LAYER` if not compliant

## Fixtures
- `proof.json`
  - all required layers present
  - expected: `compliant: true`
- `break.json`
  - one or more required layers missing (example includes only `Surface`)
  - expected: `compliant: false`

## Run
```bash
python3 harness/run_demo.py --demo demo30_stratified_persistence_required --mode proof
python3 harness/run_demo.py --demo demo30_stratified_persistence_required --mode break
```

## Pass condition
`pass` is true iff `compliant == expected_compliant`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
