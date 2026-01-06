from .HelpCommand import HelpCommand
from .BenchmarkCommand import BenchmarkCommand
from .SignatureCommand import SignatureCommand
from .AbstractCommand import AbstractCommand

commands = {
    '--help': HelpCommand,
    '--benchmark': BenchmarkCommand,
    '--signature': SignatureCommand,
}

def getCommand(commandName: str) -> AbstractCommand:
    return commands.get(commandName, HelpCommand)()