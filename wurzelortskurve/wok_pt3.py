import numpy as np
import control
import matplotlib.pyplot as plt
a0 = 1.; a1 = 10. ; a2 = 31. ; a3 = 30.
b0 = 1.
num  = np.array([b0])
den  = np.array([a3, a2, a1, a0])
stand = control.tf(num,den)
po=control.pole(stand)
print(stand,'Die Pole sind : ',po)
control.root_locus(stand)
plt.title('Wurzelortskurve')
plt.grid()
plt.show()