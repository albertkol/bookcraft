from bookcraft.cursor.CursorModifierProcessor import CursorModifierProcessor
from bookcraft.models import Cursor, CursorModifier, RuleType

processor = CursorModifierProcessor()


def mod(rule, counter=2):
    return CursorModifier(rule=rule, cursor=Cursor(), counter=counter)


def test_empty_returns_empty():
    assert processor.process([]) == []


def test_default_resets_to_single():
    result = processor.process([mod(RuleType.ROLE), mod(RuleType.DEFAULT)])
    assert len(result) == 1
    assert result[0].rule == RuleType.DEFAULT


def test_title_resets_to_single():
    result = processor.process([mod(RuleType.ROLE), mod(RuleType.TITLE)])
    assert len(result) == 1
    assert result[0].rule == RuleType.TITLE


def test_counter_decrements():
    result = processor.process([mod(RuleType.ROLE, counter=3)])
    assert result[0].counter == 2


def test_expired_modifier_removed():
    result = processor.process([mod(RuleType.ROLE, counter=1)])
    assert result == []


def test_infinite_counter_not_removed():
    result = processor.process([mod(RuleType.DEFAULT, counter=-1)])
    assert len(result) == 1


def test_italic_end_removes_italic_end_modifier():
    modifiers = [
        mod(RuleType.ITALIC_START, counter=-1),
        mod(RuleType.ITALIC_END, counter=1),
    ]
    result = processor.process(modifiers)
    assert not any(m.rule == RuleType.ITALIC_END for m in result)
