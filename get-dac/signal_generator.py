import time
import numpy

def get_sin_wave_amplitude(freq, time):
    return (numpy.sin(2 * numpy.pi * freq * time) + 1) / 2

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1 / sampling_frequency)