import RPi.GPIO as GPIO

out_array = [9, 10, 22, 27, 17, 4, 3, 2]
in_array = [21, 20, 26, 16, 19, 25, 23, 24]

in_status = [1, 0, 0, 0, 0, 0, 0, 0]

GPIO.setmode(GPIO.BCM)

GPIO.setup(out_array, GPIO.OUT)
GPIO.setup(in_array, GPIO.IN)

while 1:
    for i in range(8):
        in_status[i] = GPIO.input(in_array[i])

    GPIO.output(out_array, in_status)
