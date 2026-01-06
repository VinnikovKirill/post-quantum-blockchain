from .AbstractCommand import AbstractCommand
from src.Configuration.Configuration import Configuration

class SignatureCommand(AbstractCommand):
    def execute(self):
        print('--signature')
        print(Configuration.getVendor())