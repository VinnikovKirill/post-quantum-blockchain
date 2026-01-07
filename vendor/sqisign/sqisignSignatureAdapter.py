from src.VendorAdapter.VendorAdapterSignInterface import VendorAdapterSignInterface
from src.Event.EventEmitterInterface import EventEmitterInterface
from src.Service.ExportResolveService import ExportResolveService

class SqisignSignatureAdapter(VendorAdapterSignInterface, EventEmitterInterface):
    def fullCycleSign(self):
        self.attach((ExportResolveService()).getExportInterface())
        self.notify('print', 'SqisignSignatureAdapter')