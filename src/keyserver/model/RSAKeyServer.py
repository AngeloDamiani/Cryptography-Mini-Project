import socket


from . import RsaServerProtocol


class RSAKeyServer:
    KEYMAXLENGTH = 1024
    MAXUSERNAME = 32
    INSTRUCTIONLENGTH = 1
    def __init__(self):
        ## TODO CONF SU FILE

        PORT_RCV = 50001
        PORT_TX = 50000

        MY_IP = socket.gethostbyname(socket.gethostname())
        print(MY_IP)

        self.clientsKeys = dict()

        self.rcvsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rcvsocket.bind((MY_IP, PORT_RCV))

        self.txsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.txsocket.bind((MY_IP, PORT_TX))


    def start(self):


        print("###########################################")

        while True:
            # 2 is because I suppose 1024 bytes for RSA's "e" and 1024 for RSA's "n"
            data, user = self.rcvsocket.recvfrom(2*self.KEYMAXLENGTH + self.MAXUSERNAME + self.INSTRUCTIONLENGTH)
            if data:

                arrdata = data.decode("utf-8")
                instr = arrdata[:self.INSTRUCTIONLENGTH]

                if instr == RsaServerProtocol.REGISTERINSTR:
                    user = arrdata[self.INSTRUCTIONLENGTH:self.MAXUSERNAME+self.INSTRUCTIONLENGTH].strip(" ")
                    e = RsaServerProtocol.unformatKey(arrdata[self.INSTRUCTIONLENGTH + self.MAXUSERNAME : self.INSTRUCTIONLENGTH + self.KEYMAXLENGTH + self.MAXUSERNAME])
                    n = RsaServerProtocol.unformatKey(arrdata[self.INSTRUCTIONLENGTH + self.KEYMAXLENGTH + self.MAXUSERNAME:])
                    key = (e, n)

                    self.register(user,key)

                elif instr == RsaServerProtocol.REMOVEINSTR:
                    user = arrdata[self.INSTRUCTIONLENGTH:self.MAXUSERNAME+self.INSTRUCTIONLENGTH].strip(" ")

                    self.remove(user)

                elif instr == RsaServerProtocol.ASKINSTR:
                    target = arrdata[self.INSTRUCTIONLENGTH:self.MAXUSERNAME+self.INSTRUCTIONLENGTH].strip(" ")

                    self.answer(user, target)


    def register(self, user : str, key):
        self.clientsKeys[user] = key
        print("# Associated: "+user)
        print("# Public key: "+str(key))
        print("###########################################")

    def remove(self, user : str):
        self.clientsKeys.pop(user)

    def answer(self, user, trgt : str):
        if trgt in self.clientsKeys.keys():
            keyStr = RsaServerProtocol.formattingKey(str(self.clientsKeys[trgt][0]))+RsaServerProtocol.formattingKey(str(self.clientsKeys[trgt][1]))
            keyStr = keyStr.encode("utf-8")
            self.txsocket.sendto(keyStr, user)

