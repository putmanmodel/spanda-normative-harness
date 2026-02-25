# demo19_reflex_forwards_governance_decides

**Normative:** N24  
**Goal:** Ensure reflex forwarding does not auto-authorize governance action.

## Invariant
Reflex MAY forward a signal, but governance must independently decide on action.
Reflex forwarding must not grant action unless governance approval is true.

## Rules
- `forwarded = (reflex_triggered and forward_requested)`
- `action_allowed = governance_approved`

## Decision mapping
- `FORWARD_AND_ALLOW_ACTION` if forwarded and action allowed
- `FORWARD_ONLY_GOVERNANCE_PENDING` if forwarded and not action allowed
- `ALLOW_ACTION_NO_FORWARD` if not forwarded and action allowed
- `NO_FORWARD_NO_ACTION` otherwise

## Fixtures
- `proof.json`
  - `reflex_triggered: true`, `forward_requested: true`, `governance_approved: true`
  - Expected: `forwarded: true`, `action_allowed: true`
- `break.json`
  - `reflex_triggered: true`, `forward_requested: true`, `governance_approved: false`
  - Expected: `forwarded: true`, `action_allowed: false`

## Run
```bash
python3 harness/run_demo.py --demo demo19_reflex_forwards_governance_decides --mode proof
python3 harness/run_demo.py --demo demo19_reflex_forwards_governance_decides --mode break
```

## Pass condition
`pass` is true iff:
- `forwarded == expected_forwarded`, and
- `action_allowed == expected_action_allowed`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
