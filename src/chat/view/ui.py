import abc

class Ui(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def start(self, user : "src.chat.model.client"):
        pass
