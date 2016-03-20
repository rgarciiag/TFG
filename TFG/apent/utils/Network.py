from Host import Host

class Network:
    __slots__=['__addr', '__addrHostsList', '__hostsDict']
    
    def __init__(self):
        self.__addrHostsList = []    
        self.__hostsDict = {}    
    
    def setAddr(self, addr):
        self.__addr = addr
    
    def setAddrHostsList(self, hostsList):
        self.__addrHostsList = hostsList
        
        for addr in self.__addrHostsList:
            self.__hostsDict[str(addr)] = Host(addr)

    def getAddrHostsList(self):
        return self.__addrHostsList

    def getHostByAddr(self, addr):
        return self.__hostsDict[str(addr)]
