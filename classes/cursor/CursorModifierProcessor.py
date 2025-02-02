from classes.models import CursorModifier, RuleType


class CursorModifierProcessor:
    def process(self, modifiers: list[CursorModifier]) -> list[CursorModifier]:
        if not modifiers:
            return modifiers

        last_modifier = modifiers[-1]

        if last_modifier.rule == RuleType.DEFAULT:
            modifiers = [last_modifier]

        if last_modifier.rule == RuleType.TITLE:
            modifiers = [last_modifier]

        if last_modifier.rule == RuleType.ITALIC_END:
            modifiers = modifiers[::-1]
            for i in range(len(modifiers)):
                modifier = modifiers[i]
                if modifier.rule == RuleType.ITALIC_START:
                    modifier.counter = 2
                    break
            modifiers = modifiers[::-1]
            modifiers.pop(-1)

        refreshed_modifiers = self._decrease_counter(modifiers)

        return refreshed_modifiers

    def _decrease_counter(
        self, modifiers: list[CursorModifier]
    ) -> list[CursorModifier]:
        for modifier in modifiers:
            if modifier.counter == -1:
                continue

            modifier.counter -= 1

        return [modifier for modifier in modifiers if modifier.counter != 0]
