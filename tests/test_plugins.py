import os
from main import load_plugins

from calculator.plugins.add_command import AddCommand
from calculator.plugins.subtract_command import SubtractCommand
from calculator.plugins.multiply_command import MultiplyCommand
from calculator.plugins.divide_command import DivideCommand
from decimal import Decimal
import pytest

def test_add_plugin():
    command = AddCommand()
    assert command.execute(Decimal('2'), Decimal('3')) == Decimal('5')

def test_subtract_plugin():
    command = SubtractCommand()
    assert command.execute(Decimal('5'), Decimal('3')) == Decimal('2')

def test_multiply_plugin():
    command = MultiplyCommand()
    assert command.execute(Decimal('2'), Decimal('3')) == Decimal('6')

def test_divide_plugin():
    command = DivideCommand()
    assert command.execute(Decimal('6'), Decimal('3')) == Decimal('2')

    with pytest.raises(ValueError):
        command.execute(Decimal('1'), Decimal('0'))

def test_load_plugins():
    commands = load_plugins()
    
    assert 'add' in commands
    assert 'subtract' in commands
    assert 'multiply' in commands
    assert 'divide' in commands

    assert commands['add'].__class__.__name__ == 'AddCommand'
    assert commands['subtract'].__class__.__name__ == 'SubtractCommand'
    assert commands['multiply'].__class__.__name__ == 'MultiplyCommand'
    assert commands['divide'].__class__.__name__ == 'DivideCommand'
