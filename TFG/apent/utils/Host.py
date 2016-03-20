
class Host:
    __slots__=['__addr', '__os', '__portsList']
    
    def __init__(self, addr):
        self.__addr = addr        
        self.__portsList = []
    
    def getAddr(self):
        return self.__addr

    def setAddr(self, addr):
        self.__addr = addr

    def setPortsList(self, portsList):
        for port in portsList:
            self.__portsList.append(Port(port))

