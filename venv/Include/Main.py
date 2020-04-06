
import sys
import json
import censys.ipv4
from JSONSlicers import JSONSlicers
from Model.Protocol import Protocol
from Model.Host import Host
from Test import Test

API_URL = "https://censys.io/api/v1"

#UID = "8b283696-e777-4291-a8c0-420896961798"
#SECRET = "z6mmLUY0nULUkKn7vji9m9rGIvQbHIgT"

UID = "a4e47672-8df9-4bd3-a935-7409ff4c333c"
SECRET = "jqL3H9ZhbGfTrqCGRSCqWdNJfXOunpzv"
hostIPS = []
hostDetailed = []

foundPorts = []
hosts = []

slicer = JSONSlicers()

def createCSV():

  c = censys.ipv4.CensysIPv4(api_id=UID, api_secret=SECRET)
  i=1
  #for i in range(1,10001):

  # Extra fields: "8080.http.get.body","80.http.get.body","443.http.get.body"

  flatten_protocols = False # True: Duplicate rows for each of a host's protocols. False: Single rows with only one protocol listed.
  write_keys = True

  with open('data.csv', 'w') as csv_file:
    with open('jsontext.txt', 'w') as f:
      json_list = list(c.search("tags.raw:iot", max_records=4000,fields=filters))
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

                  if str(result[key]) == "Telef�nica Celular de Bolivia S.A." or "Mikołów":
                  #  print(str(result[key]) + "\n")
                    pass


                  else:

                    csv_file.write(str(result[key]).replace(',', ' '))
              else:
                csv_file.write('')
              csv_file.write(',')
            csv_file.write("\n")
            if not flatten_protocols: # Exit loop to only print the first protocol if this is not set
              break
      

        else:
          for key in key_object:
            if key in result:
              csv_file.write(str(result[key]).replace(',', ' '))
            else:
              csv_file.write('')

            csv_file.write(',')
          csv_file.write("\n")

def run(count, tags, filters, filename):
  c = censys.ipv4.CensysIPv4(api_id=UID, api_secret=SECRET)

  with open('output.json', 'a') as f:

    json_list = list(c.search("tags.raw:"+tag, max_records=4000,fields=filtersThree,))
    for result in json_list: # result is a json object
  # Handle missing json keys too
       print(result)
       json.dump(result, f)
       f.write("\n")

  #for results in c.search("tags.raw:iot"):
    #hosts.append(results["ip"])

    #with open(filename, 'a') as f:


      #for ip in hosts:

       # resultOne = list(c.search(query=ip,fields=filters,max_records=5000))
       # resultTwo = list(c.search(query=ip,fields=filtersOne,))
       # resultThree = list(c.search(query=ip,fields=filtersTwo,))
       # resultFour = list(c.search(query=ip,fields=filtersThree,))
       # json.dump(resultOne,f)
       # f.write("\n")
       # json.dump(resultTwo,f)
       # f.write("\n")
       # json.dump(resultThree,f)
       # f.write("\n")
       # json.dump(resultFour,f)
       # f.write("\n")

 # with open(filename, 'w') as f:
 #   json_list = list(c.search("tags.raw:"+tag, max_records=count,fields=filters,))
 #   for result in json_list: # result is a json object
      # Handle missing json keys too
 #     print(result)
 #     json.dump(result, f)
 #     f.write("\n")


  pass



# for results in c.search("tags.raw:"):
#  hosts.append(results["ip"])

#with open(filename, 'a') as f:
#  for ip in hosts:
#    resultOne = list(c.search(query=ip,fields=filters,))
#    resultTwo = list(c.search(query=ip,fields=filtersOne,))
#    resultThree = list(c.search(query=ip,fields=filtersTwo,))
#    resultFour = list(c.search(query=ip,fields=filtersThree,))
#    json.dump(resultOne,f)
#    f.write("\n")
#    json.dump(resultTwo,f)
#    f.write("\n")
#    json.dump(resultThree,f)
#    f.write("\n")
#    json.dump(resultFour,f)
#    f.write("\n")





if __name__ == "__main__":
  count = 1
  tag = "iot"
  filters = ["location.country","ip","location.city","country.code","protocols","location.longitude","location.latitude","signature.self_signed","autonomous_system.name", ]

  filtersOne = ["ip","21.ftp.banner","21.ftp.metadata.product","21.ftp.metadata.version","23.telnet.banner.banner ", "3306.mysql.banner.server_version","3306.mysql.banner.capability_flags.MYSQL_OLD_PASSWORD ","3306.mysql.banner.capability_flags.CLIENT_SECURE_CONNECTION","3306.mysql.banner.capability_flags.CLIENT_LONG_PASSWORD ","3306.mysql.banner.capability_flags.CLIENT_SSL ", ]
  filtersTwo = ["ip","8883.mqtt.banner.connack.raw ","8883.mqtt.banner.tls.signature.valid ","8883.mqtt.banner.tls.version ", "8883.mqtt.banner.tls.certificate.parsed.signature.self_signed ","1883.mqtt.banner.connack.raw ","1883.mqtt.banner.tls.signature.valid ", "1883.mqtt.banner.tls.version ","1883.mqtt.banner.tls.certificate.parsed.signature.self_signed ","5672.amqp.banner.version.major"
                     ,"5672.amqp.banner.version.minor","5672.amqp.banner.version.revision",]
  #filtersThree = ["ip","443.https.get.title","443.https.get.status_code","443.https.get.metadata.product","443.https.get.metadata.version","443.https.get.body","8080.http.get.title","8080.http.get.status_code","8080.http.get.metadata.product","8080.http.get.metadata.version","8080.http.get.body","5672.amqp.version.major"
  #                   ,"5672.amqp.version.minor","5672.amqp.version.revision","80.http.get.title ","80.http.get.status_code","80.http.get.metadata.product","80.http.get.metadata.version","80.http.get.body",]
  outputFilename = "output.json"

  for a in sys.argv:
    print(a, end=" ")
  print("\n")

  length = len(sys.argv)
  if length == 1:
    print("Running the default query")
    print("Usage: Main.py [-c count] [-t tag] [-f filters] [-o output filename]")

  i = 1
  # Loop over arguments trying to modify the default values with command line arguments
  while i < length:
    if sys.argv[i] == "-c":
      if i+1 < length and str.isdigit(sys.argv[i+1]):
        count = int(sys.argv[i+1])
        i += 2
      else:
        sys.exit("Error: Count argument expects a number\n\n")

    elif sys.argv[i] == "-t":
      if i+1 < length:
        tag = sys.argv[i+1]
        i += 2
      else:
        sys.exit("Error: Tag argument expects a tag\n\n")

    elif sys.argv[i] == "-f":
      while i+1 < length and sys.argv[i+1][0] != '-':

        filters.append(sys.argv[i+1])
        i += 1

      if len(filters) == 0:
        sys.exit("Error: filter argument expects some filters\n\n")
      else:
        i += 1

    elif sys.argv[i] == "-o":
      print("Found -o at " + str(i))
      if i+1 < length:
        print("Found " + str(sys.argv[i+1]) + " at " + str(i+1))
        outputFilename = sys.argv[i+1]
        i += 2
      else:
        sys.exit("Error: Output argument expects a filename\n\n")

    else:
      sys.exit("Usage: Main.py [-c count] [-t tag] [-f filters] [-o output filename]")


  print("count: " + str(count))
  print("tag: " + str(tag))
  print("filters: " + str(filters))
  print("outputFilename: " + str(outputFilename))

  #run(count, tag, filters, outputFilename)
  createCSV()
  print("")









