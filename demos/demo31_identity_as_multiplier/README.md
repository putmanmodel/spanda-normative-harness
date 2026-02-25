# demo31_identity_as_multiplier

**Normative:** N08  
**Goal:** Enforce identity as a multiplier mechanism rather than an identity flag.

## Invariant
Identity MUST manifest as persistence weighting and hysteresis (multiplier effects),
not as a metaphysical identity flag.

## Rules
- `effective_weight = base_weight * identity_multiplier`
- `compliant = true` iff `identity_flag_used` is false

## Decision mapping
- `COMPLIANT_MULTIPLIER` if compliant
- `NONCOMPLIANT_IDENTITY_FLAG` if not compliant

## Fixtures
- `proof.json`
  - `identity_flag_used: false`
  - `base_weight: 0.5`, `identity_multiplier: 2.0`
  - expected: `effective_weight: 1.0`, `compliant: true`
- `break.json`
  - `identity_flag_used: true`
  - `base_weight: 0.5`, `identity_multiplier: 2.0`
  - expected: `effective_weight: 1.0`, `compliant: false`

## Run
```bash
python3 harness/run_demo.py --demo demo31_identity_as_multiplier --mode proof
python3 harness/run_demo.py --demo demo31_identity_as_multiplier --mode break
```

## Pass condition
`pass` is true iff:
- `effective_weight == expected_effective_weight` (exact), and
- `compliant == expected_compliant`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
