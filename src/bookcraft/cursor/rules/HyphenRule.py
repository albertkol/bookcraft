from bookcraft.cursor.rules.Rule import CursorRule
from bookcraft.models import Context, Cursor, CursorModifier, RuleType


class HyphenRule(CursorRule):
    def apply(self, context: Context) -> CursorModifier:
        return CursorModifier(
            rule=RuleType.PARENTHESES,
            cursor=Cursor(size=13),
            counter=2,
        )
