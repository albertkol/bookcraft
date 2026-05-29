# Changelog

## 1.2.0 — 2026-05-29

### Changes

- Craft page width reduced from 475 pt to 455 pt

## 1.1.0 — 2026-05-25

### Features

- `page.page_no_offset` config field: set the integer offset added to the displayed page number in headers. Replaces the hardcoded `+22` (RA) / `−5` (Craft) values that were baked into the library.

## 1.0.0 — 2026-05-25

### Features

- `~text~` underline rule: wrapping text in `~…~` renders it underlined, using the font and size already active at that position
- Underline is continuous through justified spaces — space cells in an underlined span are underlined manually to close the gaps fpdf2 leaves
- `CursorConfig.size` is now optional (null inherits the current font size); the underline cursor defaults to null for all config fields except `style: "U"`

### Changes

- Bold keywords now suppress italic style but not underline: a keyword inside `(…)` renders bold-only; a keyword inside `~…~` renders bold and underlined
- `CursorModifierReducer` now derives `cursor.style` from logical states (`is_bold`, `is_italic`, `is_underline`) rather than chaining modifier `style` fields — prevents B and U from silently overwriting each other
- `CursorModifierProcessor` correctly handles simultaneous END markers (e.g. italic and underline closing on the same character)
- `ItalicType` and `UnderlineType` merged into a single `MarkerType` enum
- `isBoldSpecification` / `isItalicSpecification` renamed to `IsBoldSpecification` / `IsItalicSpecification`
- `type` parameter in `ItalicRule` / `UnderlineRule` renamed to `marker` to avoid shadowing the built-in
- Processor DEFAULT/TITLE reset and `_handle_end` reverse-scan simplified

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
