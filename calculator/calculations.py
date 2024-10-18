"""
Calculations Class

A class to handle a history of calculations is defined in this module.
It enables the addition, removal, retrieval, and filtering of calculations
according on the operation performed.

"""

from calculator.calculation import Calculation
from decimal import Decimal
from typing import Callable, List

class calculations:
    """
    A class to manage a history of calculations.

    Attributes:
        history (List[Calculation]): A list to store calculation instances.

    Methods:
        add_calculation(calculation: Calculation):
            Adds a new Calculation instance to the history.
        
        delete_calculation():
            Clears the entire history of calculations.
        
        get_latest() -> Calculation:
            Returns the most recent Calculation instance, or None if the history is empty.
        
        print_all_calculation() -> List[Calculation]:
            Returns all Calculation instances in the history.
        
        filter_with_operation(operation: str) -> List[Calculation]:
            Returns a list of Calculation instances that match the specified operation.
    """
    
    history = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """
        Add a new Calculation instance to the history.

        Args:
            calculation (Calculation): The Calculation instance to add.
        """
        cls.history.append(calculation)
    
    @classmethod
    def delete_calculation(cls):
        """
        Clear the entire history of calculations.
        """
        cls.history.clear()
        
    @classmethod
    def get_latest(cls) -> Calculation:
        """
        Retrieve the most recent Calculation instance.

        Returns:
            Calculation: The latest Calculation instance, or None if the history is empty.
        """
        if cls.history:
            return cls.history[-1]
        return None
    
    @classmethod
    def print_all_calculation(cls) -> List[Calculation]:
        """
        Retrieve all Calculation instances in the history.

        Returns:
            List[Calculation]: A list of all Calculation instances.
        """
        return cls.history

    @classmethod
    def filter_with_operation(cls, operation: str) -> List[Calculation]:
        """
        Filter Calculation instances based on the specified operation.

        Args:
            operation (str): The name of the operation to filter by.

        Returns:
            List[Calculation]: A list of Calculation instances that match the operation.
        """
        return [calc for calc in cls.history if calc.operation.__name__ == operation]
