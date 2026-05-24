from bookcraft.cursor.rules.Rule import CursorRule
from bookcraft.models import Context, Cursor, CursorModifier, RuleType


class HeaderRule(CursorRule):
    def apply(self, context: Context) -> CursorModifier:
        config = context.config
        return CursorModifier(
            rule=RuleType.TITLE,
            cursor=Cursor(**config.heading_cursor),
            counter=-1,
        )
