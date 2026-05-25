from bookcraft.models import Cursor, CursorModifier, RuleType


class CursorModifierReducer:
    def reduce(self, modifiers: list[CursorModifier]) -> Cursor:
        is_bold = self._is_bold(modifiers)
        is_italic = self._is_italic(modifiers)
        is_underline = self._is_underline(modifiers)

        cursor = Cursor(
            is_bold=is_bold,
            is_italic=is_italic,
            is_underline=is_underline,
        )

        for modifier in modifiers:
            cursor.family = modifier.cursor.family or cursor.family
            cursor.size = modifier.cursor.size or cursor.size
            cursor.colour = modifier.cursor.colour or cursor.colour
            cursor.fill = modifier.cursor.fill or cursor.fill

        style = ""
        if is_bold:
            style += "B"
        elif is_italic:
            style += "I"
        if is_underline:
            style += "U"
        cursor.style = style

        return cursor

    def _is_bold(self, modifiers: list[CursorModifier]) -> bool:
        return any(modifier.rule == RuleType.KEYWORD for modifier in modifiers)

    def _is_italic(self, modifiers: list[CursorModifier]) -> bool:
        return any(modifier.rule == RuleType.ITALIC_START for modifier in modifiers)

    def _is_underline(self, modifiers: list[CursorModifier]) -> bool:
        return any(modifier.rule == RuleType.UNDERLINE_START for modifier in modifiers)
