class Redis:

    product="redis"
    def __init__(self,productVersion,infoResponse):
        self.productVersion = productVersion
        self.infoResponse = infoResponse

    def setProdVersion(self,version):
        self.productVersion = version

    def setInfoResponse(self,response):
        self.infoResponse = response

    def getProdVersion(self):
        return self.productVersion

    def getInfoResponse(self):
        return self.infoResponse