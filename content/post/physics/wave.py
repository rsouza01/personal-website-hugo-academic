#!/usr/local/bin/python3

import numpy as np
import math
import matplotlib.pyplot as plt

x_interval = np.linspace(0, 10, 100)
k_interval = np.linspace(0, 2*math.pi, 100)
phi = 1
x = 0

i = 0
for x in x_interval:
    for k in k_interval:
        k_plot = phi*np.cos(k*x)
        plt.plot(k, k_plot)

plt.show()
