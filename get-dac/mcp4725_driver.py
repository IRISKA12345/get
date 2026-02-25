import smbus
import time

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose=True):
        """Инициализация I2C ЦАП MCP4725"""
        self.bus = smbus.SMBus(1)
        self.address = address
        self.mm = 0x00  
        self.pds = 0x00 
        self.verbose = verbose
        self.dynamic_range = dynamic_range
    
    def deinit(self):
        """Деструктор - закрытие I2C шины"""
        self.bus.close()
    
    def set_number(self, number):
        """
        Отправка числа в MCP4725
        number: 12-битное число (0-4095)
        """

        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")
            return
        
        if not (0 <= number <= 4095):
            print(f"Число выходит за разрядность MCP4725 (12 бит): {number}")
            return
        
        first_byte = self.mm | self.pds | ((number >> 8) & 0x0F)
        second_byte = number & 0xFF
        
        self.bus.write_byte_data(self.address, first_byte, second_byte)
        
        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: "
                  f"[0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]")
    
    def set_voltage(self, voltage):
        """
        Установка напряжения на выходе ЦАП
        voltage: напряжение в вольтах (0.0 - dynamic_range)
        """
        if voltage < 0 or voltage > self.dynamic_range:
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            return
        
        number = int((voltage / self.dynamic_range) * 4095)
        
        if self.verbose:
            print(f"Напряжение {voltage}В -> Число {number}")
        
        self.set_number(number)


if __name__ == "__main__":
    try:
        dac = MCP4725(dynamic_range=5.11, address=0x61, verbose=True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз.")
    
    finally:
        dac.deinit()