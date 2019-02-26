from machine import I2C

i2c = I2C(0, I2C.MASTER, baudrate=100000)

device_addr = 42    # 0x2A
update_reg = 192    # 0xCO
temp_reg = 1        # 0x01

def get_data(buffer):
    i2c.writeto_mem(device_addr, update_reg, b'\xFF')       # request readings update
    i2c.readfrom_mem_into(device_addr, temp_reg, buffer)    # read data starting from temp register to buffer

def bytes_to_int(bytes):  # convert two first bytes from buffer array to one int
    int_value = bytes[0] << 8 | bytes[1]
    #print(int_value)
    return int_value