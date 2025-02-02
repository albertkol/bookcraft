from abc import ABC, abstractmethod
from typing import Optional

from classes.models import Context


class Specification(ABC):
    @abstractmethod
    def is_satisfied(self, context: Context) -> bool:
        pass


class AndSpecification(Specification):
    def __init__(
        self,
        spec1: Specification,
        spec2: Specification,
        spec3: Optional[Specification] = None,
    ):
        self.spec1 = spec1
        self.spec2 = spec2
        self.spec3 = spec3

    def is_satisfied(self, context: Context) -> bool:
        spec1 = self.spec1.is_satisfied(context)
        spec2 = self.spec2.is_satisfied(context)
        if self.spec3 is None:
            return spec1 and spec2

        spec3 = self.spec3.is_satisfied(context)
        return spec1 and spec2 and spec3


class OrSpecification(Specification):
    def __init__(self, spec1: Specification, spec2: Specification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied(self, context: Context) -> bool:
        return self.spec1.is_satisfied(context) or self.spec2.is_satisfied(
            context
        )


class NotSpecification(Specification):
    def __init__(self, spec: Specification):
        self.spec = spec

    def is_satisfied(self, context: Context) -> bool:
        return not self.spec.is_satisfied(context)
