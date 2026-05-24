from bookcraft.cursor.rules.Rule import CursorRule
from bookcraft.models import (
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
        config = context.config
        return CursorModifier(
            rule=(
                RuleType.ITALIC_START
                if self.type == ItalicType.START
                else RuleType.ITALIC_END
            ),
            cursor=Cursor(**config.italic_cursor),
            counter=-1,
        )
