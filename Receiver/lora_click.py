# -*- coding: utf-8 -*-
# Author: Florian Gabelle

import RPi.GPIO as GPIO
import serial
import time

# Set up LoRa click module reset pin (active LOW)
resetPin = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(resetPin, GPIO.OUT)
GPIO.output(resetPin, GPIO.HIGH)

# Initializing serial connection with LoRa click module
ser = serial.Serial ("/dev/serial0", baudrate = 57600)

# Reset LoRa click module
def reset():
    # Hardware reset, does not solve "stuck in 'busy' mode"
    #GPIO.output(resetPin, GPIO.LOW)
    #GPIO.output(resetPin, GPIO.HIGH)
    
    # Software reset, solves "stuck in 'busy' mode"
    write_line("sys reset")
    print(read_line())
    
# Initialize LoRa click module
def setup():
    print ("START LoRa setup\r\n")
    write_line("sys get ver")
    print(read_line())
    write_line("mac pause")
    print(read_line())
    write_line("radio set mod lora")
    print(read_line())
    write_line("radio set freq 869100000")
    print(read_line())
    write_line("radio set pwr 14")
    print(read_line())
    write_line("radio set sf sf7")
    print(read_line())
    write_line("radio set crc on")
    print(read_line())
    write_line("radio set iqi off")
    print(read_line())
    write_line("radio set cr 4/5")
    print(read_line())
    write_line("radio set wdt 0")
    print(read_line())
    write_line("radio set sync 12")
    print(read_line())
    write_line("radio set bw 125")
    print(read_line())
    print ("END LoRa setup\r\n")
    time.sleep(1)
    
# Read one line from LoRa click module serial port
def read_line():
    line = ser.readline().decode('utf-8')
    line = line[:-2] # remove extra characters '\r\n' at the end of string
    time.sleep(0.08) # may return 'busy' without this delay
    return line

# Write one line to LoRa click module serial port
def write_line(line):
    line += "\r\n"
    ser.write(str.encode(line))

# Receive data using LoRa click module
# Returns -1 on error
# Retuns data from received packet on success
def receive_data():
    write_line("radio rx 0") # continuous reception mode
    
    response_after_command = read_line()
    print("response_after_command: ", response_after_command)
    if response_after_command != "ok": # if response is 'invalid_param' or 'busy'
        reset()
        setup()
        return -1
    else:
        print("Waiting for data packet\n")

    response_after_receive = read_line()
    print("response_after_receive: ", response_after_receive)
    if response_after_receive[0:8] != "radio_rx":
        return -1
    else: # if response is ok
        print("Data packet received: ", response_after_receive[10:])
        return response_after_receive[10:]