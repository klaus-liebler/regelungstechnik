import math
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import os

K=1 #Übertragungskonstante
T = 1 #Zeitkonstante
D = 1 #Dämpfung

#lti = sc.signal.TransferFunction([K], [T*T, 2*D*T, 1])
lti = sc.signal.TransferFunction([10], [T*T, 2*D*T, 1])
t, y = sc.signal.step(lti, T=np.arange(0, 10, 0.01))
plt.plot(t, y)
plt.axis('off')
plt.savefig(os.path.basename(__file__)+".svg", format="svg")
plt.axis('on')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step response')
plt.grid()

plt.show()