from classes.models import Context
from classes.specs.Specification import Specification


class FirstLineSpecification(Specification):
    def is_satisfied(self, context: Context) -> bool:
        return context.i == 0
