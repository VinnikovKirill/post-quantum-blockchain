import os
import importlib
import sys

from vendor import VENDOR_DIR
from src.VendorAdapter.VendorAdapterSignInterface import VendorAdapterSignInterface
from src.VendorAdapter.VendorAdapterBenchmarkInterface import VendorAdapterBenchmarkInterface

class AdapterResolveService:
    def getSignatureVendorAdapter(self, adapterTitle: str) -> VendorAdapterSignInterface | None:
        moduleTitle = f"{adapterTitle}SignatureAdapter"

        adapterClassInstance = self.getVendorAdapterModuleClassInstance(adapterTitle, moduleTitle)

        if not isinstance(adapterClassInstance, VendorAdapterSignInterface):
            return None

        return adapterClassInstance

    def getBenchmarkVendorAdapter(self, adapterTitle: str):
        moduleTitle = f"{adapterTitle}BenchmarkAdapter"

        adapterClassInstance = self.getVendorAdapterModuleClassInstance(adapterTitle, moduleTitle)

        if not isinstance(adapterClassInstance, VendorAdapterBenchmarkInterface):
            return None

        return adapterClassInstance

    def getVendorAdapterModuleClassInstance(self, adapterTitle: str, moduleTitle: str) -> any:
        moduleImport = f"vendor.{adapterTitle}.{moduleTitle}"
        adapterPath = f"{VENDOR_DIR}{os.sep}{adapterTitle}{os.sep}{moduleTitle}.py"

        if adapterPath not in sys.path:
            sys.path.insert(0, adapterPath)

        module = importlib.import_module(moduleImport)
        adapterClass = getattr(module, moduleTitle[0].upper() + moduleTitle[1:])

        return adapterClass()