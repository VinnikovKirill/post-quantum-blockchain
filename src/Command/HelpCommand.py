from .AbstractCommand import AbstractCommand

class HelpCommand(AbstractCommand):
    def execute(self):
        print('--help')