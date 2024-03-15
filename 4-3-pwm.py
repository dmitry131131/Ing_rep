import RPi.GPIO as GPIO

pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 1000)
p.start(0)

try:
    while True:
        f = int(input("Enter frec: "))
        p.ChangeDutyCycle(f)
        print(3.3*f/100)

finally:
    p.stop()
    GPIO.output(pin, 0)
    GPIO.cleanup()