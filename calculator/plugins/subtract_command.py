from decimal import Decimal
from calculator.commands import Command

class SubtractCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a - b
