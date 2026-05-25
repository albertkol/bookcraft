from bookcraft.cursor.rules.Rule import CursorRule
from bookcraft.models import Context, Cursor, CursorModifier, MarkerType, RuleType


class UnderlineRule(CursorRule):
    def __init__(self, marker: MarkerType) -> None:
        self.marker = marker

    def apply(self, context: Context) -> CursorModifier:
        config = context.config
        return CursorModifier(
            rule=(
                RuleType.UNDERLINE_START
                if self.marker == MarkerType.START
                else RuleType.UNDERLINE_END
            ),
            cursor=Cursor(**config.underline_cursor),
            counter=-1,
        )
