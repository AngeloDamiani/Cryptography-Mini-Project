from .. import ICrypto
from math import gcd,log, ceil, floor
from ....utility.AsciiConverter import AsciiConverter as AC
import random

class Rsa(ICrypto):
    eMAXLENGTH = 1024
    nMAXLENGTH = 1024
    def __init__(self):
        pass

    def setPublicKeys(self, keys):
        self.e = keys[0]
        self.n = keys[1]

    def generateKeys(self, p : int, q : int):
        if (log(p*q,2)) > self.nMAXLENGTH:
            raise Exception('Key n too long')
        self.p = p,
        self.q = q
        self.n = p*q
        self.phin = (p-1)*(q-1)

        self.e = random.randint(1 + 1, self.phin - 1)
        if (log(self.e,2)) > self.eMAXLENGTH:
            raise Exception('Key e too long')
        while gcd(self.e,self.phin) != 1:
            self.e = random.randint(1 + 1, self.phin - 1)

        self.d = self._modinv(self.e, self.phin)

    def encrypt(self, msg : str):
        intmessage = AC().strToInt(msg)
        cipher = pow(intmessage,self.e,self.n)
        cipher = AC().intToStr(cipher)

        return cipher

    def decrypt(self, ciphered : str):

        ciphered = AC().strToInt(ciphered)
        m = pow(ciphered, self.d, self.n)
        message = AC().intToStr(m)

        return message

    def getPublicKeys(self):
        return (self.e,self.n)

    def _egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self._egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def _modinv(self, a, m):
        g, x, y = self._egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m
