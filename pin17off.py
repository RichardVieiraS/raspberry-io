#!/urs/bin/env python3

from gpiozero import LED

led = LED(17)

while True:
    led.off()