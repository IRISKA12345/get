import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)
    
    def deinit(self):
        """Destructor - cleanup GPIO"""
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    
    def set_number(self, number):
        """Set DAC value using binary representation"""
        if self.verbose:
            print(f"Setting number: {number} (0b{number:08b})")
        
        for i, pin in enumerate(self.gpio_bits):
            bit = (number >> (7 - i)) & 1
            GPIO.output(pin, bit)
    
    def set_voltage(self, voltage):
        """Set DAC voltage - converts voltage to number and calls set_number"""
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Warning: Voltage {voltage}V is out of range [0, {self.dynamic_range}]V")
            voltage = max(0, min(voltage, self.dynamic_range))
        
        number = int((voltage / self.dynamic_range) * 255)
        
        if self.verbose:
            print(f"Voltage {voltage}V -> Number {number}")
        
        self.set_number(number)


if __name__ == "__main__":
    dac = None
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    
    finally:
        if dac is not None:
            dac.deinit()