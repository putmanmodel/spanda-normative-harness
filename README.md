# Spanda Normative POW

Deterministic micro-demos that prove (and falsify) architectural normatives.

Core idea:
- Normatives = testable MUST/MUST NOT rules
- Each demo has a proof fixture + a break fixture
- Output is deterministic, replayable, and logged

## Repo layout
- normatives/ : normative specs + demo map
- harness/    : log schema + runner
- demos/      : one folder per demo
- fixtures/   : shared fixtures (optional)
- logs/       : generated outputs (local)
