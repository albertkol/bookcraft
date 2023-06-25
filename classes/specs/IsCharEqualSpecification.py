from classes.models import Context
from classes.specs.Specification import Specification


class IsCharEqualSpecification(Specification):
    def __init__(self, chars: list[str]):
        self.chars = chars

    def is_satisfied(self, context: Context) -> bool:
        page = context.memory[0]
        char = page[context.i][context.j]

        return char in self.chars
