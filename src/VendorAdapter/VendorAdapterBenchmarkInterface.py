from abc import ABC, abstractmethod

class VendorAdapterBenchmarkInterface(ABC):
    @abstractmethod
    def benchmark(self) -> None:
        pass