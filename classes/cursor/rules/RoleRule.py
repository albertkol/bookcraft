from classes.cursor.rules.Rule import CursorRule
from classes.helpers import next_chars_matches
from classes.models import Context, Cursor, CursorModifier, RuleType


class RoleRule(CursorRule):
    def apply(self, context: Context) -> CursorModifier:
        CONFIG = context.config
        role, _ = next_chars_matches(
            chars=CONFIG.ROLES.keys(),
            i=context.i,
            j=context.j,
            memory=context.memory,
            inclusive=False,
        )

        fill = CONFIG.ROLES[role]["light"] if role else CONFIG.DEFAULT_FILL

        return CursorModifier(
            rule=RuleType.ROLE_HIGHLIGHT,
            cursor=Cursor(fill=fill),
            counter=-1,
        )
