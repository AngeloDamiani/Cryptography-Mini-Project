from ..settings import GlobalSettings

from ..metaclasses import MetaSingleton


class CryptoModule(metaclass=MetaSingleton):
    algo = False
    def __init__(self):
        set = GlobalSettings().getSetting("algorithm")
        keys = set.get("keys").split(set.get("delimeter"))
        self.algo = eval(set.get("name"))(keys)

    def encrypt(self, msg) -> str:
        return self.algo.encrypt(msg)

    def decrypt(self, msg) -> str:
        return self.algo.decrypt(msg)
