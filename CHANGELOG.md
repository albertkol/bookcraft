# Changelog

## 0.3.1 — 2026-05-25

### Fixes

- Header dashed line is now suppressed for any chapter whose title contains `"Cover"` or `"End"`, replacing the fragile `page_no > 0 and page_no < 150` range check
- Cover page suppression now applies to all book types, not just Royal Arch

## 0.3.0 — 2026-05-24

### Breaking changes

- `Settings.books` now expects a list of `ChapterEntry` objects (`path`, `title`) instead of plain strings — update your YAML config accordingly
- `Book.set_margin()` renamed to `configure_margins()`

### Changes

- Font paths in `fonts.yaml` are now resolved relative to the YAML file's location, making font loading work correctly regardless of working directory
- Updated fpdf2 API: `cell()` now uses `XPos`/`YPos` enums; removed deprecated `ln` parameter and `uni=True` from `add_font()`
- `CellRule.apply()` and `CursorRule.apply()` return types now include `None`
- Removed `FontStyle` enum — font styles are now plain strings
- Fixed `None` guards in `_print_line` and `_justify_line`
- Fixed `default_fill` and `template_color` returning `None` instead of `[]`
- Improved type annotations throughout (`previous_chars_matches`, `next_chars_matches`, `RGBColour`, `Page`)
- Expanded test suite: CLI, config, factory, helpers, specs, and integration tests
- Added ruff, ty, and pre-commit to dev toolchain
- Added Codecov configuration

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
