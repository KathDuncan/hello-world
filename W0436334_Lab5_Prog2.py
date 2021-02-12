# W0436334 Kath Duncan
# EETG3024 Advanced Embedded Controllers
# Ricardo Bautista-Quintero
# Lab 5 Part 2
# Change LED brightness level using sin function
#
# Frequency = 0.3Hz, therefore period = 3.333s = 10/3s
# Sin range = 0 - 2pi. Across 10/3s, this is 3/5pi per second

from gpiozero import PWMLED
from time import sleep
import math

led = PWMLED(17)                # LED connected to GPIO 17
x = ((2*math.pi)/(10/3))/10
a = 0

while True:
    y = ((math.sin(a))+1)/2
    led.value = y
    sleep(0.1)
    a+=x
    if a >= (2*math.pi):
        a = x