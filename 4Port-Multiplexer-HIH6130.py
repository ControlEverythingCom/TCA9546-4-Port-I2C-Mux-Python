import smbus
import time
import sys

address = 112
hihaddress = 0x27


bus = smbus.SMBus(1)
print "start"

data = bytearray()

i = 1
sensorNum = 1
while(i < 9):
    bus.write_byte(address, i)
    time.sleep(0.1)
    data = bus.read_i2c_block_data(hihaddress, 4)
    temp = (((data[2] * 256) + (data[3] & 0xFC)) / 4)
    cTemp = (temp / 16384.0) * 165.0 - 40.0
    fTemp = (cTemp * 1.8)+32
    print "Temp on Sensor %i: %.2f C, %.2f F" % (sensorNum, cTemp, fTemp)
    sensorNum = sensorNum + 1
    i = i * 2
