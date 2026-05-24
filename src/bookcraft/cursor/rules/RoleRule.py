from bookcraft.cursor.rules.Rule import CursorRule
from bookcraft.helpers import next_chars_matches
from bookcraft.models import Context, Cursor, CursorModifier, RuleType


class RoleRule(CursorRule):
    def apply(self, context: Context) -> CursorModifier:
        config = context.config
        role, _ = next_chars_matches(
            chars=list(config.roles.keys()),
            i=context.i,
            j=context.j,
            memory=context.memory,
            inclusive=False,
        )

        fill = config.roles[role].light if role else config.default_fill

        return CursorModifier(
            rule=RuleType.ROLE_HIGHLIGHT,
            cursor=Cursor(fill=fill),
            counter=-1,
        )
