from dataclasses import dataclass

from classes.cell.rules.BreakLineRule import BreakLineRule
from classes.cell.rules.CharRule import CharRule
from classes.cell.rules.HeaderSpacingRule import HeaderSpacingRule
from classes.cell.rules.Rule import CellRule, CellSpecificationRule
from classes.models import Cell, Context
from classes.specs.FirstLineSpecification import FirstLineSpecification
from classes.specs.IsCharEqualSpecification import IsCharEqualSpecification
from classes.specs.IsEndOfLineSpecification import IsEndOfLineSpecification
from classes.specs.LineHasCharSpecification import LineHasCharSpecification
from classes.specs.Specification import AndSpecification, NotSpecification


@dataclass
class CellFactory:
    rules: tuple[CellRule, ...] = (
        CellSpecificationRule(
            AndSpecification(
                NotSpecification(LineHasCharSpecification(["#"], -1)),
                IsCharEqualSpecification(["#"]),
                NotSpecification(FirstLineSpecification()),
            ),
            HeaderSpacingRule(),
        ),
        CellSpecificationRule(
            NotSpecification(
                IsCharEqualSpecification(["#", ">", "$", "<", "/", "%", "&"])
            ),
            CharRule(),
        ),
        CellSpecificationRule(
            IsEndOfLineSpecification(),
            BreakLineRule(),
        ),
        CellSpecificationRule(
            AndSpecification(
                IsEndOfLineSpecification(),
                LineHasCharSpecification(["#"], 0),
                NotSpecification(LineHasCharSpecification(["#"], 1)),
            ),
            HeaderSpacingRule(),
        ),
    )

    def create_cells(self, context: Context) -> list[Cell]:
        cells = []
        for rule in self.rules:
            cell = rule.apply(context)

            if cell is None:
                continue

            cells.append(cell)

        return cells
