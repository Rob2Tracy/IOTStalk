from Model.Protocol import Protocol
from Model.Service import Service
from Model.Geolocation import Geolocation
from Model.SpecialityProtocols.Redis import Redis
class JSONSlicers:










   def protocolSeperator(self,protocols,num):
    protocolsFound = []   # Protocol port # odds, Protocol name # evens

    i=0
    for p in protocols:


     for sub in range(0,len(p.split('/')) - 1):
             #  protocol = Protocol(p.split('/')[sub])
               fPort = p.split('/')[sub]

               sub+=1
               fProto = p.split('/')[sub]
               #protocol = Protocol(p.split('/')[sub])
               protocol = Protocol(fProto,fPort)
               protocolsFound.append(protocol)

    #print(protocolsFound[0].getPort())

    return protocolsFound

   def bannerGrab(self,protocols,num,data):

       foundProducts = []

       for protocol in protocols:


           banner = data[protocol.getPort()][protocol.getProtocol()]["banner"]

           if(protocol.getProtocol() == "amqp"):
               version =str(banner["version"]["major"])+"." + str(banner["version"]["minor"]) +"." +str(banner["version"]["revision"])
               service = Service("amqp",version,"NULL")
               foundProducts.append(service)

           elif(protocol.getProtocol() == "redis"):
               redis = Redis(banner["NULL","info_response"])
               foundProducts.append(redis)

           elif(protocol.getProtocol() == "mqtt"):
               pass


           elif(protocol.getProtocol() == "ssh"):
               subDirect = data[protocol.getPort()][protocol.getProtocol()]
               metadata = data[protocol.getPort()][protocol.getProtocol()][subDirect]["metadata"]

               product = metadata["product"]
               version = metadata["version"]

               service = Service(product,version,"NULL")
               foundProducts.append(service)

           elif(protocol.getProtocol() == "banner"):
               if(protocol.getPort() == "22"):
                   version = "NULL"
                   protocol.setProtocol("ssh")
                   extra = data[protocol.getPort()]["banner"]["banner_decoded"]
                   service = Service("ssh",version,extra)
                   foundProducts.append(service)
           else:
               print("add " + protocol.getProtocol())

       return foundProducts

   def geoGrab(self,data):

       cCode = data["location"]["registered_country_code"]
       lat = data["location"]["latitude"]
       long = data["location"]["longitude"]
       country = data["location"]["registered_country"]

       try:
        province = data["location"]["province"]

       except KeyError as e:
        province = "NULL"

       geo = Geolocation(province,country,cCode,lat,long)

       return geo





