from dataclasses import dataclass

from classes.cursor.rules.BlankSpaceRule import BlankSpaceRule
from classes.cursor.rules.DarkenRoleRule import DarkenRoleRule
from classes.cursor.rules.DefaultRule import DefaultRule
from classes.cursor.rules.HeaderRule import HeaderRule
from classes.cursor.rules.HyphenRule import HyphenRule
from classes.cursor.rules.ItalicRule import ItalicRule
from classes.cursor.rules.KeywordRule import KeywordRule
from classes.cursor.rules.ParenthesisRule import ParenthesisRule
from classes.cursor.rules.RoleRule import RoleRule
from classes.cursor.rules.Rule import CursorRule, CursorSpecificationRule
from classes.models import Context, CursorModifier, ItalicType
from classes.specs.AfterRoleSpecification import AfterRoleSpecification
from classes.specs.IsCharEqualSpecification import IsCharEqualSpecification
from classes.specs.IsItalicSpecification import isItalicSpecification
from classes.specs.LineHasCharSpecification import LineHasCharSpecification
from classes.specs.NextCharEquals import NextCharEquals
from classes.specs.PreviousCharEquals import PreviousCharEquals
from classes.specs.Specification import AndSpecification, NotSpecification


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
            ItalicRule(ItalicType.START),
        ),
        CursorSpecificationRule(
            AndSpecification(
                isItalicSpecification(),
                NextCharEquals([")", "<"]),
            ),
            ItalicRule(ItalicType.END),
        ),
        CursorSpecificationRule(
            PreviousCharEquals([")", "<"]),
            BlankSpaceRule(),
        ),
        CursorSpecificationRule(
            NotSpecification(LineHasCharSpecification(["#"], 0)),
            KeywordRule(),
        ),
        CursorSpecificationRule(
            IsCharEqualSpecification(["-"]),
            HyphenRule(),
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
