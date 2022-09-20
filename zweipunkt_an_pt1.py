import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

from enum import Enum

#Define Time
t_span = (0.0, 5.0)
t_step = 0.01
ts = np.arange(t_span[0], t_span[1], t_step)

#Define System
Kp_pt1 = 1
T_pt1  = 1
def system_pt1(t, state, tps):
    y=state
    u=tps.do(y, 50, 20)
    dydt=(Kp_pt1*u-y)/T_pt1
    return dydt


#Two-Point-Controller
class TwoPointController:
    class TwoPointState(Enum):
        UPPER = 1
        LOWER = 2
    state = TwoPointState.LOWER
    min=0
    max=0
    
    def __init__(self, min, max, highInputMeansMaxOutput, initialState):
        self.state=initialState
        self.min=max if highInputMeansMaxOutput else min
        self.max=min if highInputMeansMaxOutput else max
        dir=highInputMeansMaxOutput

    def do(self, input, setpoint, hysteresis):
        if self.state==TwoPointController.TwoPointState.UPPER:
            if input < setpoint-hysteresis/2:
                self.state=TwoPointController.TwoPointState.LOWER
                return self.max
            else:
                return self.min
        else:
            if input > setpoint+hysteresis/2:
                self.state=TwoPointController.TwoPointState.UPPER
                return self.min
            else:
                return self.max



setpoint = 50
power_max= 100
power_min=0
v_0 = 10
tps= TwoPointController(power_min, power_max, False, TwoPointController.TwoPointState.LOWER)

sol = sc.integrate.solve_ivp(system_pt1, t_span, [v_0], args=(tps,), max_step=0.001)
plt.plot(sol.t, sol.y[0,:])
plt.show()