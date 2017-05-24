class Chatprotocol:
    DATABYTES = 4096
    LENGTHNAME = 32
    LENGTHPORT = 5
    LOGINSTRING = ""


    ## MESSAGE FORMAT ##

    # TX
    #    source_rcv_port|srcuser|dstuser|msg   #

    # RCVD
    #    srcuser|data
    #
    #
    #
    ## EXECUTION ##
    #
    # python3 mainclient.py Username portrcv porttx
    # python3 mainserver.py


    @staticmethod
    def formattingUser(string):
        dif = Chatprotocol.LENGTHNAME - len(string)
        for i in range (dif):
            string = " "+string
        return string

    @staticmethod
    def unformatUser(string):
        return string.strip(" ")


    @staticmethod
    def formattingPort(portno : int):
        strport = str(portno)
        dif = Chatprotocol.LENGTHPORT - len(strport)
        for i in range (dif):
            strport = "0"+strport
        return strport

    @staticmethod
    def unformatPort(string):
        return int(string)
