from .metaclasses import MetaSingleton


class AsciiConverter(metaclass=MetaSingleton):
    charBitLength = 8

    def tobits(self, s: str):
        result = []
        for c in s:
            bits = bin(ord(c))[2:]
            bits = '00000000'[len(bits):] + bits
            result.extend([int(b) for b in bits])
        return result

    def frombits(self, bits):
        chars = []
        for b in range(int(len(bits) / 8)):
            byte = bits[b * 8:(b + 1) * 8]
            chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        return ''.join(chars)

    def bitsToInt(self, bits):
        return int(''.join(map(str, bits)), 2)

    def intToBits(self, num):
        bitsarray = [int(x) for x in bin(num)[2:]]
        padnum = self.charBitLength - (len(bitsarray) % self.charBitLength)
        padunit = [0]
        for i in range(padnum):
            bitsarray = padunit + bitsarray
        return bitsarray

    def strToInt(self, s: str):
        return self.bitsToInt(self.tobits(s))

    def intToStr(self, num: int):
        return self.frombits(self.intToBits(num))