# -*-coding: utf-8 -*-

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
    GPIO.output(resetPin, GPIO.LOW)
    GPIO.output(resetPin, GPIO.HIGH)
    setup()
    
# Initializing LoRa click module
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
    
# Read one line from LoRa click module serial port
def read_line():
    line = ser.readline().decode('utf-8')
    line = line[:-2]  # remove extra characters '\r\n' at the end of string
    time.sleep(0.08) # may return 'busy' without this delay
    return line

# Write one line to LoRa click module serial port
def write_line(line):
    line += "\r\n"
    ser.write(str.encode(line))

# Receive data using LoRa click module
def receive_data():
    write_line("radio rx 0") # continuous reception mode
    
    response_after_command = read_line()
    if response_after_command != "ok": # if response is 'invalid_param' or 'busy'
        print(response_after_command)
        reset()
        return -1
    else:
        print("Waiting for data packet\n")

    response_after_receive = read_line()
    if response_after_receive[0:8] != "radio_rx": # if reception was not successful
        print(response_after_receive)
        return -1
    else: # if response is ok
        print("Data packet received: ", response_after_receive[10:])
        return response_after_receive[10:]