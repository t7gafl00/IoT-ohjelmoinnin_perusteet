# -*- coding: utf-8 -*-
# Author: Florian Gabelle
# This code is based on an example found in Mikrobitti magazine from November 2017

from datetime import datetime
from time import strftime
import requests
import json

# Laitetaan aikaleima ja sääantureilta
# saadut arvotdatarakenteeseen
# Arvoa 21 käytetään testitarkoituksessa
# Korvaa kohta oikealla sääanturin
# tiedon lukemisella
def post_data(temperature, pressure, humidity, luminance):
    measurements = {
        #"timestamp": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        "date": str(datetime.now().strftime("%Y-%m-%d")),
        "time": str(datetime.now().strftime("%H:%M:%S")),
        "temperature": str(temperature),
        "pressure": str(pressure),
        "humidity": str(humidity),
        "luminance": str(luminance)
        }
    post_body = json.dumps(measurements)

    # Lähetetään sääantureilta luettu data
    # Api Gatewaylle
    # Kopioi oikea osoite Lambdan
    # triggers -välilehdeltä
    r = requests.post('https://so9cjj3pk8.execute-api.eu-west-1.amazonaws.com/v1/measurementsToDatabase', data = post_body)

    print(r.text, "\n")
