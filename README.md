# Spanda Normative Harness

Deterministic micro-demos for validating Spanda normatives with schema-validated JSONL outputs.

## Quickstart

```bash
source .venv/bin/activate
python3 harness/run_demo.py --demo demo27_no_narrative_projection --mode proof
python3 harness/run_demo.py --demo demo27_no_narrative_projection --mode break
```

## Run all demos

```bash
source .venv/bin/activate
for d in demos/*; do
  demo_id="$(basename "$d")"
  python3 harness/run_demo.py --demo "$demo_id" --mode proof
  python3 harness/run_demo.py --demo "$demo_id" --mode break
done
```

## Normatives coverage

Paper 8 (Spanda architectural documentation) — Normative Spec v0.2 — DOI: 10.5281/zenodo.18791708
https://doi.org/10.5281/zenodo.18791708

N01–N30 are currently covered by 31 demos (N11 has two demos).

## Determinism contract

- No network calls in demo logic.
- No randomness in demo logic.
- Same fixture input must produce identical output behavior.
- Output events are validated against `harness/schema.json`.
- Every demo result must include explicit `rationale` and `evidence`.

## Repo structure

```text
.
├── harness/      # deterministic runner + JSON schema
├── demos/        # one folder per micro-demo (proof.json, break.json, demo.py, README.md)
├── normatives/   # normative references and mapping notes
├── logs/         # local-only generated JSONL outputs
└── tasks/        # local-only scratchpad (not tracked)
```

## Notes

- `logs/` contains generated deterministic JSONL outputs and is local-only.
- `tasks/` is a local-only scratchpad and is not tracked.

## License

This project is licensed under **Creative Commons Attribution–NonCommercial 4.0 International (CC BY-NC 4.0)**.  
See the [`LICENSE`](LICENSE) file for details.

## Contact

- GitHub: **@putmanmodel**
- Email: **putmanmodel@pm.me**
- BlueSky: **@putmanmodel.bsky.social**
- X / Twitter: **@putmanmodel**
- Reddit: **u/putmanmodel**
