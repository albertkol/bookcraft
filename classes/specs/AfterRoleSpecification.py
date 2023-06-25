from classes.helpers import previous_chars_matches
from classes.models import Context
from classes.specs.Specification import Specification


class AfterRoleSpecification(Specification):
    def is_satisfied(self, context: Context) -> bool:
        roles = [f"${role}" for role in context.config.ROLES.keys()]
        asb = previous_chars_matches(
            chars=roles,
            i=context.i,
            j=context.j,
            memory=context.memory,
        )

        return asb
