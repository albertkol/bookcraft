from classes.config import CONFIG
from classes.cursor.rules.Rule import CursorRule
from classes.models import Context, Cursor, CursorModifier, RuleType


class ContentsItemRulenRule(CursorRule):
    def apply(self, context: Context) -> CursorModifier:
        return CursorModifier(
            rule=RuleType.CONTENTS_ITEM,
            cursor=Cursor(
                size=15,
                family=CONFIG.TEXT["heading"]["cursor"]["family"],
                style="I",
            ),
            counter=2,
        )
