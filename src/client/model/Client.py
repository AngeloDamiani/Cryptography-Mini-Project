import socket
import threading
import hashlib
import random
import string

from ..utility.cryptography import CryptoModule
from . import Chatprotocol


class Client:
    def __init__(self, usr:str, port_tx: int, port_rcv: int, ui : "src.client.view.Ui"):

        #TODO Configurazione su file
        #TODO Splitting cartelle client e server

        self.cryptomodule = CryptoModule(usr)

        self.serverip = "127.0.1.1"
        self.serverport = 9999

        ###

        self.rcvport = port_rcv
        self.txort = port_tx

        self.gui = ui
        self._end = True

        self.portrcvaddress=port_rcv


        MY_IP = socket.gethostbyname(socket.gethostname())
        self.name = usr[:Chatprotocol.LENGTHNAME]
        self.rcvsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rcvsocket.bind((MY_IP, port_rcv))

        self.txsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.txsocket.bind((MY_IP, port_tx))
        self.sendMessage(Chatprotocol.LOGINSTRING," ")


        quitstring = ''.join(random.choice(string.ascii_letters) for i in range(Chatprotocol.DATABYTES))
        self.quitsequence = hashlib.sha256(quitstring.encode()).hexdigest()


    def start(self):

        self._end = False
        rcvingmessagethread = threading.Thread(target=self._handleIncomingMessage, args=())
        rcvingmessagethread.start()

        self.gui.start(self)

    def sendMessage(self, message: str, dstuser: str):
        c = self.cryptomodule
        srcuser = Chatprotocol.formattingUser(self.name)
        dstuser = Chatprotocol.formattingUser(dstuser)
        message = c.encrypt(message, dstuser)
        msg = srcuser + dstuser + message

        portaddress = Chatprotocol.formattingPort(self.portrcvaddress)
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
                    src = arrdata[:Chatprotocol.LENGTHNAME]
                    crypdata = arrdata[Chatprotocol.LENGTHNAME:]
                    srcname = Chatprotocol.unformatUser(src)
                    message = self.cryptomodule.decrypt(crypdata)
                    self.gui.printChat(message,srcname)

    def stop(self):
        self._end = True

        self.txsocket.sendto(self.quitsequence.encode("utf-8"), (socket.gethostbyname(socket.gethostname()), self.rcvport))
        self.rcvsocket.close()
        self.txsocket.close()

from ..view.Ui import Ui as Ui