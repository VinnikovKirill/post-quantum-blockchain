from .AbstractCommand import AbstractCommand

class BenchmarkCommand(AbstractCommand):
    def execute(self):
        print('--benchmark')