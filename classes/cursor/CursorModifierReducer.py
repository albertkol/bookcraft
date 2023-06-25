from classes.models import Cursor, CursorModifier, RuleType


class CursorModifierReducer:
    def reduce(self, modifiers: list[CursorModifier]) -> Cursor:
        cursor = Cursor(
            is_bold=self._is_bold(modifiers),
            is_italic=self._is_italic(modifiers),
        )

        for modifier in modifiers:
            cursor.family = modifier.cursor.family or cursor.family
            cursor.style = modifier.cursor.style or cursor.style or ""
            cursor.size = modifier.cursor.size or cursor.size
            cursor.colour = modifier.cursor.colour or cursor.colour
            cursor.fill = modifier.cursor.fill or cursor.fill

        return cursor

    def _is_bold(self, modifiers: list[CursorModifier]) -> bool:
        return modifiers and modifiers[-1].rule == RuleType.KEYWORD

    def _is_italic(self, modifiers: list[CursorModifier]) -> bool:
        return any(
            modifier
            for modifier in modifiers
            if modifier.rule == RuleType.ITALIC_START
        )
