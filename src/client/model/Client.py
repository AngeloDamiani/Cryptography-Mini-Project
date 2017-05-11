import socket
import threading

from ..utility.cryptography import CryptoModule
from . import Chatprotocol


class Client:
    def __init__(self, usr:str, port_tx: int, port_rcv: int, ui : "src.client.view.Ui"):

        #TODO Configurazione su file
        #TODO Splitting cartelle client e server

        self.serverip = "127.0.1.1"
        self.serverport = 9999

        ###

        self.rcvport = port_rcv
        self.txort = port_tx

        self.gui = ui
        self._end = True

        self.portrcvaddress=port_rcv


        MY_IP = socket.gethostbyname(socket.gethostname())
        self.name = usr[:32]
        self.rcvsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rcvsocket.bind((MY_IP, port_rcv))

        self.txsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.txsocket.bind((MY_IP, port_tx))
        self.sendMessage("","")

        self.quitsequence = CryptoModule().encrypt(self.name+"quit")
    def start(self):

        self._end = False
        rcvingmessagethread = threading.Thread(target=self._handleIncomingMessage, args=())
        rcvingmessagethread.start()

        self.gui.start(self)


    def sendMessage(self, message: str, dstuser: str):

        srcuser = CryptoModule().encrypt(self._nameFormat(self.name))
        dstuser = CryptoModule().encrypt(self._nameFormat(dstuser))
        message = CryptoModule().encrypt(message)
        msg = srcuser + dstuser + message

        portaddress = ("00000"+str(self.portrcvaddress))
        portaddress = portaddress[len(portaddress)-Chatprotocol.LENGTHPORT:]

        msg = portaddress + msg


        msg = msg.encode("utf-8")

        self.txsocket.sendto(msg,(self.serverip, self.serverport))

    def _handleIncomingMessage(self):

        while not self._end:
            data, user = self.rcvsocket.recvfrom(Chatprotocol.DATABYTES)
            if data:
                arrdata = data.decode("utf-8")
                if not (arrdata == self.quitsequence):
                    crypsrc = arrdata[:Chatprotocol.LENGTHNAME]
                    crypdata = arrdata[Chatprotocol.LENGTHNAME:]
                    srcname = "".join((CryptoModule().decrypt(crypsrc)).split(" "))
                    message = CryptoModule().decrypt(crypdata)
                    self.gui.printChat(message,srcname)

    def _nameFormat(self, name):
        return ("                                "+name)[-Chatprotocol.LENGTHNAME:]

    def stop(self):
        self._end = True

        self.txsocket.sendto(self.quitsequence.encode("utf-8"), (socket.gethostbyname(socket.gethostname()), self.rcvport))

        self.rcvsocket.close()
        self.txsocket.close()

from ..view.Ui import Ui as Ui