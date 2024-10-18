''' 
Calculations Test Module 

This module contains unit tests for the calculations history management. 
It verifies that the operations can be added, retrieved, deleted, and 
filtered correctly using pytest.
'''

from decimal import Decimal
import pytest

from calculator.calculation import Calculation
from calculator.calculations import calculations
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def sample_operations():
    '''
    Fixture to add sample operations into the history for test cases.

    This function clears any existing calculations and adds four 
    sample calculations to the history.
    '''
    calculations.delete_calculation()

    calculations.add_calculation(Calculation(Decimal('2'), Decimal('3'), add))
    calculations.add_calculation(Calculation(Decimal('4'), Decimal('3'), subtract))
    calculations.add_calculation(Calculation(Decimal('10'), Decimal('3'), multiply))
    calculations.add_calculation(Calculation(Decimal('9'), Decimal('3'), divide))

def test_add_calculation():
    '''
    Test adding a calculation to the history.

    This test creates a Calculation instance and checks if it 
    is successfully added to the calculations history.
    '''
    add_obj = Calculation(Decimal('5'), Decimal('3'), add)
    calculations.add_calculation(add_obj)
    assert calculations.get_latest() == add_obj, "History addition failed."

def test_get_all_history(sample_operations):
    '''
    Test retrieving all calculations from history.

    This test verifies that the total number of entries in the 
    history matches the expected count after sample operations 
    have been added.
    '''
    history = calculations.print_all_calculation()
    assert len(history) == 4, "All history count is not correct."

def test_delete_history():
    '''
    Test clearing the calculation history.

    This test checks if the delete_calculation method successfully 
    clears all entries in the history.
    '''
    calculations.delete_calculation()
    assert len(calculations.print_all_calculation()) == 0, "Delete history failed."

def test_get_latest_calculation(sample_operations):
    '''
    Test retrieving the latest calculation from history.

    This test verifies that the latest calculation is the correct 
    one based on the previously added sample operations.
    '''
    latest = calculations.get_latest()
    assert latest.a == Decimal('9') and latest.b == Decimal('3'), "Get latest failed."

def test_get_latest_after_clear():
    '''
    Test retrieving the latest calculation after clearing history.

    This test verifies that the history is empty after being cleared 
    and that get_latest returns None.
    '''
    calculations.delete_calculation()
    assert calculations.get_latest() is None, "Get history should be empty."

def test_find_by_operation(sample_operations):
    '''
    Test filtering calculations by operation.

    This test checks if the filtering functionality correctly 
    returns the number of operations for specific arithmetic 
    operations (add, multiply).
    '''
    add_find = calculations.filter_with_operation("add")
    assert len(add_find) == 1, "Count of add operations doesn't match."
    multiply_filter = calculations.filter_with_operation("multiply")
    assert len(multiply_filter) == 1, "count of multiply operations doesnt match"
