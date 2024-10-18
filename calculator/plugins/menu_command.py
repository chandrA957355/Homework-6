from calculator.commands import Command

class MenuCommand(Command):
    def execute(self, commands_dict):
        print("Available commands:")
        for command in commands_dict.keys():
            print(f" - {command}")
