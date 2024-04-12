
import RPi.GPIO as GPIO
from time import sleep

dac    = [8, 11, 7, 1, 0, 5, 12, 6]
troyka = 13
comp   = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)

GPIO.setup(comp, GPIO.IN)


def dbl(number):
    binary_list = []
    while number > 0:
        remainder = number % 2
        binary_list.insert(0, remainder)
        number = number // 2
    while len(binary_list) < 8:
        binary_list.insert(0, 0)
    return binary_list


def adc():
    res = 0
    i = 128
    while i >= 1:
        GPIO.output(dac, dbl(int(i + res)))
        sleep(0.01)
        tmp = GPIO.input(comp)
        if tmp == 0:
            res += i
        i /= 2
    
    return res

try:
    while True:
        q = adc()
        i = 3.3 * q / 256.0
        print("current volt: ", i)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
    print("EOooo")
