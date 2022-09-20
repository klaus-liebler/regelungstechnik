import math
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from labellines import labelLine, labelLines

# Streckendaten:
R=1
C=1


#definiere Simulationszeitraum
t_span = (0.0, 20)
t_step = 0.01
ts = np.arange(t_span[0], t_span[1], t_step)
u_vect=[]

class SinusGenerator:
    min=0
    max=0
    T=0
    def __init__(self, min, max, T):
        self.min=min
        self.max=max
        self.T=T

    def calc(self, t):
        return math.sin((2*math.pi/self.T)*t)

#define das System
def system_RC(t, v, gen): #t ist Zeit, v ist die aktuelle Kondensatorspannung
    u=gen.calc(t)
    u_vect.append(u)
    return (u-v)/(R*C)

gen= SinusGenerator(-1, +1, 5)
v_0 = 0
sol = sc.integrate.solve_ivp(system_RC, t_span, [v_0], args=(gen,), max_step=0.01)
plt.plot(sol.t, sol.y[0,:])
plt.plot(sol.t, [gen.calc(t) for t in sol.t])
plt.show()