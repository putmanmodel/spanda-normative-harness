# demo05_residual_activation_bounded

**Normative:** N07  
**Goal:** Enforce bounded residual activation via explicit clamping.

## What this demo asserts
- Compute `proposed = residual_before + residual_delta`.
- If `proposed > cap`, clamp to `cap` and emit `residual_clamped:true`.
- Otherwise apply `proposed` and emit `residual_clamped:false`.

## Fixtures
- `proof.json`
  - Non-clamp case where `residual_before + residual_delta <= cap`
  - Expected: decision `APPLY_RESIDUAL`, `pass: true`
- `break.json`
  - Clamp case where `residual_before + residual_delta > cap`
  - Expected: decision `CLAMP_RESIDUAL`, `pass: true`

## Run
```bash
python harness/run_demo.py --demo demo05_residual_activation_bounded --mode proof
python harness/run_demo.py --demo demo05_residual_activation_bounded --mode break
```

## Pass conditions
- `pass` is true iff:
  - computed `residual_after == expected_residual_after` (exact equality), and
  - computed clamp state matches `expected_clamped`.
- Evidence always includes:
  - `residual_before:<value>`
  - `residual_delta:<value>`
  - `cap:<value>`
  - `residual_after:<value>`
  - `residual_clamped:true|false`

## Determinism
No randomness, no network calls, and pure fixture-driven behavior.
