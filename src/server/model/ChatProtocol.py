class Chatprotocol:
    DATABYTES = 4096
    LENGTHNAME = 32
    LENGTHPORT = 5


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
