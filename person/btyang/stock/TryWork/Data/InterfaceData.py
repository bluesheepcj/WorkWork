from abc import ABCMeta, abstractmethod

class InterfaceData(metaclass=ABCMeta):
    @abstractmethod
    def GetData(self): pass