from bookcraft.models import CursorModifier, RuleType


class CursorModifierProcessor:
    def process(self, modifiers: list[CursorModifier]) -> list[CursorModifier]:
        if not modifiers:
            return modifiers

        last_modifier = modifiers[-1]

        if last_modifier.rule in (RuleType.DEFAULT, RuleType.TITLE):
            modifiers = [last_modifier]

        modifiers = self._handle_end(
            modifiers, RuleType.ITALIC_END, RuleType.ITALIC_START
        )
        modifiers = self._handle_end(
            modifiers, RuleType.UNDERLINE_END, RuleType.UNDERLINE_START
        )

        refreshed_modifiers = self._decrease_counter(modifiers)

        return refreshed_modifiers

    def _handle_end(
        self,
        modifiers: list[CursorModifier],
        end_type: RuleType,
        start_type: RuleType,
    ) -> list[CursorModifier]:
        if not any(m.rule == end_type for m in modifiers):
            return modifiers
        for modifier in reversed(modifiers):
            if modifier.rule == start_type:
                modifier.counter = 2
                break
        return [m for m in modifiers if m.rule != end_type]

    def _decrease_counter(
        self, modifiers: list[CursorModifier]
    ) -> list[CursorModifier]:
        for modifier in modifiers:
            if modifier.counter == -1:
                continue

            modifier.counter -= 1

        return [modifier for modifier in modifiers if modifier.counter != 0]
