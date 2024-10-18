from decimal import Decimal
import pytest
from main import perform_calculation_and_display, run_repl
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_perform_calculation_and_display(capsys):
    commands = {
        'add': AddCommand(),
        'subtract': SubtractCommand(),
        'multiply': MultiplyCommand(),
        'divide': DivideCommand()
    }

    perform_calculation_and_display('5', '3', 'add', commands)
    captured = capsys.readouterr()
    assert "The result of 5 add 3 is 8" in captured.out

    perform_calculation_and_display('invalid', '3', 'add', commands)
    captured = capsys.readouterr()
    assert "Invalid number input: invalid or 3 is not a valid number." in captured.out

    perform_calculation_and_display('5', '3', 'unknown', commands)
    captured = capsys.readouterr()
    assert "Unknown operation: unknown" in captured.out

    perform_calculation_and_display('5', '0', 'divide', commands)
    captured = capsys.readouterr()
    assert "Error: Cannot divide by zero" in captured.out

def test_run_repl(monkeypatch, capsys):
    commands = {
        'add': AddCommand(),
        'subtract': SubtractCommand(),
        'multiply': MultiplyCommand(),
        'divide': DivideCommand()
    }

    inputs = iter(['add 2 3', 'subtract 5 3', 'divide 4 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    run_repl(commands)
    
    captured = capsys.readouterr()
    assert "Result: 5" in captured.out
    assert "Result: 2" in captured.out
    assert "Error: Cannot divide by zero" in captured.out

def test_menu_command(capsys):
    from calculator.plugins.menu_command import MenuCommand
    commands = {
        'add': AddCommand(),
        'subtract': SubtractCommand(),
        'multiply': MultiplyCommand(),
        'divide': DivideCommand(),
        'menu': MenuCommand(),
    }

    commands['menu'].execute(commands)
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out
    assert " - add" in captured.out
    assert " - subtract" in captured.out
    assert " - multiply" in captured.out
    assert " - divide" in captured.out
