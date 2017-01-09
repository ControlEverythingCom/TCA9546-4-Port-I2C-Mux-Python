import smbus
import time
import sys

address = 112


bus = smbus.SMBus(1)
print "start"

i = 1
port = 1
while(i < 9):
    present = False
    bus.write_byte(address, i)
    time.sleep(0.1)
    print 'port %i' % port
    for x in range(1,127):
        try:
            status = bus.write_quick(x)
            if(x != 112):
               print 'device present at %i' % x
               present = True
        except IOError, err:
            continue
    if(present != True):
        print 'no devices on port %i' % port
    port = port + 1
    i = i * 2
