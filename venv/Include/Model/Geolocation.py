class Geolocation:

    def __init__(self,province,country,countryCode,lat,long):
        self.province = province
        self.country = country
        self.countryCode = countryCode
        self.lat = lat
        self.long = long

    def setprovince(self,province):
        self.province = province

    def setCountry(self,country):
        self.country = country

    def setCountryCode(self,cCode):
        self.countryCode = cCode
    
    def setLat(self,lat):
        self.lat = lat
    
    def setLong(self,long):
        self.long = long

    def getprovince(self):
        return self.province

    def getCountry(self):
        return self.country

    def getCountryCode(self):
        return self.countryCode
    
    def getLat(self):
        return self.lat
    
    def getLong(self):
        return self.long