#put in the weather API
import requests
import json

Weather_URL = "http://api.weatherapi.com/v1/current.json"
Weather_API = "API_KEY"

#functions for al de opties
def Main (URL, API):
    #Options
    Locatie = input("In welke Locatie bevind u zich? :")

    para = {
    "key": API,
    "q": Locatie
    }

    req = requests.get(URL, params=para)
    data = req.json()
    current = data["current"]

    print("Temperatuur is nu : ", current["temp_c"], "Celsius")
    print("Percentage wolken is : ", current["cloud"],"%")
    print("Wind : ",current["wind_kph"], "Km per uur")
    print("Directie van de wind : ",current["wind_dir"])

req = requests.get(Weather_URL, Weather_API)
print("Checking... \nCode is: ", req.status_code)

if (req.status_code == 401):
    print("conectie gemaakt!")
    Main(Weather_URL, Weather_API)
else:
    raise Exception("\n Oops... er is geen conectie") 



