from dataclasses import dataclass

from bookcraft.cell.rules.BreakLineRule import BreakLineRule
from bookcraft.cell.rules.CharRule import CharRule
from bookcraft.cell.rules.HeaderSpacingRule import HeaderSpacingRule
from bookcraft.cell.rules.Rule import CellRule, CellSpecificationRule
from bookcraft.models import Cell, Context
from bookcraft.specs.FirstLineSpecification import FirstLineSpecification
from bookcraft.specs.IsCharEqualSpecification import IsCharEqualSpecification
from bookcraft.specs.IsEndOfLineSpecification import IsEndOfLineSpecification
from bookcraft.specs.LineHasCharSpecification import LineHasCharSpecification
from bookcraft.specs.Specification import AndSpecification, NotSpecification


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
                IsCharEqualSpecification(["#", ">", "$", "<", "=", "%", "&", "@"])
            ),
            CharRule(),
        ),
        CellSpecificationRule(
            AndSpecification(
                IsEndOfLineSpecification(),
                NotSpecification(LineHasCharSpecification(["@"], 0)),
            ),
            BreakLineRule(),
        ),
        CellSpecificationRule(
            AndSpecification(
                IsEndOfLineSpecification(),
                LineHasCharSpecification(["@"], 0),
            ),
            HeaderSpacingRule(),
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
