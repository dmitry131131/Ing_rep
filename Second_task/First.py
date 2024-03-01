import RPi.GPIO as GPIO
import time

led_array = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_array, GPIO.OUT)

while 1:
    for i in range(8):
        GPIO.output(led_array, 0)
        GPIO.output(led_array[i], 1)
        time.sleep(0.5)
