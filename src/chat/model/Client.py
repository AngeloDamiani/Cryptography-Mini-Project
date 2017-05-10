import socket
import threading


from src.chat.model.ChatProtocol import Chatprotocol


class Client:
    def __init__(self, usr:str, port_tx: int, port_rcv: int, ui : "src.chat.view.ui.Ui"):

        #TODO Configurazione su file

        self.serverip = "127.0.1.1"
        self.serverport = 9999

        ###

        self.rcvport = port_rcv
        self.txort = port_tx

        self.gui = ui
        self._end = True

        self.portrcvaddress=port_rcv


        MY_IP = socket.gethostbyname(socket.gethostname())
        self.name = usr
        self.rcvsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rcvsocket.bind((MY_IP, port_rcv))

        self.txsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.txsocket.bind((MY_IP, port_tx))
        self.sendMessage("","")


    def start(self):

        self._end = False
        rcvingmessagethread = threading.Thread(target=self._handleIncomingMessage, args=())
        rcvingmessagethread.start()

        self.gui.start(self)


    def sendMessage(self, message: str, dstuser: str):
        msg = str(self.portrcvaddress) + Chatprotocol.SEPSTRING + self.name + Chatprotocol.SEPSTRING + dstuser + Chatprotocol.SEPSTRING + message
        msg = msg.encode("utf-8")
        self.txsocket.sendto(msg,(self.serverip, self.serverport))

    def _handleIncomingMessage(self):

        while not self._end:
            data, user = self.rcvsocket.recvfrom(Chatprotocol.DATABYTES)
            if data:
                arrdata = data.decode("utf-8")
                if not (arrdata == Chatprotocol.CLOSE_SEQUENCE):
                    arrdata = arrdata.split(Chatprotocol.SEPSTRING)
                    srcname = arrdata[0]
                    message = arrdata[1]
                    self.gui.printChat(message,srcname)

    def stop(self):
        self._end = True

        self.txsocket.sendto(Chatprotocol.CLOSE_SEQUENCE.encode("utf-8"), (socket.gethostbyname(socket.gethostname()), self.rcvport))

        self.rcvsocket.close()

        self.txsocket.close()


import src.chat.view.ui