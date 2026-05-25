from dataclasses import dataclass

from bookcraft.cursor.rules.BlankSpaceRule import BlankSpaceRule
from bookcraft.cursor.rules.ContentsItemRule import ContentsItemRulenRule
from bookcraft.cursor.rules.DarkenRoleRule import DarkenRoleRule
from bookcraft.cursor.rules.DefaultRule import DefaultRule
from bookcraft.cursor.rules.HeaderRule import HeaderRule
from bookcraft.cursor.rules.HyphenRule import HyphenRule
from bookcraft.cursor.rules.ItalicRule import ItalicRule
from bookcraft.cursor.rules.KeywordRule import KeywordRule
from bookcraft.cursor.rules.UnderlineRule import UnderlineRule
from bookcraft.cursor.rules.ParenthesisRule import ParenthesisRule
from bookcraft.cursor.rules.RoleRule import RoleRule
from bookcraft.cursor.rules.Rule import CursorRule, CursorSpecificationRule
from bookcraft.models import Context, CursorModifier, MarkerType
from bookcraft.specs.AfterRoleSpecification import AfterRoleSpecification
from bookcraft.specs.IsCharEqualSpecification import IsCharEqualSpecification
from bookcraft.specs.IsItalicSpecification import IsItalicSpecification
from bookcraft.specs.IsUnderlineSpecification import IsUnderlineSpecification
from bookcraft.specs.LineHasCharSpecification import LineHasCharSpecification
from bookcraft.specs.NextCharEquals import NextCharEquals
from bookcraft.specs.PreviousCharEquals import PreviousCharEquals
from bookcraft.specs.Specification import AndSpecification, NotSpecification


@dataclass
class CursorModifierFactory:
    rules: tuple[CursorRule, ...] = (
        CursorSpecificationRule(
            IsCharEqualSpecification(["#"]),
            HeaderRule(),
        ),
        CursorSpecificationRule(
            IsCharEqualSpecification(["$"]),
            DefaultRule(),
        ),
        CursorSpecificationRule(
            IsCharEqualSpecification(["$"]),
            RoleRule(),
        ),
        CursorSpecificationRule(
            IsCharEqualSpecification(["$"]),
            DarkenRoleRule(),
        ),
        CursorSpecificationRule(
            AfterRoleSpecification(),
            BlankSpaceRule(),
        ),
        CursorSpecificationRule(
            IsCharEqualSpecification(["(", ")"]),
            ParenthesisRule(),
        ),
        CursorSpecificationRule(
            AndSpecification(
                IsCharEqualSpecification([" "]),
                NextCharEquals(["(", ">"]),
            ),
            BlankSpaceRule(),
        ),
        CursorSpecificationRule(
            PreviousCharEquals(["(", ">"]),
            ItalicRule(MarkerType.START),
        ),
        CursorSpecificationRule(
            AndSpecification(
                IsItalicSpecification(),
                NextCharEquals([")", "<"]),
            ),
            ItalicRule(MarkerType.END),
        ),
        CursorSpecificationRule(
            PreviousCharEquals([")", "<"]),
            BlankSpaceRule(),
        ),
        CursorSpecificationRule(
            AndSpecification(
                IsCharEqualSpecification(["~"]),
                NotSpecification(IsUnderlineSpecification()),
            ),
            UnderlineRule(MarkerType.START),
        ),
        CursorSpecificationRule(
            AndSpecification(
                IsCharEqualSpecification(["~"]),
                IsUnderlineSpecification(),
            ),
            UnderlineRule(MarkerType.END),
        ),
        CursorSpecificationRule(
            NotSpecification(LineHasCharSpecification(["#", "&"], 0)),
            KeywordRule(),
        ),
        CursorSpecificationRule(
            IsCharEqualSpecification(["-"]),
            HyphenRule(),
        ),
        CursorSpecificationRule(
            LineHasCharSpecification(["&"], 0),
            ContentsItemRulenRule(),
        ),
        CursorSpecificationRule(
            IsCharEqualSpecification(["%"]),
            DefaultRule(),
        ),
    )

    def resolve(self, context: Context) -> list[CursorModifier]:
        modifiers = []

        for rule in self.rules:
            modifier = rule.apply(context)
            if modifier:
                modifiers.append(modifier)

        return modifiers
