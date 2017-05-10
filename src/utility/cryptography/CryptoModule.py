from src.utility.metaclasses.MetaSingleton import MetaSingleton
from src.utility.settings.GlobalSettings import GlobalSettings

class CryptoModule(metaclass=MetaSingleton):
    algo = False
    def __init__(self):
        import src.utility.cryptography.Des as Des
        import src.utility.cryptography.TDes as TDes

        set = GlobalSettings().getSetting("algorithm")
        keys = set.get("keys").split(set.get("delimeter"))
        self.algo = eval(set.get("name"))(keys)

    def encrypt(self, msg) -> str:
        return self.algo.encrypt(msg)

    def decrypt(self, msg) -> str:
        return self.algo.decrypt(msg)
