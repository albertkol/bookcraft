from bookcraft.cursor.rules.Rule import CursorRule
from bookcraft.models import Context, Cursor, CursorModifier, RuleType


class ParenthesisRule(CursorRule):
    def apply(self, context: Context) -> CursorModifier:
        config = context.config
        return CursorModifier(
            rule=RuleType.PARENTHESES,
            cursor=Cursor(
                family=config.default_cursor["family"],
                size=config.default_cursor["size"],
                style=config.default_cursor["style"],
                fill=None if config.is_dark else [255, 255, 255],
            ),
            counter=2,
        )
