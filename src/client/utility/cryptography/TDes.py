from .. import AsciiConverter as AC
from . import ICrypto


class TDes(ICrypto):

    def __init__(self, keys: list):
        ac = AC()

        from . import Des

        self.d1 = Des(keys[0])
        self.d2 = Des(keys[1])
        self.d3 = Des(keys[2])

    def encrypt(self, msg : str) -> str:
        return self.d3.encrypt(self.d2.decrypt(self.d1.encrypt(msg)))

    def decrypt(self, msg : str) -> str:
        return self.d1.decrypt(self.d2.encrypt(self.d3.decrypt(msg)))


