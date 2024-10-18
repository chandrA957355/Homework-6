import multiprocessing
import sys
import importlib
import os
from decimal import Decimal, InvalidOperation

from collections import OrderedDict
import logging
import logging.config
from dotenv import load_dotenv


def load_environment_variables():
    load_dotenv()
    settings = {key: value for key, value in os.environ.items()}
    logging.info("Environment variables loaded.")
    return settings


def configure_logging():
    os.makedirs("logs", exist_ok=True)
    logging_conf_path = "logging.conf"
    if os.path.exists(logging_conf_path):
        logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
    else:
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
    logging.info("Logging configured.")


def load_plugins():
    commands = OrderedDict()
    plugins_dir = os.path.join('calculator', 'plugins')

    for filename in os.listdir(plugins_dir):
        if filename.endswith('_command.py'):
            module_name = filename[:-3]  
            module = importlib.import_module(f'calculator.plugins.{module_name}')
            command_class = getattr(module, module_name[:-8].capitalize() + 'Command')
            commands[module_name[:-8]] = command_class()  

    return commands


def perform_calculation_and_display(num1, num2, operation_type, commands, use_multiprocessing=False):
    """
    Performs the specified arithmetic operation on two numbers, using multiprocessing if chosen.
    """
    try:
        decimal_num1, decimal_num2 = map(Decimal, [num1, num2])
        operation_function = commands.get(operation_type)
        if not operation_function:
            print(f"Unknown operation: {operation_type}")
            return
        
        if use_multiprocessing:
            result_queue = multiprocessing.Queue()

            process = multiprocessing.Process(
                target=operation_function.execute_multiprocessing,
                args=(decimal_num1, decimal_num2, result_queue)
            )
            process.start()
            process.join()

            result = result_queue.get()
            print(f"The result of {num1} {operation_type} {num2} using multiprocessing is {result}")
        else:
            result = operation_function.execute(decimal_num1, decimal_num2)
            print(f"The result of {num1} {operation_type} {num2} is {result}")

    except InvalidOperation:
        print(f"Invalid number input: {num1} or {num2} is not a valid number.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")



def main():
    """
    Main function to handle command-line arguments and initiate the calculation.
    """
    commands = load_plugins()  

    if len(sys.argv) == 4:  
        _, num1, num2, operation_type = sys.argv
        perform_calculation_and_display(num1, num2, operation_type, commands)
        
    elif len(sys.argv) == 5:  
        _, num1, num2, operation_type, mp_flag = sys.argv
        use_multiprocessing = mp_flag == "mp"
        perform_calculation_and_display(num1, num2, operation_type, commands, use_multiprocessing)
    
    elif len(sys.argv) == 2 and sys.argv[1] == 'repl':  
        run_repl(commands)
        
    else:
        print("Usage: python main.py <number1> <number2> <operation> [mp] or python main.py repl")



def run_repl(commands):
    """
    Run the REPL (Read-Eval-Print Loop) for interactive calculations.
    """
    print("Entering REPL mode. Type 'exit' to quit.")
    print("Add 'mp' at the end of a command to use multiprocessing.")
    
    while True:
        user_input = input("Enter command: ")
        if user_input == 'exit':
            print("Exiting REPL mode...")
            break
        elif user_input == 'menu':
            commands['menu'].execute(commands)  
            continue

        parts = user_input.split()
        if len(parts) not in [3, 4]:  
            print("Usage: <command> <num1> <num2> [mp]")
            continue

        command_name, num1, num2 = parts[:3]
        use_multiprocessing = len(parts) == 4 and parts[3] == 'mp'

        if command_name not in commands:
            print(f"Unknown command: {command_name}")
            continue

        try:
            decimal_num1 = Decimal(num1)
            decimal_num2 = Decimal(num2)

            if use_multiprocessing:
                result_queue = multiprocessing.Queue()
                process = multiprocessing.Process(
                    target=commands[command_name].execute_multiprocessing,
                    args=(decimal_num1, decimal_num2, result_queue)
                )
                process.start()
                process.join()

                result = result_queue.get()
                print(f"Result using multiprocessing: {result}")
            else:
                result = commands[command_name].execute(decimal_num1, decimal_num2)
                print(f"Result: {result}")

        except (ValueError, InvalidOperation) as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    configure_logging()
    settings = load_environment_variables()

    logging.info(f"Environment: {settings.get('ENVIRONMENT')}")
    logging.info("Application started.")
    main()
