# StratForge

Base scaffold for a Python library project using a `src` layout.

## Structure

```text
.
├── pyproject.toml
├── README.md
├── src/
│   └── strat_forge/
│       └── __init__.py
└── tests/
    └── test_package.py
```

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```
