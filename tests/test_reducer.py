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
    result = reducer.reduce([
        mod(RuleType.DEFAULT, family="Arial", size=12),
        mod(RuleType.DEFAULT, family="Helvetica", size=14),
    ])
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
