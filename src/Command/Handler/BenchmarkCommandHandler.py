from src.Configuration.Configuration import Configuration
from src.Service.AdapterResolveService import AdapterResolveService

class BenchmarkCommandHandler:
    def __call__(self):
        vendorAdapter = (AdapterResolveService()).getBenchmarkVendorAdapter(Configuration.getBenchmarkVendor())
        vendorAdapter.benchmark()