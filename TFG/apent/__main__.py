from Core import Core
from utils.Network import Network

def main():
    mainCore = Core();
    
    print "Initializing the penetration test..."
    print "Phase 1: Mapping the network."
    mainCore.mapInternalNetwork()
    print "\nPorts State."
    mainCore.mapNetworkHosts()
    
    
if __name__ == "__main__":
    main()
   
