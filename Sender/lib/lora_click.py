# Author: Florian Gabelle

from machine import UART
from machine import Pin
import time

# Initialize LoRa module reset pin
resetPin = Pin('P19', mode=Pin.OUT)
resetPin.value(1);

# Initialize serial connection
ser = UART(1, baudrate=57600)

# Reset LoRa click module
def lora():
    resetPin.value(0);
    resetPin.value(1);
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
    line = ser.readline()
    line = str(line)
    line = line[2:-5]  # remove extra characters "b'" and "\r\n'" from string
    time.sleep(0.08) # may return 'busy' without this delay
    return line

# Write one line to LoRa click module serial port
def write_line(line):
    line += "\r\n"
    ser.write(str.encode(line))

# Send data over LoRa connection
def send_data(data_str):
    ser.write("radio tx ")
    ser.write(data_str)
    ser.write("\r\n")

    response_after_command = read_line()
    print(response_after_command)
    if response_after_command != "ok":
        lora()
        return -1
    response_after_transmission = read_line()
    print(response_after_transmission, "\n")
    if response_after_transmission == "radio_err":
        lora()
        return -1

# Receive data using LoRa click module
def receive_data():
    write_line("radio rx 0") # continuous reception mode

    response_after_command = read_line()
    print("response_after_command = ", response_after_command)

    if response_after_command != "ok": # if response is 'invalid_param' or 'busy'
        lora()
        print("not ok")
        return -1

    response_after_receive = read_line()
    print("response_after_receive = ", response_after_receive)

    if response_after_receive[0:8] != "radio_rx": # if reception was not successful
        return -1
    else: # if response contains data
        return response_after_receive
