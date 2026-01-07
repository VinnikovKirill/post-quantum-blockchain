from .AbstractCommand import AbstractCommand
from src.Command.Handler.HelpCommandHandler import HelpCommandHandler

class HelpCommand(AbstractCommand):
    def execute(self):
        (HelpCommandHandler())()