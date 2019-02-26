# Author: Florian Gabelle
# IMPORTANT NOTE:
# if deepsleep() is in use, the device is actually restarted on exit,
# meaning that both boot.py and main.py are being run everytime,
# and while True: loop is only gone through once

import pycom
import bme_280
import max_44009
import lora_click
import time
import ubinascii

# Convert int to N = "width" characters long string with leading zeroes,
# based on code by pythoncoder at:
# https://forum.micropython.org/viewtopic.php?t=3201
def zfill(s, width):
	return '{:0>{w}}'.format(str(s), w = width)

pycom.heartbeat(False) # turn off blinkind led

time.sleep(1) # wait for sensors and LoRa module to initialize after power-on

lora_click.setup()

while True:
	pycom.rgbled(0x00FF00) # Green
	time.sleep(0.2)
	pycom.rgbled(0x000000) # Off

	# Read data from BME280 + apply coefficients to keep decimal precision
	bme_280_readings = bme_280.get_readings();
	temperature = int(bme_280_readings[0] * 10)
	pressure = int(bme_280_readings[1] * 10000)
	humidity = int(bme_280_readings[2] * 10)
	# Read data from MAX44009
	luminance = int(max_44009.get_luminance())

	# Make data packet
	temperature = zfill(temperature, 4)
	pressure = zfill(pressure, 8)
	humidity = zfill(humidity, 4)
	luminance = zfill(luminance, 4)
	print("T: ", temperature, "\tP:", pressure, "\tH: ", humidity, "\tL: ", luminance)
	data_sent = temperature + pressure + humidity + luminance
	print("data_packet = ", data_sent)

	# Send data
	lora_click.send_data(data_sent)

	#time.sleep(54)
	# Put device in deep sleep mode and make sending data happen about every 1 min
	machine.deepsleep(9000)
