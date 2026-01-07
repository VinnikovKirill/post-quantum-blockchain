from src.VendorAdapter.VendorAdapterBenchmarkInterface import VendorAdapterBenchmarkInterface
from src.Event.EventEmitterInterface import EventEmitterInterface
from src.Service.ExportResolveService import ExportResolveService

class SqisignBenchmarkAdapter(VendorAdapterBenchmarkInterface, EventEmitterInterface):
    def benchmark(self):
        self.attach((ExportResolveService()).getExportInterface())
        self.notify('print', 'SqisignBenchmarkAdapter')