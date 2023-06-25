from classes.helpers import previous_chars_matches
from classes.models import Context
from classes.specs.Specification import Specification


class PreviousCharEquals(Specification):
    def __init__(self, chars: list[str]):
        self.chars = chars

    def is_satisfied(self, context: Context) -> bool:
        return previous_chars_matches(
            chars=self.chars,
            i=context.i,
            j=context.j,
            memory=context.memory,
        )
