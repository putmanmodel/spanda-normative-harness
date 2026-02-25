# demo27_no_narrative_projection

**Normative:** N02  
**Goal:** Reject intention/agency narratives unless invariant support exists.

## Invariant
The system MUST NOT attribute intention/agency/purpose without invariant support.
Unsupported attributions MUST be flagged as projection.

## Rules
- If `invariant_support` is `true`:
  - `accepted = true`
  - `flagged_projection = false`
  - `decision = ACCEPT_HYPOTHESIS`
- Else:
  - `accepted = false`
  - `flagged_projection = true`
  - `decision = FLAG_PROJECTION`

## Fixtures
- `proof.json`
  - `invariant_support: true`
  - Expected: accepted hypothesis, not flagged projection
- `break.json`
  - `invariant_support: false`
  - Expected: rejected hypothesis, flagged projection

## Run
```bash
python3 harness/run_demo.py --demo demo27_no_narrative_projection --mode proof
python3 harness/run_demo.py --demo demo27_no_narrative_projection --mode break
```

## Pass condition
`pass` is true iff:
- `accepted == expected_accepted`, and
- `flagged_projection == expected_flagged_projection`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
