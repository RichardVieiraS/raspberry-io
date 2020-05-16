#!/urs/bin/env python3
import os
from gpiozero import LED
from time import sleep

led = LED(17)
os.system("...Running pin17bkink.py")

while True:
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.15)


