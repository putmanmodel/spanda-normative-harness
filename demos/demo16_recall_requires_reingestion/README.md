# demo16_recall_requires_reingestion

**Normative:** N28  
**Goal:** Require re-ingestion before recall-derived signals can be promoted.

## Invariant
Recall-derived signals MUST be re-ingested as a new Event before promotion predicates can be satisfied.
If `source == "RECALL"` and `reingested == false`, promotion is rejected.

## Rules
- If `promotion_requested` is `false`: `allowed = true`
- If `promotion_requested` is `true`:
  - If `source == "RECALL"` and `reingested == false`: `allowed = false`
  - Else: `allowed = true`

## Decision mapping
- `ALLOW_PROMOTION` if allowed
- `REJECT_PROMOTION_RECALL_NOT_REINGESTED` if not allowed

## Fixtures
- `proof.json`
  - `source: RECALL`, `reingested: true`, `promotion_requested: true`
  - Expected: `allowed: true`
- `break.json`
  - `source: RECALL`, `reingested: false`, `promotion_requested: true`
  - Expected: `allowed: false`

## Run
```bash
python3 harness/run_demo.py --demo demo16_recall_requires_reingestion --mode proof
python3 harness/run_demo.py --demo demo16_recall_requires_reingestion --mode break
```

## Pass condition
`pass` is true iff `allowed == expected_allowed`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
