from .AbstractCommand import AbstractCommand
from src.Command.Handler.SignatureCommandHandler import SignatureCommandHandler

class SignatureCommand(AbstractCommand):
    def execute(self):
        (SignatureCommandHandler())()