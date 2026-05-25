from bookcraft.cursor.rules.Rule import CursorRule
from bookcraft.models import (
    Context,
    Cursor,
    CursorModifier,
    RuleType,
    UnderlineType,
)


class UnderlineRule(CursorRule):
    def __init__(self, type) -> None:
        self.type = type

    def apply(self, context: Context) -> CursorModifier:
        config = context.config
        return CursorModifier(
            rule=(
                RuleType.UNDERLINE_START
                if self.type == UnderlineType.START
                else RuleType.UNDERLINE_END
            ),
            cursor=Cursor(**config.underline_cursor),
            counter=-1,
        )
