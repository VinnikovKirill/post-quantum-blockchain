import sys

class AbstractCommand:
    def execute(self):
        pass

class BenchmarkCommand(AbstractCommand):
    def execute(self):
        print('--benchmark')

class HelpCommand(AbstractCommand):
    def execute(self):
        print('--help')

command = None

if len(sys.argv) <= 1:
    command = HelpCommand()
    command.execute()
    sys.exit(0)

command = None

match sys.argv[1]:
    case '--help':
        command = HelpCommand()
    case '--benchmark':
        command = BenchmarkCommand()
    case _:
        command = HelpCommand()

command.execute()

sys.exit(0)
