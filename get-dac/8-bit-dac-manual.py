import RPi.GPIO as GPIO
import time

print()

dac_bins = [16,20,21,25,26,17,27,22]

GPIO.setmode(GPIO.BCM)
for pin in dac_pins:
    GPIO.setup(pin,GPIO.OUT)

V_REF = 3.3

def voltage_to_number(voltage):
    if not (0.0 <=voltage<=V_REF):
        print(f"Нвпряжение выходит за динамический диапазон ЦАП")
        print("Устанавливаю 0.0 В")
        return 0
    return int(voltage / V_REF * 255)

def number_to_dac(number):
    for i in range(8):
        bit = (number>>(7-i)) & 1
        GPIO.output(dac_bits[i],bit)

GPIO.setmode(GPIO.BCM)
for pin in dac_pins:
    GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        try:
            voltare = float(input("Введите напряжение в Вольтах:"))
            number = voltare_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы не ввели число.Попробуйте еще раз.")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()