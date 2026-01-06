from config.config import config

class Configuration():
    @staticmethod
    def get(configType: str, optionTitle: str) -> str:
        return config.get(configType, {}).get(optionTitle, {})
    
    @staticmethod
    def getVendor() -> str:
        return Configuration.get("signature", "vendor")