from classes.models import Context
from classes.specs.Specification import Specification


class isBoldSpecification(Specification):
    def is_satisfied(self, context: Context) -> bool:
        return context.cursor.is_bold
