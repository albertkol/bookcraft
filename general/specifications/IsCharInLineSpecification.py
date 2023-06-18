from general.interfaces.specification import Specification


class IsCharInLineSpecification(Specification):
    def is_satisfied(self, line: str) -> bool:
        return self.char in line
