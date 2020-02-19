
import sys
import json
import censys.ipv4
from JSONSlicers import JSONSlicers
from Model.Protocol import Protocol
from Model.Host import Host
from Test import Test


API_URL = "https://censys.io/api/v1"

UID = ""
SECRET = ""

hostIPS = []
hostDetailed = []

foundPorts = []
hosts = []

slicer = JSONSlicers()

c = censys.ipv4.CensysIPv4(api_id=UID, api_secret=SECRET)
i=1
#for i in range(1,10001):

for result in c.search("tags.raw:iot", max_records=1000,fields=["location.country","ip","location.city","country.code","protocols","location.longitude","location.latitude","signature.self_signed","autonomous_system.name","8080.http.get.body","80.http.get.body","443.http.get.body"]):

     print(result)











