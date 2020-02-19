
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

# Extra fields: "8080.http.get.body","80.http.get.body","443.http.get.body"

write_keys = True

with open('data.csv', 'w') as csv_file:
  with open('jsontext.txt', 'w') as f:
    json_list = list(c.search("tags.raw:iot", max_records=1000,fields=["location.country","ip","location.city","country.code","protocols","location.longitude","location.latitude","signature.self_signed","autonomous_system.name",]))
    json_list.sort(key=lambda j: len(j), reverse=True) # Should sort the list so that the json object with the most keys is on the top
    key_object = json_list[0] # Keep the first json object to have a list of keys

    # Write keys from the json object with the most keys as attributes in the spreadsheet
    for key in key_object:
      csv_file.write(key + ',')
    csv_file.write("\n")

    for result in json_list: # result is a json object
      # Handle missing json keys too
      print(result)
      json.dump(result, f)
      f.write("\n")

      if "protocols" in result:
        protocols = result["protocols"] # Get list of protocols to iterate over

        for protocol in protocols: # Create a row for each protocol
          for key in key_object:
            if key in result:
              if key == "protocols":
                csv_file.write(str(protocol))
              else:
                csv_file.write(str(result[key]).replace(',', ' '))
            else:
              csv_file.write('')
            csv_file.write(',')
          csv_file.write("\n")

      else:
        for key in key_object:
          if key in result:
            csv_file.write(str(result[key]).replace(',', ' '))
          else:
            csv_file.write('')

          csv_file.write(',')
        csv_file.write("\n")











