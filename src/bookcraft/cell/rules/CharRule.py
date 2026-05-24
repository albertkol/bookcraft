from bookcraft.cell.rules.Rule import CellRule
from bookcraft.models import Cell, Context


class CharRule(CellRule):
    def apply(self, context: Context) -> Cell:
        config = context.config
        page = context.memory[0]
        char = page[context.i][context.j]

        return Cell(
            width=0,
            height=config.default_height,
            text=char,
            cursor=context.cursor,
            has_fill=True,
        )
