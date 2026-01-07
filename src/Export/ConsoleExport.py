from src.Export.ExportInterface import ExportInterface
from src.Event.EventSubscriberInterface import EventSubscriberInterface

class ConsoleExport(ExportInterface, EventSubscriberInterface):
    def export(self, data: any = None) -> any:
        print(f"{str(data)}\n")

    def update(self, event: str, data: any) -> None:
        if event != 'print':
            return

        self.export(data)