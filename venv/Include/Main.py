
import sys
import json
import censys.ipv4
from JSONSlicers import JSONSlicers
from Model.Protocol import Protocol
from Model.Host import Host


API_URL = "https://censys.io/api/v1"
UID = ""
SECRET = ""
hostIPS = []
hostDetailed = []

foundPorts = []
hosts = []

slicer = JSONSlicers()

c = censys.ipv4.CensysIPv4(api_id=UID, api_secret=SECRET)

for result in c.search("autonomous_system.asn:15169 AND tags.raw:iot", max_records=3):

  #   print(result["ip"])
     hostIPS.append(result["ip"]);

for details in c.view(host):
    # data = json.dumps(details, separators=(":",','))
    # dataform = str(details).strip("'<>() ").replace('\'', '\"')
    # struct = json.loads(dataform)
    data = json.loads(details)
    print(data)

#        with open("currentHost.json", "w") as write_file:
#               json.dump(c.view(host), write_file)
# with open('currentHost.json') as json_file:
#        data = json.load(json_file)
#        numProtocols = len(data["protocols"])


#        foundProtocols = slicer.protocolSeperator(data["protocols"], numProtocols)

#       foundProducts = slicer.bannerGrab(foundProtocols, numProtocols, data)
#       geoLocation = slicer.geoGrab(data)
#       ip = data["ip"]

#      host = Host(ip,geoLocation,foundProducts,foundProtocols)
#      hosts.append(host)

# for details in hostDetailed:
#     test = json.loads(details)
# print(test)




