import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

dac    = [8, 11, 7, 1, 0, 5, 12, 6]
led    = [2, 3, 4, 17, 27, 22, 10, 9]
troyka = 13
comp   = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(comp, GPIO.IN)

data_v = []
data_t = []

# Функция переводящая напряжение в массив 1 и 0 для вывода да плату
def dbl(number):
    binary_list = []
    while number > 0:
        remainder = number % 2
        binary_list.insert(0, remainder)
        number = number // 2
    while len(binary_list) < 8:
        binary_list.insert(0, 0)
    return binary_list

# Функция получающая значение с компаратора и переводящая в число от 0 до 255
def adc():
    res = 0
    i = 128
    while i >= 1:
        GPIO.output(dac, dbl(int(i + res)))
        time.sleep(0.01)
        tmp = GPIO.input(comp)
        if tmp == 0:
            res += i
        i /= 2
    
    return res


try:
    while True:
        GPIO.output(troyka, 0)
        q = adc()
        #i = 3.3 * q / 256.0
        print("Current volt: ", q)
        tmp = dbl(2**int(q  / 32) - 1)
        GPIO.output(led, tmp)

        if (q == 0):
            print("Start!")
            time.sleep(1)
            break

    GPIO.output(troyka, 1)

    old_q = 0

    while True:
        q = adc()

        if (old_q - q <= 0.001):
            print("Turn off voltage!")
            break

        old_q = q

        print("Current volt: ", q)
        tmp = dbl(2**int(q  / 32) - 1)
        GPIO.output(led, tmp)

    GPIO.output(troyka, 0)

    while True:
        q = adc()

        if (old_q - q <= 0.001):
            print("End!")
            break

        old_q = q

        print("Current volt: ", q)
        tmp = dbl(2**int(q  / 32) - 1)
        GPIO.output(led, tmp)
            

        



finally:
    GPIO.output(dac, 0)
    GPIO.output(led, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
    print("EOooo")