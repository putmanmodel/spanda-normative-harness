# NORMATIVES

## How this is used

- Each normative is validated by a demo with both `proof.json` and `break.json` fixtures.
- The harness runs demos and emits deterministic JSONL logs.
- `PROVEN` in this file means the mapped demo currently passes both proof and break modes.

## N01 — Constraint-Bound Hypothesis Acceptance
Hypotheses MUST be accepted only when they are supported by invariant boundary effects. Explanations without invariant grounding MUST be rejected or flagged.
Implementation: PROVEN (demo01_constraint_boundary)

## N02 — No Narrative Projection Without Invariants
The system MUST NOT attribute intention, agency, or purpose without invariant support. Unsupported attribution MUST be flagged as projection.
Implementation: PROVEN (demo27_no_narrative_projection)

## N03 — Gated Dimensional Expansion
Latent dimensions MAY be introduced only when they reduce inconsistency and are traceable to constraint-accessible invariants. Silent dimensional expansion MUST NOT be allowed.
Implementation: PROVEN (demo28_gated_dimensional_expansion)

## N04 — Invariant-Based Embodiment Transfer
Policy transfer across embodiments MUST occur through shared invariant abstractions, not raw sensor equivalence. Raw-sensor transfer MUST be rejected.
Implementation: PROVEN (demo29_invariant_based_embodiment_transfer)

## N05 — Stratified Persistence Requirement
Temporally extended agency MUST use stratified memory layers (Surface, Intermediate, Priors). Single-layer persistence MUST be treated as non-compliant.
Implementation: PROVEN (demo30_stratified_persistence_required)

## N06 — Pressure + Viscosity Assimilation Gate
Consolidation MAY occur only when pressure and exposure (viscosity) thresholds are satisfied. If either threshold is not met, consolidation MUST NOT occur.
Implementation: PROVEN (demo02_pressure_viscosity_assimilation)

## N07 — Residual Activation Bounded
Residual activation MUST remain bounded by a cap. If an update exceeds cap, the value MUST be clamped and the clamp condition explicitly evidenced.
Implementation: PROVEN (demo05_residual_activation_bounded)

## N08 — Identity as Multiplier, Not Flag
Identity effects MUST be represented as measurable weighting/hysteresis multipliers. A metaphysical identity flag MUST NOT be used as the governing mechanism.
Implementation: PROVEN (demo31_identity_as_multiplier)

## N09 — Declared Dimension Resolution
Any dimension expansion MUST resolve against explicitly declared dimensions. Undeclared dimensions MUST be rejected.
Implementation: PROVEN (demo12_dimension_expansion_declared)

## N10 — Dissipation Capacity Requirement
The system MUST model dissipation capacity when evaluating coupling pressure. High coupling without sufficient dissipation MUST be flagged as risk.
Implementation: PROVEN (demo25_dissipation_required)

## N11 — Contract Requirement for Irreversible/Amplified Effect
Irreversible or high-impact effect paths MUST be explicitly governed and measurable. Operations lacking required governing conditions MUST be rejected.
Implementation: PROVEN (demo06_irreversible_requires_contract; demo26_asymmetric_influence_measurable)

## N12 — Cross-Tier Write Requires Gate
Cross-tier memory writes MUST require an explicit gate signal. If the gate is closed, transfer MUST NOT occur.
Implementation: PROVEN (demo09_cross_tier_write_requires_gate)

## N13 — Drift Inputs Must Be Accessible
Drift detection MUST use interaction-accessible inputs only. If inaccessible inputs are used, the drift decision MUST be rejected.
Implementation: PROVEN (demo22_drift_inputs_must_be_accessible)

## N14 — Memory Write Requires Provenance
Persistent memory writes MUST include complete provenance metadata. Missing or incomplete provenance MUST cause rejection.
Implementation: PROVEN (demo07_memory_write_requires_provenance)

## N15 — Scope-Stratified Baselines
Baseline updates MUST target supported scopes in a stratified baseline model. Unsupported scopes MUST be rejected.
Implementation: PROVEN (demo23_scope_stratified_baselines)

## N16 — Stability Window Before Baseline Update
Baseline updates MUST require a minimum stability window. Updates requested before sufficient stability MUST be rejected.
Implementation: PROVEN (demo10_baseline_update_requires_stability_window)

## N17 — Rationale Artifact Required
Governance events MUST produce rationale artifacts sufficient for deterministic replay. Missing rationale pointers MUST cause rejection.
Implementation: PROVEN (demo24_rationale_artifact_required)

## N18 — Guarded Update Freeze Under Instability
Under instability, baseline adaptation MUST be suppressed (freeze mode). Updates MAY resume only outside instability conditions.
Implementation: PROVEN (demo04_guarded_update_freeze)

## N19 — TVS Strict Resolution + Provenance
If TVS tags are used, they MUST resolve against a versioned dictionary and include provenance. Unresolved tags or missing provenance MUST be rejected.
Implementation: PROVEN (demo21_tvs_strict_resolution)

## N20 — Commit-Class Enforcement
Canonical and associative memory writes MUST remain distinct. Canonical writes MUST require explicit promotion; associative writes MAY proceed under their class.
Implementation: PROVEN (demo14_commit_class_enforcement)

## N21 — Evidence Supports Decision
A decision MUST be logically supported by its evidence fields. Contradictory evidence MUST be flagged as unsupported.
Implementation: PROVEN (demo11_evidence_supports_decision)

## N22 — Reflex Non-Persistent Constraint
Reflex handling MUST remain non-persistent by default. Reflex pathways MUST NOT directly commit persistent state without separate governance.
Implementation: PROVEN (demo03_reflex_non_persistent)

## N23 — Reflex Expiry Requirement
Reflex events MUST expire unless re-triggered under short-horizon conditions. Expired reflex state MUST be deactivated automatically.
Implementation: PROVEN (demo18_reflex_expiry)

## N24 — Reflex Forwards, Governance Decides
Reflex MAY forward a signal, but governance MUST independently authorize action. Reflex forwarding alone MUST NOT grant action authority.
Implementation: PROVEN (demo19_reflex_forwards_governance_decides)

## N25 — No Silent Prior Drift
Priors MUST NOT change unless an explicit prior-update path is invoked. Silent drift attempts MUST be rejected and priors preserved.
Implementation: PROVEN (demo08_no_silent_prior_drift)

## N26 — Action Budget Cap
Per-cycle action execution MUST be bounded by a budget cap. Excess requested actions MUST be clamped or denied.
Implementation: PROVEN (demo13_action_budget_cap)

## N27 — Recall Is Attention-Only
Recall MUST NOT mutate canonical memory, baselines, priors, or authorize irreversible action. Side-effect attempts during recall MUST be rejected.
Implementation: PROVEN (demo15_recall_attention_only)

## N28 — Recall Requires Re-ingestion for Promotion
Recall-derived signals MUST be re-ingested as new events before promotion predicates are satisfied. Non-reingested recall promotion MUST be rejected.
Implementation: PROVEN (demo16_recall_requires_reingestion)

## N29 — Transition Log Required Fields
Canonical transitions MUST emit required log fields (`timestamp`, `event_ids`, `predicate_vector`, `governance_token`, `signer_tag`). Missing or empty required fields MUST cause rejection.
Implementation: PROVEN (demo17_transition_log_required_fields)

## N30 — Post-Instability Stabilization Window
After instability, baseline updates MUST wait for a bounded stabilization window. Update requests inside that window MUST be rejected.
Implementation: PROVEN (demo20_post_instability_stabilization_window)
