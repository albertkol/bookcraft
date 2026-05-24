from bookcraft.cell.rules.Rule import CellRule
from bookcraft.models import Cell, Context


class BreakLineRule(CellRule):
    def apply(self, context: Context) -> Cell:
        CONFIG = context.config
        return Cell(
            width=0,
            height=CONFIG.DEFAULT_HEIGHT,
            text="",
            has_break=True,
            cursor=context.cursor,
        )
