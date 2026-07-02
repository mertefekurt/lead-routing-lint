# lead-routing-lint

> Audit lead routing rules for owner gaps, region mismatch, and fallback behavior.

## CI gate Overview

Audit lead routing rules for owner gaps, region mismatch, and fallback behavior. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts lead routing rule. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
lead-routing-lint examples/sample.txt
lead-routing-lint examples/sample.txt --json --fail-on medium
python -m lead_routing_lint --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-owner` | high | lead owner missing |
| `missing-fallback` | medium | fallback route missing |
| `territory-mismatch` | low | territory mismatch detected |

## Validation Notes

```bash
ruff check .
pytest
python -m lead_routing_lint --help
```

Example risky input:

```text
region EMEA owner none fallback missing territory mismatch
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
