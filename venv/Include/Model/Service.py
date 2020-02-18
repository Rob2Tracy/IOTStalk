class Service:

    def __init__(self,product,productVersion,extra):
        self.product = product
        self.productVersion = product
        self.extra = extra

    def setProduct(self,product):
        self.product = product

    def setProdVersion(self,version):
        self.productVersion = version

    def setExtra(self,extra):
        self.extra = extra

    def getProduct(self):
        return self.product

    def getProdVersion(self):
        return self.productVersion

    def getExtra(self):
        return self.extra
