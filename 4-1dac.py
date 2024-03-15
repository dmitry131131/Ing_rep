import RPi.GPIO as GPIO

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
    while True:
        number = input("Enter number from 0 to 255: ")
        if number == "q": break
        try:
            number = int(number)
            if 0 <= number <= 255:
                array = to_bytes(number)
                GPIO.output(dac, array)
                volt = (float(number) / 256) * 3.3
                print(f"Voltage is: {volt:.4}")
            else:
                print("Enter number from 0 to 255!")

        except Exception:
            print("Enter number, not string!")


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
