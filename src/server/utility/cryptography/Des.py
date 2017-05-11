from .. import AsciiConverter as AC
from .ICrypto import ICrypto


class Des(ICrypto):

    KEYLENGTH = 64
    MSGLENGTH = 64

    IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17,  9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
    IP1 = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
           38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
           36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
           34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
    EP = [32, 1, 2, 3, 4, 5, 4,	5, 6, 7, 8,	9,
          8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
          16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
          24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    KP = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
          10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
          63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
          14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    SBOX = [
                [
                    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
                ],
                [
                    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
                ],
                [
                    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
                ],
                [
                    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
                ],
                [
                    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
                ],
                [
                    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
                ],
                [
                    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
                ],
                [
                    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
                ]
            ]
    CP = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
          2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

    CKP = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
           23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

    def __init__(self, key : str):
        ac = AC()

        if not len(key)>=8:
            key = key+"        "

        self.key = ac.tobits(key[0:8])

    def decrypt(self, msg : str) -> str:
        return self.encryptDecrypt(msg, encrypt = False)
    
    def encrypt(self, msg) -> str:
        return self.encryptDecrypt(msg, encrypt = True)    

    def encryptDecrypt(self, msg : str, encrypt = True) -> str:

        charstep = int(self.MSGLENGTH/ AC.charBitLength)
        messageArray = self._splitMessage(msg,charstep)

        finalString = ""
        ac = AC()

        for submsg in messageArray:

            # In case of messages not multiples of 64 bits
            if len(submsg) < charstep:
                for i in range (0, charstep-len(submsg)):
                    submsg = submsg+" "


            # In this moment we have a list of bits (Ascii to bit) of the submsg
            subbits = ac.tobits(submsg)

            # Initial permutation for the submsg (list of bits)
            result = self._initialPermutation(subbits)

            # Generation of all the keys
            if encrypt:
                K = self._kArrayGeneration()
            else:
                K = self._kArrayGeneration()[::-1]

            # Division in R and L (list of bits)
            L = result[0:int(len(result)/ 2)]
            R = result[int(len(result)/ 2):]

            for i in range (16):

                # Expansion of R (list of bits)
                f = self._xor(self._RExpansion(R), K[i])

                # Splitting of 6 bits for element
                split = self._splitBits(f, 6)

                # Application of s-boxes
                f = self._sBoxesApplications(split)

                # Concatenation after SBoxes
                temp = []
                for j in f:
                    temp = temp + j
                f = temp

                f = self._PPermutation(f)

                Li = R
                R = self._xor(f,L)
                L = Li

            temp = L
            L = R
            R = temp

            result = L+R
            result = self._finalPermutation(result)

            finalsubtext = ac.frombits(result)

            finalString = finalString + finalsubtext

        return finalString

    def _kArrayGeneration(self) -> list:
        K = []

        # Cycle Permutation of k
        k = self._keyPermutation(self.key)

        shiftrounds = {1:1, 2:1, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:1, 10:2, 11:2, 12:2, 13:2, 14:2, 15:2, 16:1}
        for i in range(16):
            k = self._shift(k,shiftrounds[i+1])
            K.append(self._cycleKeyPermutation(k))

        return K

    def _shift(self, k : list, shift : int) -> list:

        c0 = k[0:int(len(k) / 2)]
        d0 = k[int(len(k) / 2):]

        c1 = c0
        d1 = d0

        for i in range(shift):
            c1.append(c1.pop(0))
            d1.append(d1.pop(0))

        return c1+d1

    def _sBoxesApplications(self, Bs : list) -> list:
        arraybit = []
        NUMSBOX = 8
        for i in range(NUMSBOX):
            arraybit.append(self._singleSBoxApplication(Bs[i],i))
        return arraybit

    def _singleSBoxApplication(self, bits, sbox : int) -> list:
        SBOXBIT = 4
        row = int("".join(str(x) for x in bits[0:2]), 2)
        col = int("".join(str(x) for x in bits[2:]), 2)
        arr = [int(x) for x in bin(self.SBOX[sbox][row][col])[2:]]

        b = []
        if 4-len(arr)>0:
            for i in range (4-len(arr)):
                b = b+[0]
        return b+arr

    def _splitBits(self, bitsarray : list, bitsplitting : int) -> list:
        arraybit = []

        for i in range(0, len(bitsarray), bitsplitting):
            if not (i+bitsplitting>len(bitsarray)):
                arraybit.append(bitsarray[i : i+bitsplitting])
            else:
                arraybit.append(bitsarray[i : len(bitsplitting)])
        return arraybit

    def _splitMessage(self, msg : str, charstep : int) -> list:
        arrmessages = []

        for i in range(0, len(msg), charstep):
            if not (i+charstep>len(msg)):
                arrmessages.append(msg[i : i+charstep])
            else:
                arrmessages.append(msg[i : len(msg)])

        return arrmessages

    def _xor(self, a : list, b : list) -> list:
        arraybit = []

        for i in range (len(a)):
            arraybit.append(int(bool(a[i]) != bool(b[i])))

        return arraybit

    def _permutation(self, input: list, table) -> list:
        arraybit = []

        for i in table:
            # -1 Because the permutations are defined from 1 to n
            # but array index are defined from 0 to n-1
            arraybit.append(input[i - 1])

        return arraybit

    def _initialPermutation(self, bits) -> list:
        return self._permutation(bits, self.IP)

    def _finalPermutation(self, bits: list) -> list:
        return self._permutation(bits, self.IP1)

    def _cycleKeyPermutation(self, k: list) -> list:
        return self._permutation(k, self.CKP)

    def _PPermutation(self, bits):
        return self._permutation(bits, self.CP)

    def _keyPermutation(self, k : list) -> list:
        return self._permutation(k, self.KP)
    
    def _RExpansion(self, R : list):
        return self._permutation(R, self.EP)
