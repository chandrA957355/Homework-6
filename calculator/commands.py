import multiprocessing
from decimal import Decimal


class Command:
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        raise NotImplementedError("Each command must implement the execute method.")
    def execute_multiprocessing(self, a: Decimal, b: Decimal, result_queue):
        """Execute the command in a separate process and put the result in a queue."""
        try:
           result = self.execute(a, b)
           result_queue.put(result)
        except Exception as e:
           result_queue.put(e) 

#command pattern reference
class AddCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a + b

class SubtractCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a - b

class MultiplyCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a * b

class DivideCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
