from config.config import config

class Configuration():
    @staticmethod
    def get(configType: str, optionTitle: str) -> str:
        return config.get(configType, {}).get(optionTitle, {})
    
    @staticmethod
    def getSignatureVendor() -> str:
        return Configuration.get("signature", "vendor")
    
    @staticmethod
    def getBenchmarkVendor() -> str:
        return Configuration.get("benchmark", "vendor")