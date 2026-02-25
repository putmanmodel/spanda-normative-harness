# demo03_reflex_non_persistent

**Normative:** N22  
**Goal:** Prove reflex events are **non-persistent** and cannot trigger irreversible actions.

## What this demo asserts
When `reflex_triggered: true`, reflex MUST NOT:
- write memory (`memory_writes`)
- update baselines (`baseline_updates`)
- modify priors (`prior_updates`)
- trigger irreversible actions (`irreversible_actions`)

## Fixtures
- `proof.json`
  - reflex triggered
  - attempted forbidden mutations are empty
  - Expected: **REFLEX_FLAG_ONLY**, `pass: true`
- `break.json`
  - reflex triggered
  - attempted includes forbidden items (e.g., memory write, baseline update, irreversible action)
  - Expected: **REFLEX_VIOLATION_REJECTED**, `pass: true` (i.e., the demo correctly flags/rejects)

## Run
```
python harness/run_demo.py --demo demo03_reflex_non_persistent --mode proof
python harness/run_demo.py --demo demo03_reflex_non_persistent --mode break
```

## Pass conditions
- Proof run: no violations detected; decision is `REFLEX_FLAG_ONLY`.
- Break run: violations detected; decision is `REFLEX_VIOLATION_REJECTED`.
- Output is deterministic and schema-valid.

## Notes
This demo treats “reflex” as an attention-only pathway. Any persistent mutation attempt is a hard violation.