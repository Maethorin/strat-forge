# StratForge

[![Build Status](https://img.shields.io/github/actions/workflow/status/Maethorin/strat-forge/ci.yml?branch=master&label=build)](https://github.com/Maethorin/strat-forge/actions/workflows/ci.yml) [![Coverage](https://img.shields.io/codecov/c/github/Maethorin/strat-forge?label=coverage)](https://codecov.io/gh/Maethorin/strat-forge) [![License](https://img.shields.io/badge/license-Non--Commercial-lightgrey)](./LICENSE.md) [![Python](https://img.shields.io/badge/python-3.14%2B-blue)](./pyproject.toml)

Base scaffold for a Python library project using a `src` layout.

## Structure

```text
.
├── LICENSE.md
├── LICENSE-COMMERCIAL.md
├── pyproject.toml
├── README.md
├── src/
│   └── strat_forge/
│       └── __init__.py
└── tests/
    └── unit/
        ├── strat_forge/
        │   └── test___init__.py
        ├── test_github_actions.py
        ├── test_pyproject.py
        ├── test_readme.py
        └── test_setup.py
```

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## License

StratForge is available under a non-commercial license:

- Free for non-commercial use. see LICENSE.md.
- Commercial use requires a separate commercial license (see LICENSE-COMMERCIAL.md).

For commercial licensing, contact:
ti@mae42.com.br
