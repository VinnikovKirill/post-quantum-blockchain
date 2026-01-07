from src.Export.ExportInterface import ExportInterface
from src.Export.ConsoleExport import ConsoleExport

class ExportResolveService:
    def getExportInterface(self) -> ExportInterface:
        return ConsoleExport()