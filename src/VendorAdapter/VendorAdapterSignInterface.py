from abc import ABC, abstractmethod

class VendorAdapterSignInterface(ABC):
    @abstractmethod
    def fullCycleSign(self) -> None:
        pass