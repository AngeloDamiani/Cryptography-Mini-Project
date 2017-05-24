import socket

from ..settings import GlobalSettings

from . import Des
from . import TDes
from .rsa import Rsa

class CryptoModule:

    def __init__(self, user : str):
        self.usr = user

        gs = GlobalSettings()

        self.algoname = gs.getSetting("algorithm")

        self.algo = False
        self.dstkeys = {}

        set = gs.getSetting(self.algoname)

        if self.algoname == "algorithmDES":
            keys = set.get("key")
            self.algo = eval(set.get("class"))(keys)

        elif self.algoname == "algorithmTDES":
            key1 = set.get("key1")
            key2 = set.get("key2")
            key3 = set.get("key3")
            keys = [key1,key2,key3]
            self.algo = eval(set.get("class"))(keys)

        elif self.algoname == "algorithmRSA":
            key1 = set.get("key1")
            key2 = set.get("key2")
            keys = [key1,key2]
            self.algo = eval(set.get("class"))()
            self.algo.generateKeys(key1,key2)
            publicKeys = self.algo.getPublicKeys()
            self.registerRSAKey(publicKeys, user)

    def encrypt(self, msg : str, dst : str) -> str:
        from .rsa import Rsa
        if msg:
            if self.algoname == "algorithmRSA":
                if dst in self.dstkeys:
                    k = self.dstkeys[dst]
                else:
                    k = self.retrieveRSAKey(dst)
                rsa = Rsa()
                rsa.setPublicKeys(k)
                return rsa.encrypt(msg)

            return self.algo.encrypt(msg)
        else: return msg

    def decrypt(self, msg : str) -> str:
        return self.algo.decrypt(msg)

    def retrieveRSAKey(self, dst : str):
        from .rsa import RsaServerProtocol as RSP

        set = GlobalSettings().getSetting("algorithmRSA")
        PORT_TX = set.get("myport")

        MY_IP = socket.gethostbyname(socket.gethostname())
        SERVER_IP = set.get("keyserver")
        SERVER_PORT = set.get("serverport")

        mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mysocket.bind((MY_IP, PORT_TX))

        msg = (RSP.ASKINSTR+RSP.formattingUser(dst)).encode("utf-8")

        mysocket.sendto(msg, (SERVER_IP,SERVER_PORT))

        data, user = mysocket.recvfrom(RSP.KEYLENGTH*2)

        arrdata = data.decode("utf-8")
        e = RSP.unformatKey(arrdata[:RSP.KEYLENGTH])
        n = RSP.unformatKey(arrdata[RSP.KEYLENGTH:])
        k = (e,n)

        self.dstkeys[dst] = k

        mysocket.close()

        return k



    def registerRSAKey(self, keys, name : str):
        from .rsa import RsaServerProtocol as RSP

        set = GlobalSettings().getSetting("algorithmRSA")
        MYPORT = set.get("myport")

        MY_IP = socket.gethostbyname(socket.gethostname())
        SERVER_IP = set.get("keyserver")
        SERVER_PORT = set.get("serverport")

        #rcvsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #rcvsocket.bind((MY_IP, PORT_RCV))

        mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mysocket.bind((MY_IP, MYPORT))

        msg = RSP.REGISTERINSTR+RSP.formattingUser(name)+RSP.formattingKey(str(keys[0]))+RSP.formattingKey(str(keys[1]))
        msg = msg.encode("utf-8")
        mysocket.sendto(msg, (SERVER_IP,SERVER_PORT))

        mysocket.close()



