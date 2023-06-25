from classes.cursor.rules.Rule import CursorRule
from classes.models import Context, Cursor, CursorModifier, RuleType


class DefaultRule(CursorRule):
    def apply(self, context: Context) -> CursorModifier:
        return CursorModifier(
            rule=RuleType.DEFAULT,
            cursor=Cursor(**context.config.DEFAULT_CURSOR),
            counter=-1,
        )
