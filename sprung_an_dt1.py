import math
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import os

K=0.9 #Übertragungskonstante
T = 0.5 #Zeitkonstante

lti = sc.signal.TransferFunction([K, 0], [T, 1])
t, y = sc.signal.step(lti)
plt.plot(t, y)
plt.axis('off')
plt.savefig(os.path.basename(__file__)+".svg", format="svg")
plt.axis('on')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step response')
plt.grid()

plt.show()