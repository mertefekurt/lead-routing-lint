<p align="center">
  <img src="assets/readme-cover.svg" alt="Lead Routing Lint cover" width="100%" />
</p>

# Lead Routing Lint

![stack](https://img.shields.io/badge/stack-Python-2563eb?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-16a34a?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-dc2626?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-7c3aed?style=flat-square)

Audit lead routing rules for owner gaps, region mismatch, and fallback behavior.

## Why it exists

Small review tasks are easy to skip when the signal lives in notes, spreadsheets, or loosely formatted exports. `lead-routing-lint` turns those checks into a repeatable command with plain findings and CI-friendly exit codes.

## Quick run

```bash
python -m pip install -e ".[dev]"
lead-routing-lint examples/sample.txt
lead-routing-lint examples/sample.txt --json --fail-on medium
```

## Rule set

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-owner` | high | lead owner missing |
| `missing-fallback` | medium | fallback route missing |
| `territory-mismatch` | low | territory mismatch detected |

## Input

The reader accepts plain text, JSON, JSONL, and CSV. That keeps it useful for hand-written notes, review exports, and small automation jobs.

## Sample risky input

```text
region EMEA owner none fallback missing territory mismatch
```

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m lead_routing_lint --help
```

`cli.py` handles arguments, `core.py` reads and evaluates records, and `rules.py` keeps the Lead Routing Lint policy easy to review.
