class Protocol:


    def __init__(self, protocolName, port):
         self.protocolName = protocolName
         self.port = port

    def setPort(self, port):
        self.port = port

    def setProtocol(self,protocolName):
        self.protocolName = protocolName

    def getPort(self):
        return self.port

    def getProtocol(self):
        return self.protocolName
