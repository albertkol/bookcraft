from typing import Optional

from bookcraft.cursor.rules.Rule import CursorRule
from bookcraft.helpers import next_chars_matches
from bookcraft.models import Context, Cursor, CursorModifier, RuleType


class KeywordRule(CursorRule):
    def apply(self, context: Context) -> Optional[CursorModifier]:
        config = context.config
        match, bold_count = next_chars_matches(
            chars=config.keywords,
            i=context.i,
            j=context.j,
            memory=context.memory,
        )

        if not match:
            return None

        return CursorModifier(
            rule=RuleType.KEYWORD,
            cursor=Cursor(**config.bold_cursor),
            counter=bold_count + 1,
        )
