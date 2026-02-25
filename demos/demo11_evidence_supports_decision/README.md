# demo11_evidence_supports_decision

**Normative:** N21  
**Goal:** Verify that the claimed decision is logically supported by evidence fields.

## Invariant
A decision MUST be supported by its evidence.
If the claimed decision contradicts evidence, it must be flagged as unsupported.

## Rules
- Supported iff:
  - `claimed_decision == "ALLOW_ACTION"` and `evidence.allowed == true`, or
  - `claimed_decision == "REJECT_ACTION"` and `evidence.allowed == false`
- Any other `claimed_decision` => `supported = false`

## Decision mapping
- `EVIDENCE_SUPPORTS_DECISION` if supported
- `EVIDENCE_CONTRADICTS_DECISION` if unsupported

## Fixtures
- `proof.json`
  - `claimed_decision: ALLOW_ACTION`
  - `evidence.allowed: true`
  - `expected_supported: true`
- `break.json`
  - `claimed_decision: ALLOW_ACTION`
  - `evidence.allowed: false`
  - `expected_supported: false`

## Run
```bash
python3 harness/run_demo.py --demo demo11_evidence_supports_decision --mode proof
python3 harness/run_demo.py --demo demo11_evidence_supports_decision --mode break
```

## Pass condition
`pass` is true iff `supported == expected_supported`.

## Determinism
No randomness, no network calls, fixture-only deterministic behavior.
