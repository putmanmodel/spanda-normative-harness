import argparse
import hashlib
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

from jsonschema import Draft202012Validator


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_demo_module(demo_py: Path):
    spec = importlib.util.spec_from_file_location("demo_module", demo_py)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load demo module: {demo_py}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore
    if not hasattr(module, "run"):
        raise RuntimeError(f"{demo_py} must export run(fixture: dict) -> dict")
    return module


def validate_event(event: dict, schema: dict):
    v = Draft202012Validator(schema)
    errors = sorted(v.iter_errors(event), key=lambda e: e.path)
    if errors:
        msg_lines = ["Schema validation failed:"]
        for e in errors:
            loc = " -> ".join([str(p) for p in e.path]) if e.path else "(root)"
            msg_lines.append(f"- {loc}: {e.message}")
        raise ValueError("\n".join(msg_lines))


def main():
    import sys
    sys.argv = [a.replace('–','-').replace('—','-') for a in sys.argv]

    ap = argparse.ArgumentParser(description="Run a single deterministic Spanda normative demo.")
    ap.add_argument("--demo", required=True, help="Demo folder name, e.g. demo01_constraint_boundary")
    ap.add_argument("--mode", required=True, choices=["proof", "break"], help="Which fixture to run")
    ap.add_argument("--out", default="logs", help="Output logs folder (default: logs)")
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    demo_dir = repo_root / "demos" / args.demo
    if not demo_dir.exists():
        raise FileNotFoundError(f"Demo folder not found: {demo_dir}")

    fixture_path = demo_dir / f"{args.mode}.json"
    demo_py = demo_dir / "demo.py"
    schema_path = repo_root / "harness" / "schema.json"

    if not fixture_path.exists():
        raise FileNotFoundError(f"Missing fixture: {fixture_path}")
    if not demo_py.exists():
        raise FileNotFoundError(f"Missing demo entrypoint: {demo_py}")
    if not schema_path.exists():
        raise FileNotFoundError(f"Missing schema: {schema_path}")

    fixture = load_json(fixture_path)
    fixture_hash = sha256_file(fixture_path)
    schema = load_json(schema_path)

    module = load_demo_module(demo_py)

    result = module.run(fixture)

    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    event = {
        "demo_id": args.demo,
        "normative_ids": result.get("normative_ids", []),
        "mode": args.mode,
        "fixture_path": str(fixture_path.relative_to(repo_root)).replace("\\", "/"),
        "fixture_hash": fixture_hash,
        "pass": bool(result.get("pass")),
        "decision": str(result.get("decision", "")),
        "rationale": str(result.get("rationale", "")),
        "evidence": list(result.get("evidence", [])),
        "timestamp_utc": now,
    }

    validate_event(event, schema)

    out_dir = repo_root / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    out_file = out_dir / f"{args.demo}_{args.mode}.jsonl"
    out_line = json.dumps(event, ensure_ascii=False, sort_keys=True)
    out_file.write_text(out_line + "\n", encoding="utf-8")

    print(f"[OK] Wrote {out_file}")
    print(out_line)


if __name__ == "__main__":
    main()
