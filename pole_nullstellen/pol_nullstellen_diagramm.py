import numpy as np
import control.matlab as ma
import matplotlib.pyplot as plt
num = np.array([1,5, 4])
den  = np.array([1,8, 25, 26])
print(den)
print("Pole = ", str(np.roots(den)) )
sys = ma.tf(num,den)
print(sys)
print("Pole = ", ma.pole(sys) )
print("Nullstellen = ", ma.zero(sys) )
ma.pzmap(sys)
plt.grid()
plt.show()