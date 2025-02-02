from classes.cursor.rules.Rule import CursorRule
from classes.helpers import next_chars_matches
from classes.models import Context, Cursor, CursorModifier, RuleType


class DarkenRoleRule(CursorRule):
    def apply(self, context: Context) -> CursorModifier:
        CONFIG = context.config
        role, counter = next_chars_matches(
            chars=CONFIG.ROLES.keys(),
            i=context.i,
            j=context.j,
            memory=context.memory,
            inclusive=False,
        )

        fill = CONFIG.ROLES[role]["dark"] if role else CONFIG.DEFAULT_FILL

        return CursorModifier(
            rule=RuleType.ROLE_HIGHLIGHT,
            cursor=Cursor(fill=fill),
            counter=counter + 2,
        )
