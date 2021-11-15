# https://www.instructables.com/Raspberry-Pi-Remote-GPIO/
# https://pinout.xyz/
# https://gpiozero.readthedocs.io/en/stable/index.html

from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

from time import sleep

factory = PiGPIOFactory(host='rpizero')
red = LED(8,pin_factory=factory)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)