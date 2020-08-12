#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt


x_interval = np.linspace(-100, 100, 1000)
k_interval = np.linspace(-5, 5, 1000)


def phi(k):
    return 0.1 * np.exp(-k**2.0)


psi_interval = []

for x in x_interval:
    psi_x = 0

    for k in k_interval:
        psi_x = psi_x + phi(k)*np.cos(k*x)
    psi_interval.append(psi_x)

plt.plot(x_interval, psi_interval)
plt.show()
