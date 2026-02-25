import pwm_dac
import time
import math

FREQUENCY = 1  
AMPLITUDE = 2.5 
OFFSET = 2.5 
SAMPLE_RATE = 100 

def main():
    dac = None
    try:

        dac = pwm_dac.PWM_DAC(12, 500, 5.0, False)
        
        start_time = time.time()
        sample_interval = 1.0 / SAMPLE_RATE
        
        print("Генерация sin(t)...")
        print(f"Частота: {FREQUENCY} Гц")
        
        sample_num = 0
        while True:
            t = sample_num / SAMPLE_RATE
            
            sine_value = math.sin(2 * math.pi * FREQUENCY * t)
            
            voltage = OFFSET + AMPLITUDE * sine_value
            voltage = max(0, min(5.0, voltage))
            
            dac.set_voltage(voltage)
            
            sample_num += 1
            
            time.sleep(sample_interval)
    
    except KeyboardInterrupt:
        print("Остановка генерации...")
    
    finally:
        if dac is not None:
            dac.deinit()

if name == "main":
    main()