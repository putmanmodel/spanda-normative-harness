# demo09_cross_tier_write_requires_gate

**Normative:** N12  
**Goal:** Require explicit gate signal for cross-tier memory writes.

## Invariant
Writes between memory tiers MUST require an explicit gate signal.
If `gate_open` is `false`, cross-tier write is rejected and no transfer occurs.

## Rules
- If `cross_tier` is `false`: `transferred = false`.
- If `cross_tier` is `true`:
  - `gate_open: true` -> `transferred = true`
  - `gate_open: false` -> `transferred = false`

## Decision mapping
- `TRANSFER_ALLOWED` if transferred is true
- `REJECT_CROSS_TIER_NO_GATE` if cross-tier attempted with gate closed
- `NO_TRANSFER_SAME_TIER` if no cross-tier operation

## Fixtures
- `proof.json`
  - `cross_tier: true`, `gate_open: true`, `expected_transferred: true`
- `break.json`
  - `cross_tier: true`, `gate_open: false`, `expected_transferred: false`

## Run
```bash
python3 harness/run_demo.py --demo demo09_cross_tier_write_requires_gate --mode proof
python3 harness/run_demo.py --demo demo09_cross_tier_write_requires_gate --mode break
```

## Pass condition
`pass` is true iff `transferred == expected_transferred`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
