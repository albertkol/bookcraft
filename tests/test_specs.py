from bookcraft.models import Cursor
from bookcraft.specs.AfterRoleSpecification import AfterRoleSpecification
from bookcraft.specs.FirstLineSpecification import FirstLineSpecification
from bookcraft.specs.IsCharEqualSpecification import IsCharEqualSpecification
from bookcraft.specs.IsEndOfLineSpecification import IsEndOfLineSpecification
from bookcraft.specs.IsBoldSpecification import IsBoldSpecification
from bookcraft.specs.IsItalicSpecification import IsItalicSpecification
from bookcraft.specs.LineHasCharSpecification import LineHasCharSpecification
from bookcraft.specs.NextCharEquals import NextCharEquals
from bookcraft.specs.PreviousCharEquals import PreviousCharEquals
from bookcraft.specs.Specification import (
    AndSpecification,
    NotSpecification,
    OrSpecification,
)


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
    assert IsBoldSpecification().is_satisfied(ctx) is True


def test_is_bold_false(make_context):
    ctx = make_context(["hello"], cursor=Cursor(is_bold=False))
    assert IsBoldSpecification().is_satisfied(ctx) is False


def test_is_italic_true(make_context):
    ctx = make_context(["hello"], cursor=Cursor(is_italic=True))
    assert IsItalicSpecification().is_satisfied(ctx) is True


def test_after_role_true(make_context):
    ctx = make_context(["$W. M. hello"], i=0, j=6)
    assert AfterRoleSpecification().is_satisfied(ctx)


def test_after_role_false(make_context):
    ctx = make_context(["hello world"], i=0, j=5)
    assert not AfterRoleSpecification().is_satisfied(ctx)


def test_and_specification_three_specs_all_true(make_context):
    ctx = make_context(["hello"], i=0, j=0)
    spec = AndSpecification(
        IsCharEqualSpecification(["h"]),
        FirstLineSpecification(),
        NotSpecification(IsCharEqualSpecification(["x"])),
    )
    assert spec.is_satisfied(ctx) is True


def test_and_specification_three_specs_one_false(make_context):
    ctx = make_context(["hello"], i=0, j=0)
    spec = AndSpecification(
        IsCharEqualSpecification(["h"]),
        FirstLineSpecification(),
        IsCharEqualSpecification(["x"]),
    )
    assert spec.is_satisfied(ctx) is False


def test_or_specification_true_when_one_matches(make_context):
    ctx = make_context(["hello"], i=0, j=0)
    spec = OrSpecification(
        IsCharEqualSpecification(["h"]), IsCharEqualSpecification(["x"])
    )
    assert spec.is_satisfied(ctx) is True


def test_or_specification_false_when_none_match(make_context):
    ctx = make_context(["hello"], i=0, j=0)
    spec = OrSpecification(
        IsCharEqualSpecification(["x"]), IsCharEqualSpecification(["y"])
    )
    assert spec.is_satisfied(ctx) is False


def test_not_specification_negates(make_context):
    ctx = make_context(["hello"], i=0, j=0)
    assert NotSpecification(IsCharEqualSpecification(["x"])).is_satisfied(ctx) is True


def test_line_has_char_with_offset_out_of_bounds(make_context):
    ctx = make_context(["hello"], i=0)
    assert LineHasCharSpecification(["="], 1).is_satisfied(ctx) is False


def test_previous_char_equals_true(make_context):
    ctx = make_context(["(hello"], i=0, j=1)
    assert PreviousCharEquals(["("]).is_satisfied(ctx) is True


def test_previous_char_equals_false(make_context):
    ctx = make_context(["hello"], i=0, j=1)
    assert PreviousCharEquals(["("]).is_satisfied(ctx) is False


def test_next_char_equals_true(make_context):
    ctx = make_context(["hello("], i=0, j=4)
    assert NextCharEquals(["("]).is_satisfied(ctx) is True


def test_next_char_equals_false(make_context):
    ctx = make_context(["hello"], i=0, j=4)
    assert NextCharEquals(["("]).is_satisfied(ctx) is False
