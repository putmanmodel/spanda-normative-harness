# demo14_commit_class_enforcement

**Normative:** N20  
**Goal:** Enforce separation between associative and canonical writes.

## Invariant
Canonical vs associative memory MUST remain distinct.
A request marked `commit_class="CANONICAL"` is rejected unless `promotion_explicit` is true.
Associative writes are always allowed.

## Rules
- If `commit_class == "ASSOCIATIVE"`: `allowed = true`
- If `commit_class == "CANONICAL"`: `allowed = (promotion_explicit == true)`

## Decision mapping
- `ALLOW_ASSOCIATIVE_WRITE` if `commit_class` is ASSOCIATIVE
- `ALLOW_CANONICAL_WRITE` if `commit_class` is CANONICAL and allowed
- `REJECT_CANONICAL_NO_PROMOTION` if `commit_class` is CANONICAL and not allowed

## Fixtures
- `proof.json`
  - `commit_class: CANONICAL`
  - `promotion_explicit: true`
  - `expected_allowed: true`
- `break.json`
  - `commit_class: CANONICAL`
  - `promotion_explicit: false`
  - `expected_allowed: false`

## Run
```bash
python3 harness/run_demo.py --demo demo14_commit_class_enforcement --mode proof
python3 harness/run_demo.py --demo demo14_commit_class_enforcement --mode break
```

## Pass condition
`pass` is true iff `allowed == expected_allowed`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
