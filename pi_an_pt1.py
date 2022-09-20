import math
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import os
import control

K_PS = 1 #Strecke Übertragungskonstante
T_S  = 1 #Strecke Zeitkonstante
T_N  = 0.1 #Regler Nachstellzeit
K_PR = 10 #Regler Verstärkung

controller = control.tf([K_PR*T_N, K_PR], [T_N, 0])
plant = control.tf([K_PS], [T_S, 1])
primary =  control.series(controller, plant)
feedback = control.tf([1], [1])
sys= control.feedback(primary, feedback, -1)
(t, y) = control.step_response(sys)
plt.plot(t, y)
plt.axis('off')
plt.savefig(os.path.basename(__file__)+".svg", format="svg")
plt.axis('on')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step response')
plt.grid()

plt.show()