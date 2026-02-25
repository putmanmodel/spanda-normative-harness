# Runner

Goal: run any demo deterministically and write JSONL logs to /logs.

Contract:
- Each demo folder contains:
  - proof.json
  - break.json
  - demo.py (or demo.ts) entrypoint
- Runner loads fixture, computes fixture_hash, invokes demo, validates output, writes log line.

Next step: we’ll add a small runner script (Python or Node) once you pick a language.
