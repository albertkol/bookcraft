from bookcraft.cell.rules.BreakLineRule import BreakLineRule
from bookcraft.cell.rules.CharRule import CharRule
from bookcraft.cell.rules.HeaderSpacingRule import HeaderSpacingRule
from bookcraft.cell.rules.Rule import CellSpecificationRule
from bookcraft.cursor.rules.BlankSpaceRule import BlankSpaceRule
from bookcraft.cursor.rules.ContentsItemRule import ContentsItemRulenRule
from bookcraft.cursor.rules.DarkenRoleRule import DarkenRoleRule
from bookcraft.cursor.rules.DefaultRule import DefaultRule
from bookcraft.cursor.rules.HeaderRule import HeaderRule
from bookcraft.cursor.rules.HyphenRule import HyphenRule
from bookcraft.cursor.rules.ItalicRule import ItalicRule
from bookcraft.cursor.rules.KeywordRule import KeywordRule
from bookcraft.cursor.rules.ParenthesisRule import ParenthesisRule
from bookcraft.cursor.rules.RoleRule import RoleRule
from bookcraft.cursor.rules.Rule import CursorSpecificationRule
from bookcraft.models import Cursor, ItalicType, RuleType
from bookcraft.specs.FirstLineSpecification import FirstLineSpecification
from bookcraft.specs.IsCharEqualSpecification import IsCharEqualSpecification


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


def test_blank_space_rule_counts_consecutive_spaces(make_context):
    ctx = make_context(["abc   end"], i=0, j=3)
    result = BlankSpaceRule().apply(ctx)
    assert result.rule == RuleType.BLANK_SPACE
    assert result.counter > 1


def test_role_rule_sets_light_fill(make_context):
    ctx = make_context(["$W. M. hello"], i=0, j=0)
    result = RoleRule().apply(ctx)
    assert result.rule == RuleType.ROLE_HIGHLIGHT
    assert result.cursor.fill == [200, 200, 200]


def test_darken_role_rule_sets_dark_fill(make_context):
    ctx = make_context(["$W. M. hello"], i=0, j=0)
    result = DarkenRoleRule().apply(ctx)
    assert result.rule == RuleType.ROLE_HIGHLIGHT
    assert result.cursor.fill == [255, 255, 255]


def test_parenthesis_rule(make_context):
    ctx = make_context(["(hello)"], i=0, j=0)
    result = ParenthesisRule().apply(ctx)
    assert result.rule == RuleType.PARENTHESES
    assert result.counter == 2


def test_italic_rule_start(make_context):
    ctx = make_context(["hello"])
    result = ItalicRule(ItalicType.START).apply(ctx)
    assert result.rule == RuleType.ITALIC_START


def test_italic_rule_end(make_context):
    ctx = make_context(["hello"])
    result = ItalicRule(ItalicType.END).apply(ctx)
    assert result.rule == RuleType.ITALIC_END


def test_hyphen_rule(make_context):
    ctx = make_context(["-"])
    result = HyphenRule().apply(ctx)
    assert result.rule == RuleType.PARENTHESES
    assert result.counter == 2


def test_contents_item_rule(make_context):
    ctx = make_context(["& item"])
    result = ContentsItemRulenRule().apply(ctx)
    assert result.rule == RuleType.CONTENTS_ITEM


def test_keyword_rule_returns_none_when_no_match(make_context):
    ctx = make_context(["hello world"], i=0, j=0)
    result = KeywordRule().apply(ctx)
    assert result is None


def test_cursor_specification_rule_returns_none_when_not_satisfied(make_context):
    ctx = make_context(["hello"], i=0, j=1)
    rule = CursorSpecificationRule(IsCharEqualSpecification(["#"]), HeaderRule())
    assert rule.apply(ctx) is None


def test_cell_specification_rule_returns_none_when_not_satisfied(make_context):
    ctx = make_context(["hello"], i=1)
    rule = CellSpecificationRule(FirstLineSpecification(), CharRule())
    assert rule.apply(ctx) is None
