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

        print("###########################################")

        import src.chat.model.ChatProtocol as chatprotocol

        while True:
            data, user = self.rcvsocket.recvfrom(chatprotocol.Chatprotocol.DATABYTES)
            if data:
                arrdata = data.decode("utf-8")

                lp = chatprotocol.Chatprotocol.LENGTHPORT
                ln = chatprotocol.Chatprotocol.LENGTHNAME
                srcport = arrdata[:lp]
                srcname = arrdata[lp:lp+ln]
                dstname = arrdata[lp+ln:lp+2*ln]
                message = arrdata[lp+2*ln:]

                print("SRC = "+srcname)
                print("DST = "+dstname)
                print("Message = \n"+message)
                print("###########################################")


                if not (user in self.clients):
                    self._handleConnection(user,srcname, srcport)
                self._sendRcvdMessage(dstname, message, srcname)

    def _handleConnection(self, address: str, usrname: str, srcport: str):
        self.clients[usrname] = (address[0], int(srcport))

    def _sendRcvdMessage(self, dstuser: str, message: str, srcuser: str):
        import src.chat.model.ChatProtocol as chatprotocol
        if dstuser in self.clients:
            msg = srcuser + message
            msg = msg.encode("utf-8")
            self.txsocket.sendto(msg, self.clients[dstuser])





