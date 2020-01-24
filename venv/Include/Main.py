
import sys
import json
import censys.ipv4


API_URL = "https://censys.io/api/v1"
UID = ""
SECRET = ""
hostIPS = []
hostDetailed = []

c = censys.ipv4.CensysIPv4(api_id=UID, api_secret=SECRET)

for result in c.search("autonomous_system.asn:15169 AND tags.raw:iot", max_records=3):

  #   print(result["ip"])
     hostIPS.append(result["ip"]);



#print (len(hostIPS))
for host in hostIPS:
        for result in c.view(host):
        # print(result)

         hostDetailed.append(result)
#print(hostDetailed["protocols"])

#print(hostDetailed[1])


for details in hostDetailed:
     test = json.loads(hostDetailed[1])


#print(len(test))
print(test)
