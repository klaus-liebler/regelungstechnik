from numpy.polynomial import Polynomial
from numpy.polynomial import polynomial as P
import numpy as np
import matplotlib.pyplot as plt
import cmath;


print("np.arctan(-2)", np.arctan(-2))
x_span = (-10.0, 10.0)
x_step = 0.01
x = np.arange(x_span[0], x_span[1], x_step)
plt.plot(x, np.arctan(x))
plt.xlabel('x')
plt.ylabel('arctan(x)')
plt.grid()
plt.show()