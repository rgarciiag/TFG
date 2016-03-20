
class Service:
    
    __slots__=['__name', '__version', '__description']
    
    def __init__(self, name):
        self.__name = name

    def setAttr(self, name, version):
        self.__name = name
        self.__version = version

    def setVersion(self, version):
        self.__version = version
    
    def getVersion(self):
        return self.__version

    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name
