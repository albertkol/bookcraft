# Changelog

## 0.2.1 — 2026-05-24

- Expanded test suite: added tests for CLI, config, factory, helpers, specs, and integration
- Added ruff, ty, and pre-commit to dev toolchain
- Added codecov configuration and coverage reporting
- Minor code fixes from static analysis (ruff, ty)

## 0.2.0 — 2026-05-24

- Refactored into `src/` layout for proper PyPI packaging
- Pydantic-validated configuration (settings, fonts, keywords)
- All config properties lowercased
- `generate()` accepts explicit paths and mode instead of reading `sys.argv`
- `Book` accepts `Config` as constructor parameter
- Added `bookcraft` CLI entrypoint
- Added pytest test suite with coverage reporting
- Switched from Poetry to uv
- GitHub Actions for CI and automated PyPI publishing

## 0.1.0 — 2026-05-24

Initial release.

- `generate()` public API for building PDFs from structured text
- Four rendering modes: `craft`, `craft-dark`, `ra`, `ra-dark`
- Pydantic-validated configuration (settings, fonts, keywords)
- CLI entrypoint: `bookcraft`
