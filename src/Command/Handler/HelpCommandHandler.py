from src.Service.ExportResolveService import ExportResolveService

class HelpCommandHandler:
    HELP_COMMAND_CONTENT = "Available commands:\n--help : Display available commands\n--signature : Run signature interface using signature config\n--benchmark : Run benchmark interface using benchmark config\n"

    def __call__(self):
        (ExportResolveService()).getExportInterface().export(self.HELP_COMMAND_CONTENT)