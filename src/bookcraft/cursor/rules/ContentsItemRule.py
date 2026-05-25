from bookcraft.cursor.rules.Rule import CursorRule
from bookcraft.models import Context, Cursor, CursorModifier, RuleType


class ContentsItemRulenRule(CursorRule):
    def apply(self, context: Context) -> CursorModifier:
        return CursorModifier(
            rule=RuleType.CONTENTS_ITEM,
            cursor=Cursor(
                size=13,
                family="Montserrat Regular",
                style="",
            ),
            counter=2,
        )
