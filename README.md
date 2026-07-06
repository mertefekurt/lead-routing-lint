# Lead Routing Lint

![Lead Routing Lint cover](assets/readme-cover.svg)

Audit lead routing rules for owner gaps, region mismatch, and fallback behavior. The idea is simple: give Lead Routing Lint the local file or fixture, get a readable result, and decide what needs attention before the next handoff.

## Lead Routing Lint catches

- `missing-owner` (high): lead owner missing. Fix: assign route owner.
- `missing-fallback` (medium): fallback route missing. Fix: add fallback queue.
- `territory-mismatch` (low): territory mismatch detected. Fix: verify territory mapping.

## A normal pass

```bash
git clone https://github.com/mertefekurt/lead-routing-lint.git
cd lead-routing-lint
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
lead-routing-lint examples/sample.txt
lead-routing-lint examples/sample.txt --json
```

The input can be text, JSON, JSONL, or CSV. Use `--json` when another script needs the result instead of a Markdown report.

## A deliberately bad line

```text
region EMEA owner none fallback missing territory mismatch
```

## Maintainer loop

```bash
ruff check .
pytest
python -m lead_routing_lint --help
```
