# AGENTS.md (Codex / automation guidance)

This repo is a deterministic Proof-of-Work harness for Spanda normatives.

Hard rules:
1) Deterministic output only.
   - No network calls.
   - No randomness unless explicitly seeded in fixture.
   - Same fixture => identical log output.
2) One demo per task.
   - Keep demos isolated; do not create cross-demo dependencies.
3) Every demo MUST have:
   - proof.json fixture
   - break.json fixture
   - a demo runner entrypoint
   - JSONL log output that validates against harness/schema.json
4) Never silently mutate state. All decisions must emit rationale + evidence pointers.
