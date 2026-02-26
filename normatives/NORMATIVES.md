# NORMATIVES

## How this is used

- Each normative is validated by a demo with both `proof.json` and `break.json` fixtures.
- The harness runs demos and emits deterministic JSONL logs.
- `PROVEN` in this file means the mapped demo currently passes both proof and break modes.

## Conformance Envelope

- Required envelope fields (present in every proof/break JSONL record): `decision`, `demo_id`, `evidence`, `fixture_hash`, `fixture_path`, `mode`, `normative_ids`, `pass`, `rationale`, `timestamp_utc`.
- Optional top-level envelope fields beyond the required envelope: none (the harness emits a fixed envelope).
- Demo-specific information appears as additional `key:value` entries inside `evidence` (tokens MAY vary by demo/fixture).

## N01 — Constraint-Bound Hypothesis Acceptance
Hypotheses MUST be accepted only when they are supported by invariant boundary effects. Explanations without invariant grounding MUST be rejected or flagged.
Observable: Record MUST include the required envelope fields. Acceptance (`decision=ACCEPT_INVARIANT_HYPOTHESIS`) MUST include invariant-evidence tokens (at minimum: one `boundary_effect:*` token and one `constraint_surface:*` token). When evidence indicates no invariants (e.g., includes `no_boundary_invariants_observed`), the system MUST NOT accept and MUST emit a non-accepting decision (reject/flag).
Implementation: PROVEN (demo01_constraint_boundary)

## N02 — No Narrative Projection Without Invariants
The system MUST NOT attribute intention, agency, or purpose without invariant support. Unsupported attribution MUST be flagged as projection.
Observable: Record MUST include the required envelope fields. Proof MUST emit `decision=ACCEPT_HYPOTHESIS` with evidence tokens `invariant_support:true`, `accepted:true`, and `flagged_projection:false`. Break MUST emit `decision=FLAG_PROJECTION` with evidence tokens `invariant_support:false`, `accepted:false`, and `flagged_projection:true`.
Implementation: PROVEN (demo27_no_narrative_projection)

## N03 — Gated Dimensional Expansion
Latent dimensions MAY be introduced only when they reduce inconsistency and are traceable to constraint-accessible invariants. Silent dimensional expansion MUST NOT be allowed.
Observable: Record MUST include the required envelope fields. Proof MUST allow dimension introduction only when evidence indicates traceability to invariants (`traceable_to_invariants:true`). Break MUST reject when evidence indicates traceability is absent (`traceable_to_invariants:false`) or when expansion would be silent/unsupported; in break the system MUST NOT allow.
Implementation: PROVEN (demo28_gated_dimensional_expansion)

## N04 — Invariant-Based Embodiment Transfer
Policy transfer across embodiments MUST occur through shared invariant abstractions, not raw sensor equivalence. Raw-sensor transfer MUST be rejected.
Observable: Record MUST include the required envelope fields. Proof MUST allow policy transfer only when evidence indicates `transfer_method:INVARIANT_ABSTRACTION`. Break MUST reject when evidence indicates `transfer_method:RAW_SENSOR_EQUIVALENCE`; in break the system MUST NOT allow.
Implementation: PROVEN (demo29_invariant_based_embodiment_transfer)

## N05 — Stratified Persistence Requirement
Temporally extended agency MUST use stratified memory layers (Surface, Intermediate, Priors). Single-layer persistence MUST be treated as non-compliant.
Observable: Record MUST include the required envelope fields. Proof MUST be compliant only when evidence indicates all required layers are present (`layers_present` includes Surface, Intermediate, Priors) and `missing_layers:none`. Break MUST be non-compliant when evidence indicates any required layer is missing (i.e., `missing_layers` is not `none`).
Implementation: PROVEN (demo30_stratified_persistence_required)

## N06 — Pressure + Viscosity Assimilation Gate
Consolidation MAY occur only when pressure and exposure (viscosity) thresholds are satisfied. If either threshold is not met, consolidation MUST NOT occur.
Observable: Record MUST include the required envelope fields. Proof MAY consolidate only when evidence includes `pressure`, `pressure_threshold`, `exposures`, and `viscosity_exposure_min`, and the relational conditions hold: `pressure >= pressure_threshold` AND `exposures >= viscosity_exposure_min`. Break MUST NOT consolidate when either relational condition is false, and MUST emit a non-consolidation decision.
Implementation: PROVEN (demo02_pressure_viscosity_assimilation)

## N07 — Residual Activation Bounded
Residual activation MUST remain bounded by a cap. If an update exceeds cap, the value MUST be clamped and the clamp condition explicitly evidenced.
Observable: Record MUST include the required envelope fields. Proof MUST apply residual updates when within cap and MUST evidence `residual_clamped:false`. Break MUST clamp when an update would exceed the cap, MUST evidence `residual_clamped:true`, and the post-update residual (`residual_after`) MUST equal the cap value when clamped.
Implementation: PROVEN (demo05_residual_activation_bounded)

## N08 — Identity as Multiplier, Not Flag
Identity effects MUST be represented as measurable weighting/hysteresis multipliers. A metaphysical identity flag MUST NOT be used as the governing mechanism.
Observable: Record MUST include the required envelope fields. Proof MUST be compliant only when evidence indicates identity is represented via multiplier/hysteresis and `identity_flag_used:false`. Break MUST be non-compliant when evidence indicates a governing identity flag was used (`identity_flag_used:true`).
Implementation: PROVEN (demo31_identity_as_multiplier)

## N09 — Declared Dimension Resolution
Any dimension expansion MUST resolve against explicitly declared dimensions. Undeclared dimensions MUST be rejected.
Observable: Record MUST include the required envelope fields. Proof MUST allow only when evidence indicates `undeclared_dimensions:none`. Break MUST reject when evidence indicates any undeclared dimension is present (i.e., `undeclared_dimensions` is not `none`).
Implementation: PROVEN (demo12_dimension_expansion_declared)

## N10 — Dissipation Capacity Requirement
The system MUST model dissipation capacity when evaluating coupling pressure. High coupling without sufficient dissipation MUST be flagged as risk.
Observable: Record MUST include the required envelope fields. Proof MUST NOT flag risk when evidence indicates coupling is within dissipation capacity (risk not flagged). Break MUST flag risk when evidence indicates high coupling without sufficient dissipation (risk flagged). Numeric `risk_score` values MUST NOT be treated as normative constants; only the risk/no-risk classification is normative.
Implementation: PROVEN (demo25_dissipation_required)

## N11 — Contract Requirement for Irreversible/Amplified Effect
Irreversible or high-impact effect paths MUST be explicitly governed and measurable. Operations lacking required governing conditions MUST be rejected.
Observable: N11a (demo06) — Proof MUST allow irreversible/high-impact action only when evidence indicates `valid_contract:true`; break MUST reject when `valid_contract:false`. N11b (demo26) — When influence is measured, the record MUST include amplification measurables (e.g., `amplified:true|false` and `effective_influence:*` when amplified); break MUST not omit measurable amplification when amplification is asserted.
Implementation: PROVEN (demo06_irreversible_requires_contract; demo26_asymmetric_influence_measurable)

## N12 — Cross-Tier Write Requires Gate
Cross-tier memory writes MUST require an explicit gate signal. If the gate is closed, transfer MUST NOT occur.
Observable: Record MUST include the required envelope fields. Proof MUST transfer only when evidence indicates `cross_tier:true` AND `gate_open:true`. Break MUST reject cross-tier transfer when `gate_open:false`, and MUST evidence `transferred:false` in break.
Implementation: PROVEN (demo09_cross_tier_write_requires_gate)

## N13 — Drift Inputs Must Be Accessible
Drift detection MUST use interaction-accessible inputs only. If inaccessible inputs are used, the drift decision MUST be rejected.
Observable: Record MUST include the required envelope fields. Proof MUST allow drift decisions only when evidence indicates `blocked_inputs:none`. Break MUST reject when evidence indicates any inaccessible input was used (i.e., `blocked_inputs` is not `none`).
Implementation: PROVEN (demo22_drift_inputs_must_be_accessible)

## N14 — Memory Write Requires Provenance
Persistent memory writes MUST include complete provenance metadata. Missing or incomplete provenance MUST cause rejection.
Observable: Record MUST include the required envelope fields. Proof MUST allow writes only when evidence indicates `provenance_missing_keys:none`. Break MUST reject when evidence indicates any required provenance key is missing (i.e., `provenance_missing_keys` is not `none`).
Implementation: PROVEN (demo07_memory_write_requires_provenance)

## N15 — Scope-Stratified Baselines
Baseline updates MUST target supported scopes in a stratified baseline model. Unsupported scopes MUST be rejected.
Observable: Record MUST include the required envelope fields. Evidence MUST include `supported_scopes:*` and `requested_scope:*` for any scope update attempt. Proof MUST allow when `requested_scope` is within `supported_scopes` and MUST evidence `allowed:true`. Break MUST reject when `requested_scope` is not within `supported_scopes` and MUST evidence `allowed:false` (fixtures MAY use an example unsupported scope such as `org`).
Implementation: PROVEN (demo23_scope_stratified_baselines)

## N16 — Stability Window Before Baseline Update
Baseline updates MUST require a minimum stability window. Updates requested before sufficient stability MUST be rejected.
Observable: Record MUST include the required envelope fields. Proof MUST apply baseline updates only when evidence indicates `stable_steps >= stability_required`. Break MUST reject when evidence indicates `stable_steps < stability_required` and MUST evidence `applied:false`.
Implementation: PROVEN (demo10_baseline_update_requires_stability_window)

## N17 — Rationale Artifact Required
Governance events MUST produce rationale artifacts sufficient for deterministic replay. Missing rationale pointers MUST cause rejection.
Observable: Record MUST include the required envelope fields. Proof MUST allow governance events only when evidence indicates rationale is present (`rationale_present:true`). Break MUST reject when rationale is missing (`rationale_present:false`).
Implementation: PROVEN (demo24_rationale_artifact_required)

## N18 — Guarded Update Freeze Under Instability
Under instability, baseline adaptation MUST be suppressed (freeze mode). Updates MAY resume only outside instability conditions.
Observable: Record MUST include the required envelope fields. Under instability (`instability:true`), the system MUST freeze/suppress baseline updates (freeze decision). When not unstable (`instability:false`), updates MAY proceed subject to other constraints.
Implementation: PROVEN (demo04_guarded_update_freeze)

## N19 — TVS Strict Resolution + Provenance
If TVS tags are used, they MUST resolve against a versioned dictionary and include provenance. Unresolved tags or missing provenance MUST be rejected.
Observable: Record MUST include the required envelope fields. Proof MUST allow TVS tags only when evidence indicates a versioned dictionary (`dictionary_version:*`), no unresolved tags (`unresolved:none`), and provenance present. Break MUST reject when evidence indicates any unresolved tag (i.e., `unresolved` is not `none`) OR missing provenance; in break the system MUST NOT allow.
Implementation: PROVEN (demo21_tvs_strict_resolution)

## N20 — Commit-Class Enforcement
Canonical and associative memory writes MUST remain distinct. Canonical writes MUST require explicit promotion; associative writes MAY proceed under their class.
Observable: Record MUST include the required envelope fields. Canonical writes MUST require explicit promotion evidence (`promotion_explicit:true`). Break MUST reject canonical writes when promotion is not explicit (`promotion_explicit:false`).
Implementation: PROVEN (demo14_commit_class_enforcement)

## N21 — Evidence Supports Decision
A decision MUST be logically supported by its evidence fields. Contradictory evidence MUST be flagged as unsupported.
Observable: Record MUST include the required envelope fields. Proof MUST mark the decision as supported when evidence indicates `evidence_allowed:true` and `supported:true`. Break MUST flag contradiction/unsupported when evidence indicates `evidence_allowed:false` and `supported:false` for the same claimed decision; in break the system MUST NOT treat the claim as supported.
Implementation: PROVEN (demo11_evidence_supports_decision)

## N22 — Reflex Non-Persistent Constraint
Reflex handling MUST remain non-persistent by default. Reflex pathways MUST NOT directly commit persistent state without separate governance.
Observable: Record MUST include the required envelope fields. Proof MUST emit a reflex-only outcome (no persistence/effects) when reflex triggers. Break MUST reject if evidence indicates any forbidden side-effect category during reflex (e.g., tokens indicating memory writes, baseline updates, or irreversible actions).
Implementation: PROVEN (demo03_reflex_non_persistent)

## N23 — Reflex Expiry Requirement
Reflex events MUST expire unless re-triggered under short-horizon conditions. Expired reflex state MUST be deactivated automatically.
Observable: Record MUST include the required envelope fields. Proof MUST keep reflex active when evidence indicates `age_steps <= ttl_steps`. Break MUST expire reflex when evidence indicates `age_steps > ttl_steps`, and MUST evidence `reflex_active_after:false` when expired.
Implementation: PROVEN (demo18_reflex_expiry)

## N24 — Reflex Forwards, Governance Decides
Reflex MAY forward a signal, but governance MUST independently authorize action. Reflex forwarding alone MUST NOT grant action authority.
Observable: Record MUST include the required envelope fields. Proof MUST allow action only when both `forwarded:true` and `governance_approved:true` are evidenced. Break MUST NOT allow action when `governance_approved:false`, even if `forwarded:true`.
Implementation: PROVEN (demo19_reflex_forwards_governance_decides)

## N25 — No Silent Prior Drift
Priors MUST NOT change unless an explicit prior-update path is invoked. Silent drift attempts MUST be rejected and priors preserved.
Observable: Record MUST include the required envelope fields. Proof MUST preserve priors when no explicit update path is invoked (`explicit_update:false`) and no drift is attempted. Break MUST reject when drift is attempted without an explicit update path (`explicit_update:false` AND `drift_attempted:true`).
Implementation: PROVEN (demo08_no_silent_prior_drift)

## N26 — Action Budget Cap
Per-cycle action execution MUST be bounded by a budget cap. Excess requested actions MUST be clamped or denied.
Observable: Record MUST include the required envelope fields. Proof MUST execute within budget when `requested_count <= budget_cap`. Break MUST clamp or deny when `requested_count > budget_cap`, and MUST evidence `executed_count <= budget_cap` with `clamped:true` when clamped.
Implementation: PROVEN (demo13_action_budget_cap)

## N27 — Recall Is Attention-Only
Recall MUST NOT mutate canonical memory, baselines, priors, or authorize irreversible action. Side-effect attempts during recall MUST be rejected.
Observable: Record MUST include the required envelope fields. During recall, proof MUST show no mutation attempt and no authorization of irreversible actions. Break MUST reject if evidence indicates any attempted mutation or effect authorization during recall.
Implementation: PROVEN (demo15_recall_attention_only)

## N28 — Recall Requires Re-ingestion for Promotion
Recall-derived signals MUST be re-ingested as new events before promotion predicates are satisfied. Non-reingested recall promotion MUST be rejected.
Observable: Record MUST include the required envelope fields. Proof MUST allow promotion of recall-derived signals only when evidence indicates `reingested:true`. Break MUST reject when `reingested:false` for recall-derived promotion attempts.
Implementation: PROVEN (demo16_recall_requires_reingestion)

## N29 — Transition Log Required Fields
Canonical transitions MUST emit required log fields (`timestamp`, `event_ids`, `predicate_vector`, `governance_token`, `signer_tag`). Missing or empty required fields MUST cause rejection.
Observable: Record MUST include the required envelope fields. Proof MUST allow only when evidence indicates `missing_fields:none` for the required transition log fields. Break MUST reject when evidence indicates any required field is missing (i.e., `missing_fields` is not `none`).
Implementation: PROVEN (demo17_transition_log_required_fields)

## N30 — Post-Instability Stabilization Window
After instability, baseline updates MUST wait for a bounded stabilization window. Update requests inside that window MUST be rejected.
Observable: Record MUST include the required envelope fields. Proof MUST allow baseline updates only when evidence indicates `steps_since_instability >= stabilization_window`. Break MUST reject when evidence indicates `steps_since_instability < stabilization_window`.
Implementation: PROVEN (demo20_post_instability_stabilization_window)
