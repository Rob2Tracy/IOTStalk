class Host:

    def __init__(self,ip,geolocation,services,protocols):
        self.ip = ip
        self.geolocation = geolocation
        self.protocols = protocols

    def setIp(self,ip):
        self.ip = ip

    def setgeolocation(self,geo):
        self.geolocation = geo

    def setProtocols(self,protos):
        self.protocols = protos

    def getIP(self):
        return self.ip

    def getGeo(self):
        return self.geolocation

    def getProtocols(self):
        return self.protocols