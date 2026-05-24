from bookcraft.models import Cursor
from bookcraft.specs.AfterRoleSpecification import AfterRoleSpecification
from bookcraft.specs.FirstLineSpecification import FirstLineSpecification
from bookcraft.specs.IsCharEqualSpecification import IsCharEqualSpecification
from bookcraft.specs.IsEndOfLineSpecification import IsEndOfLineSpecification
from bookcraft.specs.IsBoldSpecification import isBoldSpecification
from bookcraft.specs.IsItalicSpecification import isItalicSpecification
from bookcraft.specs.LineHasCharSpecification import LineHasCharSpecification


def test_first_line_true(make_context):
    ctx = make_context(["hello", "world"], i=0)
    assert FirstLineSpecification().is_satisfied(ctx) is True


def test_first_line_false(make_context):
    ctx = make_context(["hello", "world"], i=1)
    assert FirstLineSpecification().is_satisfied(ctx) is False


def test_end_of_line_true(make_context):
    ctx = make_context(["hello"], i=0, j=4)
    assert IsEndOfLineSpecification().is_satisfied(ctx) is True


def test_end_of_line_false(make_context):
    ctx = make_context(["hello"], i=0, j=2)
    assert IsEndOfLineSpecification().is_satisfied(ctx) is False


def test_char_equal_true(make_context):
    ctx = make_context(["#heading"], i=0, j=0)
    assert IsCharEqualSpecification(["#"]).is_satisfied(ctx) is True


def test_char_equal_false(make_context):
    ctx = make_context(["hello"], i=0, j=0)
    assert IsCharEqualSpecification(["#"]).is_satisfied(ctx) is False


def test_line_has_char_true(make_context):
    ctx = make_context(["= title ="], i=0)
    assert LineHasCharSpecification(["="]).is_satisfied(ctx) is True


def test_line_has_char_false(make_context):
    ctx = make_context(["hello world"], i=0)
    assert LineHasCharSpecification(["="]).is_satisfied(ctx) is False


def test_is_bold_true(make_context):
    ctx = make_context(["hello"], cursor=Cursor(is_bold=True))
    assert isBoldSpecification().is_satisfied(ctx) is True


def test_is_bold_false(make_context):
    ctx = make_context(["hello"], cursor=Cursor(is_bold=False))
    assert isBoldSpecification().is_satisfied(ctx) is False


def test_is_italic_true(make_context):
    ctx = make_context(["hello"], cursor=Cursor(is_italic=True))
    assert isItalicSpecification().is_satisfied(ctx) is True


def test_after_role_true(make_context):
    ctx = make_context(["$W. M. hello"], i=0, j=6)
    assert AfterRoleSpecification().is_satisfied(ctx)


def test_after_role_false(make_context):
    ctx = make_context(["hello world"], i=0, j=5)
    assert not AfterRoleSpecification().is_satisfied(ctx)
