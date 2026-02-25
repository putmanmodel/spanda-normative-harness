# demo25_dissipation_required

**Normative:** N10  
**Goal:** Enforce dissipation-aware risk flagging under coupling pressure.

## Invariant
The system MUST model dissipation capacity.
Strong coupling without sufficient dissipation MUST be flagged as risk.

## Rules
- `risk_score = coupling_strength - dissipation_capacity`
- `risk_flagged = (risk_score > risk_threshold)`

## Decision mapping
- `RISK_FLAGGED` if `risk_flagged`
- `NO_RISK` otherwise

## Fixtures
- `proof.json`
  - Values chosen so `risk_flagged` is false
- `break.json`
  - Values chosen so `risk_flagged` is true

## Run
```bash
python3 harness/run_demo.py --demo demo25_dissipation_required --mode proof
python3 harness/run_demo.py --demo demo25_dissipation_required --mode break
```

## Pass condition
`pass` is true iff `risk_flagged == expected_risk_flagged`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
