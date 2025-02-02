from classes.cell.rules.Rule import CellRule
from classes.models import Cell, Context


class CharRule(CellRule):
    def apply(self, context: Context) -> Cell:
        CONFIG = context.config
        page = context.memory[0]
        char = page[context.i][context.j]

        return Cell(
            width=0,
            height=CONFIG.DEFAULT_HEIGHT,
            text=char,
            cursor=context.cursor,
            has_fill=True,
        )
