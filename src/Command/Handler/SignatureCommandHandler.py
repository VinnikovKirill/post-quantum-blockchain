from src.Configuration.Configuration import Configuration
from src.Service.SignatureAdapterResolveService import SignatureAdapterResolveService

class SignatureCommandHandler:
    def __call__(self):
        vendorAdapter = (SignatureAdapterResolveService()).getSignatureVendorAdapter(Configuration.getVendor())
        vendorAdapter.fullCycleSign()