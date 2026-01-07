from src.Configuration.Configuration import Configuration
from src.Service.AdapterResolveService import AdapterResolveService

class SignatureCommandHandler:
    def __call__(self):
        vendorAdapter = (AdapterResolveService()).getSignatureVendorAdapter(Configuration.getSignatureVendor())
        vendorAdapter.fullCycleSign()