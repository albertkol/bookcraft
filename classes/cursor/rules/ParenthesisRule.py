from classes.cursor.rules.Rule import CursorRule
from classes.models import Context, Cursor, CursorModifier, RuleType


class ParenthesisRule(CursorRule):
    def apply(self, context: Context) -> CursorModifier:
        CONFIG = context.config
        return CursorModifier(
            rule=RuleType.PARENTHESES,
            cursor=Cursor(
                family=CONFIG.BOLD_CURSOR["family"],
                size=CONFIG.BOLD_CURSOR["size"],
                style=CONFIG.BOLD_CURSOR["style"],
                colour=[0, 0, 0],
                fill=[255, 255, 255],
            ),
            counter=2,
        )
