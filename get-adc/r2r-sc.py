import r2r_adc
import time
import adc_plot

r2r = r2r_adc.R2R_ADC(3.3)
voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.time()
    while (time.time() - start_time) < duration:
        voltage_values.append(r2r.get_sc_voltage())
        time_values.append(time.time() - start_time)
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, 3.3)
    adc_plot.plot_sampling_period_hist(time_values)
finally:
    r2r.deinit()