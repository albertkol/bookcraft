from classes.models import Context
from classes.specs.Specification import Specification


class IsEndOfLineSpecification(Specification):
    def is_satisfied(self, context: Context) -> bool:
        page = context.memory[0]
        line = page[context.i]
        line_length = len(line)

        return context.j == line_length - 1
