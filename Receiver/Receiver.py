# Author: Florian Gabelle

# -*-coding: utf-8 -*-

import lora_click
import aws
#import mysli

# Parse received data packet string and assign values to different variables
def parse_data(data_packet):
    global temperature
    global pressure
    global humidity
    global luminance
    
    temperature = int(data_packet[0:4]) / 10
    pressure = int(data_packet[4:12]) / 10000
    humidity = int(data_packet[12:16]) / 10
    luminance = int(data_packet[16:20])

    print("temperature: ", temperature)
    print("pressure: ", pressure)
    print("humidity: ", humidity)
    print("luminance: ", luminance)
    print("")

lora_click.setup()
while 1:    
    data_packet = lora_click.receive_data()
    if data_packet != -1:
        parse_data(data_packet)
        aws.post_data(temperature, pressure, humidity, luminance)
        #mysli.to_db(temperature, pressure, humidity, luminance)
