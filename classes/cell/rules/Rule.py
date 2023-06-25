from abc import ABC, abstractmethod
from typing import Optional

from classes.models import Cell, Context
from classes.specs.Specification import Specification


class CellRule(ABC):
    @abstractmethod
    def apply(self, context: Context) -> Cell:
        pass


class CellSpecificationRule(CellRule):
    def __init__(self, specification: Specification, rule: CellRule) -> None:
        self.specification = specification
        self.rule = rule

    def apply(self, context: Context) -> Optional[Cell]:
        if self.specification.is_satisfied(context):
            return self.rule.apply(context)

        return None
