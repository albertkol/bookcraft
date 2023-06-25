from classes.cursor.rules.Rule import CursorRule
from classes.models import Context, Cursor, CursorModifier, RuleType


class HeaderRule(CursorRule):
    def apply(self, context: Context) -> CursorModifier:
        CONFIG = context.config
        return CursorModifier(
            rule=RuleType.TITLE,
            cursor=Cursor(**CONFIG.HEADING_CURSOR),
            counter=-1,
        )
