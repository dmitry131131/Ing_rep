import RPi.GPIO as GPIO
import time

dac_array = [6, 12, 5, 0, 1, 7, 11, 8]
number = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac_array, GPIO.OUT)

GPIO.output(dac_array, number)

time.sleep(10)

GPIO.output(dac_array, 0)
