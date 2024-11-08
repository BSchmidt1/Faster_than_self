import tkinter as tk
import threading
import time
import random
import math
from scripts.flickering_windows import create_window

def random_frequency():
    # Generate a random frequency between 0.05 and 0.0001 on a logarithmic scale
    log_min = math.log10(0.0001)
    log_max = math.log10(0.05)
    log_freq = random.uniform(log_min, log_max)
    freq = 10 ** log_freq
    return freq

def main():
    # Get user input for duration and number of windows
    duration = 10000000000
    num_windows = 8

    # Create and start each window with a random frequency
    windows = []
    for i in range(num_windows):
        freq = random_frequency()
        pos = (random.randint(0, 1920), random.randint(0, 1080))  # Random position on the screen
        threading.Thread(target=create_window, args=(freq, duration, pos)).start()

if __name__ == "__main__":
    main()
