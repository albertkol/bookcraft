from classes.cursor.rules.Rule import CursorRule
from classes.models import (
    Context,
    Cursor,
    CursorModifier,
    ItalicType,
    RuleType,
)


class ItalicRule(CursorRule):
    def __init__(self, type) -> None:
        self.type = type

    def apply(self, context: Context) -> CursorModifier:
        CONFIG = context.config
        return CursorModifier(
            rule=(
                RuleType.ITALIC_START
                if self.type == ItalicType.START
                else RuleType.ITALIC_END
            ),
            cursor=Cursor(**CONFIG.ITALIC_CURSOR),
            counter=-1,
        )
