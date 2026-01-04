from .HelpCommand import HelpCommand
from .BenchmarkCommand import BenchmarkCommand
from .DemoSignatureCommand import DemoSignatureCommand

commands = {
    '--help': HelpCommand,
    '--benchmark': BenchmarkCommand,
    '--demo-signature': DemoSignatureCommand,
}

def getCommand(commandName: str):
    return commands.get(commandName, HelpCommand)()