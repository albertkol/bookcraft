from classes.cell.rules.Rule import CellRule
from classes.models import Cell, Context


class HeaderSpacingRule(CellRule):
    def apply(self, context: Context) -> Cell:
        CONFIG = context.config
        return Cell(
            width=0,
            height=CONFIG.HEADING_SPACING_HEIGHT,
            text="",
            has_break=True,
            cursor=context.cursor,
        )
