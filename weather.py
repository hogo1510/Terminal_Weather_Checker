#put in the weather API
import requests

Weather_URL = "http://api.weatherapi.com/v1/current.json"
Weather_API = "Your key"
req = requests.get(Weather_URL)
print("Checking... \nCode is: ", req.status_code)
#functions for al de opties
def Main ():
    #Options

    Locatie = input("In welke Locatie bevind u zich?")



