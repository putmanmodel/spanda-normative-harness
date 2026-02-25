# demo06_irreversible_requires_contract

**Normative ID:** N11

**Invariant:**
Irreversible actions MUST require a valid contract token.
If `valid_contract` is false for an irreversible action, the action is rejected.

## Fixture expectations
- `proof.json`
  - `irreversible: true`, `valid_contract: true`, `expected_allowed: true`
  - Expected decision: `ALLOW_ACTION`, `pass: true`
- `break.json`
  - `irreversible: true`, `valid_contract: false`, `expected_allowed: false`
  - Expected decision: `REJECT_ACTION_NO_CONTRACT`, `pass: true`

## Run commands
```
python3 harness/run_demo.py --demo demo06_irreversible_requires_contract --mode proof
python3 harness/run_demo.py --demo demo06_irreversible_requires_contract --mode break
```
