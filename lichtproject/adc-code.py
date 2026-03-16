#!/usr/bin/python
import spidev
import time
from gpiozero import PWMLED
from gpiozero import LED

#Define Variables
delay = 0.5
ldr_channel = 0

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

#LED setup
led = PWMLED(18)
led.on()
exponent = 2.5
 
def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data
    
 
while True:
    ldr_value = readadc(ldr_channel)
    perc_value = ldr_value / 1023

    print("---")
    print("PERC Value:", perc_value)
    led_value = (1.0 - perc_value) ** exponent
    print("LED Value:", led_value)
    led.value = led_value
    print("---")

    time.sleep(delay)
