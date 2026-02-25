# demo01_constraint_boundary

**Normatives:** N01, N02, N03  
**Goal:** Prove constraint-only inference + reject narrative projection.

## What this demo asserts
- **N01:** Accept only hypotheses supported by invariant boundary effects.
- **N02:** Flag/reject intention/agency narratives without invariant support.
- **N03:** No silent dimensional expansion (placeholder here; enforced by “accept only invariant-backed hypothesis”).

## Fixtures
- `proof.json`
  - `invariant_supported: true`
  - `narrative_only: false`
  - Expected: **ACCEPT_INVARIANT_HYPOTHESIS**, `pass: true`
- `break.json`
  - `invariant_supported: false`
  - `narrative_only: true`
  - Expected: **REJECT_OR_FLAG_PROJECTION**, `pass: false`

## Run
```[FENCE]```
python harness/run_demo.py --demo demo01_constraint_boundary --mode proof
python harness/run_demo.py --demo demo01_constraint_boundary --mode break
```[END_FENCE]```

## Pass conditions
- Proof run logs `pass: true` and decision `ACCEPT_INVARIANT_HYPOTHESIS`.
- Break run logs `pass: false` and decision `REJECT_OR_FLAG_PROJECTION`.
- Output is deterministic and schema-valid.

## Notes
This is intentionally minimal: it currently models “constraint support” with fixture booleans.  
Later versions can replace this with actual invariant extraction / hypothesis scoring.