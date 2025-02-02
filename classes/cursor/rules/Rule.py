from abc import ABC, abstractmethod
from typing import Optional

from classes.models import Context, CursorModifier
from classes.specs.Specification import Specification


class CursorRule(ABC):
    @abstractmethod
    def apply(self, context: Context) -> CursorModifier:
        pass


class CursorSpecificationRule(CursorRule):
    def __init__(self, specification: Specification, rule: CursorRule) -> None:
        self.specification = specification
        self.rule = rule

    def apply(self, context: Context) -> Optional[CursorModifier]:
        if self.specification.is_satisfied(context):
            return self.rule.apply(context)

        return None
