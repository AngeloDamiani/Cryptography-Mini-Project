import abc

class ICrypto(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def encrypt(self, msg : str) -> str:
        """
        Encrypt a message

        :return: an encrypted message
        """
        pass

    @abc.abstractmethod
    def decrypt(self, msg : str) -> str:
        """
        Decrypt a message

        :return: a decrypted message
        """
        pass
