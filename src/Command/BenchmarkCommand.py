from .AbstractCommand import AbstractCommand
from src.Command.Handler.BenchmarkCommandHandler import BenchmarkCommandHandler

class BenchmarkCommand(AbstractCommand):
    def execute(self):
        (BenchmarkCommandHandler())()