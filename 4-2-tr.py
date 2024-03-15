import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def to_bytes(n):
    array = [0 for i in range(8)]

    d_n = n % 256

    bin_n = bin(d_n)

    i = -1
    while bin_n[i] != 'b':
        array[i] = int(bin_n[i])
        i -= 1

    return array

try:
    number = input("Enter number: ")
    try:
        number = int(number)
        array = to_bytes(number)
        GPIO.output(dac, array)
        print(f"Period is: {number} sec")
        sleep_t = float(number) / (256*2)
        out_n = 0
        while True:
            for i in range(255):
                GPIO.output(dac, to_bytes(i))
                time.sleep(sleep_t)
            for i in range(255, 0, -1):
                GPIO.output(dac, to_bytes(i))
                time.sleep(sleep_t)

    except Exception:
        print("Enter number, not string!")


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
