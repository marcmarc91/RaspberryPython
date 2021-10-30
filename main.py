from gpiozero import LightSensor

from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host='192.168.0.297')
ldr = LightSensor(18,pin_factory=factory)

while True:
    ldr.wait_for_light()
    print("Light detected!")
