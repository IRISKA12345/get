import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
signal = 6
GPIO.setup(signal, GPIO.IN)
while True:
    if GPIO.input(signal):
        GPIO.output(led, 0)
    else:
        GPIO.output(led, 1)