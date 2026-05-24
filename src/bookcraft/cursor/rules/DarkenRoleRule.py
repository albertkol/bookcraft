from bookcraft.cursor.rules.Rule import CursorRule
from bookcraft.helpers import next_chars_matches
from bookcraft.models import Context, Cursor, CursorModifier, RuleType


class DarkenRoleRule(CursorRule):
    def apply(self, context: Context) -> CursorModifier:
        config = context.config
        role, counter = next_chars_matches(
            chars=config.roles.keys(),
            i=context.i,
            j=context.j,
            memory=context.memory,
            inclusive=False,
        )

        fill = config.roles[role].dark if role else config.default_fill

        return CursorModifier(
            rule=RuleType.ROLE_HIGHLIGHT,
            cursor=Cursor(fill=fill),
            counter=counter + 2,
        )
