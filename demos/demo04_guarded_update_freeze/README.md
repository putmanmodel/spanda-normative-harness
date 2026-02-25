# demo04_guarded_update_freeze

**Normative:** N18  
**Goal:** Prove baseline adaptation is suppressed under instability (“freeze mode”).

## What this demo asserts
- If `instability: true` → baseline MUST NOT change (freeze).
- If `instability: false` → baseline MAY update using `proposed_updates`.

## Fixtures
- `proof.json`
  - instability true, proposed updates present
  - Expected: decision `FREEZE_BASELINE`, `pass: true`, baseline unchanged
- `break.json`
  - instability false, proposed updates present
  - Expected: decision `APPLY_BASELINE_UPDATE`, `pass: true`, baseline changed

## Run
```
python harness/run_demo.py --demo demo04_guarded_update_freeze --mode proof
python harness/run_demo.py --demo demo04_guarded_update_freeze --mode break
```

## Pass conditions
- Proof run: baseline unchanged; decision `FREEZE_BASELINE`.
- Break run: baseline changed; decision `APPLY_BASELINE_UPDATE`.
- Output is deterministic and schema-valid.

## Notes
This demo isolates the governance invariant: instability gates learning/adaptation. Full systems can layer richer instability criteria later.