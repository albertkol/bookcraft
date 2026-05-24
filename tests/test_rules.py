from bookcraft.cell.rules.BreakLineRule import BreakLineRule
from bookcraft.cell.rules.CharRule import CharRule
from bookcraft.cell.rules.HeaderSpacingRule import HeaderSpacingRule
from bookcraft.cursor.rules.DefaultRule import DefaultRule
from bookcraft.cursor.rules.HeaderRule import HeaderRule
from bookcraft.cursor.rules.KeywordRule import KeywordRule
from bookcraft.models import Cursor, RuleType


def test_default_rule_returns_default_modifier(make_context):
    ctx = make_context(
        ["hello"],
        cursor=Cursor(
            family="Arial", size=12, style="", colour=[0, 0, 0], fill=[255, 255, 255]
        ),
    )
    result = DefaultRule().apply(ctx)
    assert result.rule == RuleType.DEFAULT
    assert result.counter == -1


def test_header_rule_returns_title_modifier(make_context):
    ctx = make_context(["= Title ="])
    result = HeaderRule().apply(ctx)
    assert result.rule == RuleType.TITLE
    assert result.counter == -1


def test_keyword_rule_matches_keyword(make_context):
    ctx = make_context(["W. M. speaks"], i=0, j=0)
    result = KeywordRule().apply(ctx)
    assert result is not None
    assert result.rule == RuleType.KEYWORD


def test_char_rule_returns_current_char(make_context):
    ctx = make_context(
        ["hello"],
        i=0,
        j=1,
        cursor=Cursor(
            family="Arial", size=12, style="", colour=[0, 0, 0], fill=[255, 255, 255]
        ),
    )
    result = CharRule().apply(ctx)
    assert result.text == "e"
    assert result.height == 20


def test_break_line_rule(make_context):
    ctx = make_context(
        ["hello"],
        cursor=Cursor(
            family="Arial", size=12, style="", colour=[0, 0, 0], fill=[255, 255, 255]
        ),
    )
    result = BreakLineRule().apply(ctx)
    assert result.has_break is True
    assert result.text == ""


def test_header_spacing_rule(make_context):
    ctx = make_context(
        ["hello"],
        cursor=Cursor(
            family="Arial", size=12, style="", colour=[0, 0, 0], fill=[255, 255, 255]
        ),
    )
    result = HeaderSpacingRule().apply(ctx)
    assert result.has_break is True
    assert result.height == 3
