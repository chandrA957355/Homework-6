"""
Calculator Module

The addition, subtraction, multiplication, and division of fundamental arithmetic operations are 
supported by this module's simple calculator implementation. For precise numerical calculations, 
it makes use of the Decimal class and saves each result for probable future use.

"""

from calculator.operations import add, subtract, divide, multiply
from calculator.calculation import Calculation
from calculator.calculations import calculations
from decimal import Decimal
from typing import Callable

class Calculator:
    """
    A class that encapsulates basic arithmetic operations.

    Methods:
        perform(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
            Performs the given operation on two Decimal numbers and logs the calculation.
        
        add(a: Decimal, b: Decimal) -> Decimal:
            Returns the sum of two Decimal numbers.
        
        subtract(a: Decimal, b: Decimal) -> Decimal:
            Returns the difference between two Decimal numbers.
        
        multiply(a: Decimal, b: Decimal) -> Decimal:
            Returns the product of two Decimal numbers.
        
        divide(a: Decimal, b: Decimal) -> Decimal:
            Returns the quotient of two Decimal numbers.
    """

    @staticmethod
    def perform(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """
        Perform a calculation with the specified operation and stores history.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.
            operation (Callable[[Decimal, Decimal], Decimal]): The arithmetic operation to perform.

        Returns:
            Decimal: The result of the operation.
        """
        # Create a Calculation object and log it
        calculation = Calculation.create(a, b, operation)
        calculations.add_calculation(calculation)
        # Execute the operation and return the result
        return calculation.operate()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """
        Add two Decimal numbers.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.

        Returns:
            Decimal: The sum of a and b.
        """
        return Calculator.perform(a, b, add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """
        Subtract one Decimal number from another.

        Args:
            a (Decimal): The minuend.
            b (Decimal): The subtrahend.

        Returns:
            Decimal: The result of a - b.
        """
        return Calculator.perform(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """
        Multiply two Decimal numbers.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.

        Returns:
            Decimal: The product of a and b.
        """
        return Calculator.perform(a, b, multiply)
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """
        Divide one Decimal number by another.

        Args:
            a (Decimal): The dividend.
            b (Decimal): The divisor.

        Returns:
            Decimal: The result of a / b.
        
        Raises:
            ZeroDivisionError: If b is zero.
        """
        return Calculator.perform(a, b, divide)
