# demo07_memory_write_requires_provenance

**Normative:** N14  
**Goal:** Enforce provenance completeness for persistent memory writes.

## Invariant
Any persistent memory write MUST include provenance metadata.
If provenance is missing or incomplete, the write must be rejected.

## Rules
- If `persistent_write` is `false`: `allowed = true`.
- If `persistent_write` is `true`:
  - `provenance` must be an object
  - all `required_keys` must exist with non-empty values
  - otherwise `allowed = false`

## Fixtures
- `proof.json`
  - Persistent write with complete provenance
  - Expected: `ALLOW_WRITE`, `pass: true`
- `break.json`
  - Persistent write with missing provenance keys
  - Expected: `REJECT_WRITE_MISSING_PROVENANCE`, `pass: true`

## Run
```bash
python3 harness/run_demo.py --demo demo07_memory_write_requires_provenance --mode proof
python3 harness/run_demo.py --demo demo07_memory_write_requires_provenance --mode break
```

## Pass condition
`pass` is true iff computed `allowed == expected_allowed`.

## Determinism
No randomness, no network, fixture-only computation.
