class RsaServerProtocol:
    REGISTERINSTR = "+"
    REMOVEINSTR = "-"
    ASKINSTR = "?"
    KEYLENGTH = 1024
    NAMELENGTH = 32

    @staticmethod
    def formattingUser(string):
        dif = RsaServerProtocol.NAMELENGTH - len(string)
        for i in range (dif):
            string = " "+string
        return string

    @staticmethod
    def formattingKey(string):
        dif = RsaServerProtocol.KEYLENGTH - len(string)
        for i in range (dif):
            string = " "+string
        return string

    @staticmethod
    def unformatKey(string):
        return int(string)