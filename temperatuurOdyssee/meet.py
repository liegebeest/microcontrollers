#!/usr/bin/python3

import smbus
import time
import datetime
from gpiozero import LED

groen = LED(18)
rood = LED(17)


while(True):
    bus =  smbus.SMBus(1)
    data = bus.read_i2c_block_data(0x48, 0)
    msb = data[0]
    lsb = data[1]
    temp = float(msb*256+lsb)/256
    if temp < 20:
        print(datetime.datetime.now(), "te lage temp, verwarming branden:", temp, "°C")
        rood.on()
        groen.off()
    else:
        print(datetime.datetime.now(), "temperatuur ok, verwarming mag af:", temp, "°C")
        rood.off()
        groen.on()
    time.sleep(5)


