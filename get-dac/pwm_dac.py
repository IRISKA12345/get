import RPi.GPIO as GPIO
import time

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0) 
    
    def deinit(self):
        
        if self.verbose:
            print("Остановка ШИМ и очистка GPIO...")
        self.pwm.stop()
        GPIO.cleanup()
    
    def set_voltage(self, voltage):
        if voltage < 0 or voltage > self.dynamic_range:
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            return
        
        duty_cycle = (voltage / self.dynamic_range) * 100
        
        if self.verbose:
            print(f"Коэффициент заполнения: {duty_cycle:.2f}")
        
        self.pwm.ChangeDutyCycle(duty_cycle)


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    
    finally:
        dac.deinit()