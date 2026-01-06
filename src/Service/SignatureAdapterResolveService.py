import os
import importlib
import sys

from vendor import VENDOR_DIR
from src.VendorAdapter.VendorAdapterSignInterface import VendorAdapterSignInterface

class SignatureAdapterResolveService:
    def getSignatureVendorAdapter(self, adapterTitle: str) -> VendorAdapterSignInterface | None:
        moduleTitle = f"{adapterTitle}Adapter"
        moduleImport = f"vendor.{adapterTitle}.{moduleTitle}"
        adapterPath = f"{VENDOR_DIR}{os.sep}{adapterTitle}{os.sep}{moduleTitle}.py"

        if adapterPath not in sys.path:
            sys.path.insert(0, adapterPath)

        module = importlib.import_module(moduleImport)
        adapterClass = getattr(module, moduleTitle[0].upper() + moduleTitle[1:])

        adapterClassInstance = adapterClass()
        
        if not isinstance(adapterClassInstance, VendorAdapterSignInterface):
            return None

        return adapterClassInstance