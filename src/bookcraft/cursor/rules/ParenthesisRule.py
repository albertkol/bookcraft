from bookcraft.cursor.rules.Rule import CursorRule
from bookcraft.models import Context, Cursor, CursorModifier, RuleType


class ParenthesisRule(CursorRule):
    def apply(self, context: Context) -> CursorModifier:
        config = context.config
        return CursorModifier(
            rule=RuleType.PARENTHESES,
            cursor=Cursor(
                family=config.DEFAULT_CURSOR["family"],
                size=config.DEFAULT_CURSOR["size"],
                style=config.DEFAULT_CURSOR["style"],
                fill=None if config.is_dark else [255, 255, 255],
            ),
            counter=2,
        )
