class Chatprotocol:
    DATABYTES = 4096
    SEPSTRING = "%-%"
    CLOSE_SEQUENCE = SEPSTRING+"quit"+SEPSTRING

    ## MESSAGE FORMAT ##

    # TX
    #    source_rcv_port%-%srcuser%-%dstuser%-%data   #

    # RCVD
    #    src%-%data
    #
    # CLOSE SEQUENCE
    #     %-%quit%-%
    #
    #
    ## EXECUTION ##
    #
    # python3 mainclient.py Username portrcv porttx
    # python3 mainserver.py
