from classes.cursor.rules.Rule import CursorRule
from classes.models import Context, Cursor, CursorModifier, RuleType


class BlankSpaceRule(CursorRule):
    def apply(self, context: Context) -> CursorModifier:
        counter = 1
        page = context.memory[0]
        line = page[context.i]
        index = context.j
        while index <= len(line) - 1 and line[index] in [" ", ",", ".", ":", ";"]:
            counter += 1
            index += 1

        CONFIG = context.config
        return CursorModifier(
            rule=RuleType.BLANK_SPACE,
            cursor=Cursor(fill=CONFIG.DEFAULT_FILL),
            counter=counter,
        )
