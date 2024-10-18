''' My Calculator Test with Calculator object'''
import pytest
from calculator import Calculator

def test_add():
    '''Tests the addition operation with two decimals passed to the Calculator object'''
    result = Calculator.add(2,3)
    assert  result == 5

def test_subtract():
    '''Tests the subtraction operation with two decimals passed to the Calculator object'''
    assert Calculator.subtract(5,3) == 2

def test_multiply():
    '''Tests the multiplication operation with two decimals passed to the Calculator object'''
    assert Calculator.multiply(4,5) == 20

def test_divide():
    '''Tests the division operation with two decimals passed to the Calculator object'''
    assert Calculator.divide(10,2) == 5

def test_dividebyzero():
    '''Tests if the divide function throws an error when divided by zero'''
    with pytest.raises(ValueError):
        Calculator.divide(10,0)
