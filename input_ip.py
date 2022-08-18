# myfile = open("data.txt", "w+")

# while(True):

#     uaddress = input("Enter your Ip Address: ")

#     if uaddress == 'quit':
#       exit()

# myfile.write("\r\n IP ADDRESS :" +uaddress+ " \r\n")
# print("DATA SAVED TO THE FILE")

import requests

def enterIpAddress():    
    ip = input("Enter ip address: ")
    if ip == "":
        print("Enter vaild ip address")
        enterIpAddress()
    resp = requests.get("https://ipwho.is/" + ip)
    if resp.status_code == 200:
        print("IP -> " + resp.json().get("ip"))
        print("Continent -> " + resp.json().get("continent"))
        print("Country -> " + resp.json().get("country"))
        print("Country_code -> " + resp.json().get("country_code"))
        print("Region -> " + resp.json().get("region"))
        print("Region_code -> " + resp.json().get("region_code"))
        print("City -> " + resp.json().get("city"))

enterIpAddress()

