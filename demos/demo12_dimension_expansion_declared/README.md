# demo12_dimension_expansion_declared

**Normative:** N09  
**Goal:** Enforce explicit declaration for any dimension expansion.

## Invariant
Any dimension expansion MUST be explicitly declared.
If `new_dimensions` contains values not in `declared_dimensions`, the expansion is rejected.

## Rules
- `undeclared = sorted(set(new_dimensions) - set(declared_dimensions))`
- `allowed = (len(undeclared) == 0)`

## Decision mapping
- `ALLOW_DIMENSION_EXPANSION` if allowed
- `REJECT_UNDECLARED_DIMENSIONS` if not allowed

## Fixtures
- `proof.json`
  - Declared list includes all new dimensions
  - Expected: `allowed: true`, `expected_undeclared: []`
- `break.json`
  - New dimensions include undeclared entry(s)
  - Expected: `allowed: false`, `expected_undeclared` includes undeclared dimension(s)

## Run
```bash
python3 harness/run_demo.py --demo demo12_dimension_expansion_declared --mode proof
python3 harness/run_demo.py --demo demo12_dimension_expansion_declared --mode break
```

## Pass condition
`pass` is true iff:
- `allowed == expected_allowed`, and
- computed `undeclared == sorted(expected_undeclared)`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
