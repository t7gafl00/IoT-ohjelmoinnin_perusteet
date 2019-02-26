# Modifications brought by Florian Gabelle to make this program compatible with MicroPython
# This code is based on the one designed to work with the MAX44009_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/products

from machine import I2C
import time

i2c = I2C(0, I2C.MASTER, baudrate = 100000)

# Registers / messages
MAX44009_address = 74       # (0x4A)
configuration_register = 02 # (0x02)
luminance_register = 03 # (0x03)
continuous_mode = 64        # (0x40)

# Set continuous mode, integration time = 800ms
i2c.writeto_mem(MAX44009_address, configuration_register, continuous_mode)
time.sleep(0.5)

def get_luminance():
    # Read data, 2 bytes
    data = i2c.readfrom_mem(MAX44009_address, luminance_register, 2)

    # Data conversion (to lux)
    exponent = (data[0] & 0xF0) >> 4
    mantissa = ((data[0] & 0x0F) << 4) | (data[1] & 0x0F)
    luminance = ((2 ** exponent) * mantissa) * 0.045

    # Output data to screen
    #print("Ambient Light luminance : %.2f lux" %luminance)

    return luminance
