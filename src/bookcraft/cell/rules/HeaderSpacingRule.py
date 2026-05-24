from bookcraft.cell.rules.Rule import CellRule
from bookcraft.models import Cell, Context


class HeaderSpacingRule(CellRule):
    def apply(self, context: Context) -> Cell:
        config = context.config
        return Cell(
            width=0,
            height=config.heading_spacing_height,
            text="",
            has_break=True,
            cursor=context.cursor,
        )
