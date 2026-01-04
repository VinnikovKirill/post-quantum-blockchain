from .AbstractCommand import AbstractCommand

class DemoSignatureCommand(AbstractCommand):
    def execute(self):
        print('--demo-signature')