
class Port:
    
    __slots__=['__nport', '__state', '__tProtocol', '__service']
  
    def __init__(self, nport):
        self.__nport = nport
        self.__state = ""
        
        self.__tProtocol = {'tcp': False, 'udp': False}

    def setNPort(self, port):
        self.__nport = port

    def getNPort(self):
        return self.__nport

    def setState(self, state):
        self.__state = state

    def getState(self):
        return self.__state
 
    def getService(self):
        return self.__service

    def setService(self, name):
        self.__service = Service(name)

    def getServiceVersion(self):
        return self.__service.getVersion()

    def setServiceVersion(self, version):
        self.__service.setVersion(version)
    
    def setProtocol(self, protocol):
        if protocol == "tcp":
            self.__tProtocol['tcp'] = True
        elif protocol == "udp":
            self.__tProtocol['udp'] = True
    
    def getProtocol(self):
        p_list = []
        
        if self.__tProtocol['tcp']:
            p_list.append("TCP")
        if self.__tProtocol['udp']:
            p_list.append("UDP")
            
        return p_list
    
    def isTCP(self):
        return self.__tProtocol['tcp']

    def isUDP(self):
        return self.__tProtocol['udp']

    def toStr(self):
        return "Port " + str(self.__nport) + ": " + self.__state

    def __str__(self):
        return str(self.__nport)
    
    def __int__(self):
        return self.__nport

