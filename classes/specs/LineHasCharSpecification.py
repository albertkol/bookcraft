from classes.models import Context
from classes.specs.Specification import Specification


class LineHasCharSpecification(Specification):
    def __init__(self, chars: list[str], which_line: int = 0):
        self.chars = chars
        self.which_line = which_line

    def is_satisfied(self, context: Context) -> bool:
        page = context.memory[0]
        try:
            line = page[context.i + self.which_line]
        except IndexError:
            return False

        return any(char in line for char in self.chars)
