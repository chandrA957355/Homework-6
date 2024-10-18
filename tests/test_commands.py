from multiprocessing import Process, Queue
import pytest
from decimal import Decimal
from calculator.commands import Command, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    command = AddCommand()
    assert command.execute(Decimal('2'), Decimal('3')) == Decimal('5')
    assert command.execute(Decimal('0'), Decimal('0')) == Decimal('0')
    assert command.execute(Decimal('-2'), Decimal('3')) == Decimal('1')

def test_subtract_command():
    command = SubtractCommand()
    assert command.execute(Decimal('5'), Decimal('3')) == Decimal('2')
    assert command.execute(Decimal('0'), Decimal('0')) == Decimal('0')
    assert command.execute(Decimal('-5'), Decimal('3')) == Decimal('-8')

def test_multiply_command():
    command = MultiplyCommand()
    assert command.execute(Decimal('2'), Decimal('3')) == Decimal('6')
    assert command.execute(Decimal('0'), Decimal('3')) == Decimal('0')
    assert command.execute(Decimal('-2'), Decimal('3')) == Decimal('-6')

def test_divide_command():
    command = DivideCommand()
    assert command.execute(Decimal('6'), Decimal('3')) == Decimal('2')
    assert command.execute(Decimal('1'), Decimal('1')) == Decimal('1')

    with pytest.raises(ValueError):
        command.execute(Decimal('1'), Decimal('0')) 

def test_command_abstract():
    with pytest.raises(NotImplementedError):
        command = Command()
        command.execute(Decimal('1'), Decimal('1'))

def test_add_command_multiprocessing():
    command = AddCommand()
    a = Decimal('10')
    b = Decimal('5')
    result_queue = Queue()

    process = Process(target=command.execute_multiprocessing, args=(a, b, result_queue))
    process.start()
    process.join()  

    assert result_queue.get() == a + b

def test_subtract_command_multiprocessing():
    command = SubtractCommand()
    a = Decimal('10')
    b = Decimal('5')
    result_queue = Queue()

    process = Process(target=command.execute_multiprocessing, args=(a, b, result_queue))
    process.start()
    process.join()

    assert result_queue.get() == a - b

def test_multiply_command_multiprocessing():
    command = MultiplyCommand()
    a = Decimal('10')
    b = Decimal('5')
    result_queue = Queue()

    process = Process(target=command.execute_multiprocessing, args=(a, b, result_queue))
    process.start()
    process.join()

    assert result_queue.get() == a * b

def test_divide_command_multiprocessing():
    command = DivideCommand()
    a = Decimal('10')
    b = Decimal('5')
    result_queue = Queue()

    process = Process(target=command.execute_multiprocessing, args=(a, b, result_queue))
    process.start()
    process.join()

    assert result_queue.get() == a / b

def test_divide_command_by_zero_multiprocessing():
    command = DivideCommand()
    a = Decimal('10')
    b = Decimal('0')
    result_queue = Queue()

    process = Process(target=command.execute_multiprocessing, args=(a, b, result_queue))
    process.start()
    process.join()

    result = result_queue.get_nowait() 

    assert isinstance(result, ValueError)
    assert str(result) == "Cannot divide by zero"

