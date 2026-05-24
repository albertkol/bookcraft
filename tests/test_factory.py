from bookcraft.cell.CellFactory import CellFactory
from bookcraft.cursor.CursorModifierFactory import CursorModifierFactory
from bookcraft.models import Cursor, RuleType


def test_cursor_modifier_factory_resolves_title_for_header_char(make_context):
    ctx = make_context(["#heading"], i=0, j=0)
    modifiers = CursorModifierFactory().resolve(ctx)
    rules = [m.rule for m in modifiers]
    assert RuleType.TITLE in rules


def test_cursor_modifier_factory_resolves_role_highlight_for_dollar(make_context):
    ctx = make_context(["$W. M. hello"], i=0, j=0)
    modifiers = CursorModifierFactory().resolve(ctx)
    rules = [m.rule for m in modifiers]
    assert RuleType.ROLE_HIGHLIGHT in rules


def test_cell_factory_creates_cells_for_regular_char(make_context):
    ctx = make_context(
        ["hello"],
        i=0,
        j=1,
        cursor=Cursor(
            family="Arial", size=12, style="", colour=[0, 0, 0], fill=[255, 255, 255]
        ),
    )
    cells = CellFactory().create_cells(ctx)
    assert any(c.text == "e" for c in cells)


def test_cell_factory_produces_break_at_end_of_line(make_context):
    ctx = make_context(
        ["hi"],
        i=0,
        j=1,
        cursor=Cursor(
            family="Arial", size=12, style="", colour=[0, 0, 0], fill=[255, 255, 255]
        ),
    )
    cells = CellFactory().create_cells(ctx)
    assert any(c.has_break for c in cells)
