# demo02_pressure_viscosity_assimilation

**Normative:** N06  
**Goal:** Prove ME→US assimilation is **pressure-gated** and **viscosity-modulated**.

## What this demo asserts
Consolidation occurs only if:
- `pressure >= pressure_threshold`
- AND `exposures >= viscosity_exposure_min`

This models:
- **pressure** = salience/intensity at the moment
- **viscosity** = resistance to tier transfer, requiring repeat exposures

## Fixtures
- `proof.json`
  - pressure high + exposures sufficient
  - Expected: **CONSOLIDATE_ME_TO_US**, `pass: true`
- `break.json`
  - pressure low (even with high exposures)
  - Expected: **DO_NOT_CONSOLIDATE**, `pass: true`

## Run
```
python harness/run_demo.py --demo demo02_pressure_viscosity_assimilation --mode proof
python harness/run_demo.py --demo demo02_pressure_viscosity_assimilation --mode break
```

## Pass conditions
- The demo’s computed `should_consolidate` must match `expected_consolidate`.
- Logs must be deterministic and schema-valid.

## Notes
This is a “unit brick” demo. It intentionally avoids full memory structures and focuses only on the gating invariant.