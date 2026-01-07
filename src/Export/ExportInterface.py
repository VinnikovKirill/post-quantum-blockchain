from abc import ABC, abstractmethod

class ExportInterface(ABC):
    @abstractmethod
    def export(data: any = None) -> any:
        pass