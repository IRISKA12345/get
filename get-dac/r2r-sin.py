import r2r_dac as r2r
import signal_generator as sg
import time
import matplotlib.pyplot as plt
import numpy as np

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
voltage = []
times = []

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
    start_time = time.time()
    while True:
        current_time = time.time() - start_time
        times.append(current_time)
        signal = amplitude*sg.get_sin_wave_amplitude(signal_frequency, current_time)
        voltage.append(signal)
        dac.set_voltage(signal)
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    dac.deinit()
    t = np.arange(0, max(times), 1/sampling_frequency)
    sawtooth = (amplitude * 2 * signal_frequency * t) % (2*amplitude)
    triangle = amplitude - np.abs(sawtooth - amplitude)
    plt.plot(t, triangle)
    plt.title("Треугольный сигнал")
    plt.xlabel('Время')
    plt.ylabel('Амплитуда')
    plt.grid()
    plt.show()