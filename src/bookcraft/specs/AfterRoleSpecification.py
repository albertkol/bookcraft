from bookcraft.helpers import previous_chars_matches
from bookcraft.models import Context
from bookcraft.specs.Specification import Specification


class AfterRoleSpecification(Specification):
    def is_satisfied(self, context: Context) -> bool:
        roles = [f"${role}" for role in context.config.roles.keys()]
        asb = previous_chars_matches(
            chars=roles,
            i=context.i,
            j=context.j,
            memory=context.memory,
        )

        return asb is not None
