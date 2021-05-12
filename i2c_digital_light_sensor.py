
import smbus
import time

# Default I2C bus on RPi 4
bus = smbus.SMBus(1)

# Address of I2C Device
# 0x23 is Default and 0x5C if connected
address = 0x23 

# Use ONE_TIME_HIGH_RES_MODE_1 with resolution 1lx and time 120ms
mode = 0x20

# Read light level from light sensor
def get_data():
    data = bus.read_i2c_block_data(address, mode)
    result = (data[1] + (256 * data[0])) / 1.2
    return result

# Categorise lighting level based on indoor lighting
def get_category():
    if 0 <= light_level <= 10:
        return "too dark"
    elif 10 <= light_level <= 100:
        return "dark"
    elif 100 <= light_level <= 500:
        return "medium"
    elif 500 <= light_level <= 3000:
        return "bright"
    elif 3000 <= light_level <= 65535:
        return "too bright"

try:
    while True:
        light_level = get_data()
        # Print current light level as lux
        #print(f'Light Level: {light_level:.2f} lx')
        print(get_category())
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting")
