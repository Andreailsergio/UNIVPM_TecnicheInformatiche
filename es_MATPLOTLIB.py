# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:41:42 2020

@author: andrea_sergiacomi
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1.0, 50, endpoint=True)
y1 = x**0.5
y2 = x**2
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()