from bookcraft.helpers import next_chars_matches
from bookcraft.models import Context
from bookcraft.specs.Specification import Specification


class NextCharEquals(Specification):
    def __init__(self, chars: list[str]):
        self.chars = chars

    def is_satisfied(self, context: Context) -> bool:
        match, _ = next_chars_matches(
            chars=self.chars,
            i=context.i,
            j=context.j,
            memory=context.memory,
            inclusive=False,
        )

        return match is not None
