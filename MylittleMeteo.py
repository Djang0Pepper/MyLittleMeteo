#-*- coding: utf-8 -*-
#cf1cc9f567a1427aa85f4cc553727ff1
#Consultation API météo avec openweathermap merci, encore ??, lionel

import requests
import json
import datetime
import time

ville = "cappelle-la-grande"
myapi = "cf1cc9f567a1427aa85f4cc553727ff1"
#récupère le temps actuel

url_weather = "http://api.openweathermap.org/data/2.5/weather?q="+ville+"&APPID="+myapi
r_weather = requests.get(url_weather)
data = r_weather.json()
print(data)
print("my little meteo à " + ville)

t = data['main']['temp']
print("La temperature moyenne est de {0:.1f} degres Celsius ".format(t-273.15))


f = data['main']['feels_like']
print("La temperature resentie est de {00:.1f} degres Celsius".format(f-273.15))

Humidite = data['main']['humidity']
print("Taux d'humidite de {}".format(Humidite) + "%")

Sunrise = data['sys']['sunrise']
#Sr=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(Sunrise))
Sr=time.strftime("%H:%M", time.gmtime(Sunrise))
print("levé soleil "+str(Sr))

Sunset = data['sys']['sunset']
Ss=time.strftime("%H:%M", time.gmtime(Sunset))
#Ss=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(Sunset))
print("couché soleil "+str(Ss))
