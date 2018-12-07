import urllib.parse
import requests



mainApi = "https://maps.googleapis.com/maps/api/geocode/json?"
key = "AIzaSyA_VwLMTCKbOcplIRwvrei8ivqKzCpdrKw"

print("At any time you can quit by entering 'quit' or 'exit'" + "\n")

while True:
    address = input("Enter an Address: ")

    if address == "quit" or address == "exit":
        break

    url = mainApi + urllib.parse.urlencode({"address":address,"key":key})  #Create URL w/ Encoding

    jsonData = requests.get(url) .json()   #Returning Json payload of GET request
    #print(jsonData)   #Testing Request is properly formatted :: OK

    print(url)
    jsonStatus = jsonData["status"]
    print("API Status -> " + jsonStatus)  #Return Status of API Request

    if jsonStatus == "OK":

        for each in jsonData["results"][0]["address_components"]:   #Iterate through each address component
            print(each["long_name"])

        formattedAddress = jsonData["results"][0]["formatted_address"]   #Set Formatted Address to Variable
        print("\n" + formattedAddress)   #Print Formatted Address


