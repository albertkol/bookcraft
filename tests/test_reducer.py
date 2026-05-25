from bookcraft.cursor.CursorModifierReducer import CursorModifierReducer
from bookcraft.models import Cursor, CursorModifier, RuleType

reducer = CursorModifierReducer()


def mod(rule, **kwargs):
    return CursorModifier(rule=rule, cursor=Cursor(**kwargs), counter=1)


def test_empty_returns_empty_cursor():
    cursor = reducer.reduce([])
    assert cursor.family is None
    assert cursor.size is None


def test_last_modifier_wins():
    result = reducer.reduce(
        [
            mod(RuleType.DEFAULT, family="Arial", size=12),
            mod(RuleType.DEFAULT, family="Helvetica", size=14),
        ]
    )
    assert result.family == "Helvetica"
    assert result.size == 14


def test_keyword_sets_bold():
    result = reducer.reduce([mod(RuleType.KEYWORD, family="Arial")])
    assert result.is_bold is True


def test_italic_start_sets_italic():
    result = reducer.reduce([mod(RuleType.ITALIC_START, family="Arial")])
    assert result.is_italic is True


def test_no_keyword_not_bold():
    result = reducer.reduce([mod(RuleType.DEFAULT, family="Arial")])
    assert result.is_bold is False


def test_underline_start_sets_underline():
    result = reducer.reduce([mod(RuleType.UNDERLINE_START)])
    assert result.is_underline is True
    assert result.style == "U"


def test_bold_suppresses_italic_style():
    result = reducer.reduce(
        [mod(RuleType.ITALIC_START), mod(RuleType.KEYWORD, family="Arial")]
    )
    assert result.is_bold is True
    assert result.style == "B"


def test_bold_with_underline_gives_bu_style():
    result = reducer.reduce(
        [mod(RuleType.UNDERLINE_START), mod(RuleType.KEYWORD, family="Arial")]
    )
    assert result.is_bold is True
    assert result.is_underline is True
    assert result.style == "BU"


def test_bold_anywhere_in_list_detected():
    result = reducer.reduce(
        [mod(RuleType.KEYWORD, family="Arial"), mod(RuleType.UNDERLINE_START)]
    )
    assert result.is_bold is True
