import matplotlib.pyplot as plt

import numpy as np

PI = np.pi

x  =  np.arange(-100,100,0.1)
y = x**2 * ( 1 + np.cos(2 * PI * x / 20))

plt.figure(figsize=(16,9))
plt.plot(x,y)
plt.show()

