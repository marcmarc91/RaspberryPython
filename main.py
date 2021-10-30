from gpiozero import LED
from time import sleep
from signal import pause
led = LED("GPIO17")

led.blink()
pause()