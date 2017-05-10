import socket

class Server:
    def __init__(self):

        PORT_RCV = 9999
        PORT_TX = 9998
        MAX_USERS = 10
        MY_IP = socket.gethostbyname(socket.gethostname())

        self.clients = dict()

        self.rcvsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rcvsocket.bind((MY_IP, PORT_RCV))

        self.txsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.txsocket.bind((MY_IP, PORT_TX))

    def start(self):

        import src.chat.model.ChatProtocol as chatprotocol

        while True:
            data, user = self.rcvsocket.recvfrom(chatprotocol.DATABYTES)
            if data:
                arrdata = data.decode("utf-8").split(chatprotocol.SEPSTRING)
                srcport = arrdata[0]
                srcname = arrdata[1]
                dstname = arrdata[2]
                message = arrdata[3]

                if not (user in self.clients):
                    self._handleConnection(user,srcname, srcport)
                self._sendRcvdMessage(dstname, message, srcname)

    def _handleConnection(self, address: str, usrname: str, srcport: str):
        self.clients[usrname] = (address[0], int(srcport))

    def _sendRcvdMessage(self, dstuser: str, message: str, srcuser: str):
        import src.chat.model.ChatProtocol as chatprotocol
        if dstuser in self.clients:
            msg = srcuser+chatprotocol.SEPSTRING+message
            msg = msg.encode("utf-8")
            self.txsocket.sendto(msg, self.clients[dstuser])





