# DEMO_MAP

Authoritative mapping between normatives (`N01`–`N30`) and implemented demos in `/demos`.

## How To Run A Demo

```bash
source .venv/bin/activate
python3 harness/run_demo.py --demo demo27_no_narrative_projection --mode proof
python3 harness/run_demo.py --demo demo27_no_narrative_projection --mode break
```

## Normative -> Demo(s)

| Normative | Demo(s) |
|---|---|
| N01 | demo01_constraint_boundary |
| N02 | demo27_no_narrative_projection |
| N03 | demo28_gated_dimensional_expansion |
| N04 | demo29_invariant_based_embodiment_transfer |
| N05 | demo30_stratified_persistence_required |
| N06 | demo02_pressure_viscosity_assimilation |
| N07 | demo05_residual_activation_bounded |
| N08 | demo31_identity_as_multiplier |
| N09 | demo12_dimension_expansion_declared |
| N10 | demo25_dissipation_required |
| N11 | demo06_irreversible_requires_contract, demo26_asymmetric_influence_measurable |
| N12 | demo09_cross_tier_write_requires_gate |
| N13 | demo22_drift_inputs_must_be_accessible |
| N14 | demo07_memory_write_requires_provenance |
| N15 | demo23_scope_stratified_baselines |
| N16 | demo10_baseline_update_requires_stability_window |
| N17 | demo24_rationale_artifact_required |
| N18 | demo04_guarded_update_freeze |
| N19 | demo21_tvs_strict_resolution |
| N20 | demo14_commit_class_enforcement |
| N21 | demo11_evidence_supports_decision |
| N22 | demo03_reflex_non_persistent |
| N23 | demo18_reflex_expiry |
| N24 | demo19_reflex_forwards_governance_decides |
| N25 | demo08_no_silent_prior_drift |
| N26 | demo13_action_budget_cap |
| N27 | demo15_recall_attention_only |
| N28 | demo16_recall_requires_reingestion |
| N29 | demo17_transition_log_required_fields |
| N30 | demo20_post_instability_stabilization_window |

## Demo -> Normative(s)

| Demo | Normative(s) |
|---|---|
| demo01_constraint_boundary | N01 |
| demo02_pressure_viscosity_assimilation | N06 |
| demo03_reflex_non_persistent | N22 |
| demo04_guarded_update_freeze | N18 |
| demo05_residual_activation_bounded | N07 |
| demo06_irreversible_requires_contract | N11 |
| demo07_memory_write_requires_provenance | N14 |
| demo08_no_silent_prior_drift | N25 |
| demo09_cross_tier_write_requires_gate | N12 |
| demo10_baseline_update_requires_stability_window | N16 |
| demo11_evidence_supports_decision | N21 |
| demo12_dimension_expansion_declared | N09 |
| demo13_action_budget_cap | N26 |
| demo14_commit_class_enforcement | N20 |
| demo15_recall_attention_only | N27 |
| demo16_recall_requires_reingestion | N28 |
| demo17_transition_log_required_fields | N29 |
| demo18_reflex_expiry | N23 |
| demo19_reflex_forwards_governance_decides | N24 |
| demo20_post_instability_stabilization_window | N30 |
| demo21_tvs_strict_resolution | N19 |
| demo22_drift_inputs_must_be_accessible | N13 |
| demo23_scope_stratified_baselines | N15 |
| demo24_rationale_artifact_required | N17 |
| demo25_dissipation_required | N10 |
| demo26_asymmetric_influence_measurable | N11 |
| demo27_no_narrative_projection | N02 |
| demo28_gated_dimensional_expansion | N03 |
| demo29_invariant_based_embodiment_transfer | N04 |
| demo30_stratified_persistence_required | N05 |
| demo31_identity_as_multiplier | N08 |

## Totals

- TOTAL normatives covered: 30
- TOTAL demos: 31

## Notes

- N11 has two demos: `demo06_irreversible_requires_contract` and `demo26_asymmetric_influence_measurable`.
