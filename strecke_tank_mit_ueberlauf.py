import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from labellines import labelLine, labelLines

#  Eingabefeld mit Angabe der Voreinstellungen  
u_pumpe_vect=np.arange(2.0, 10.0, 1.0)

# Streckendaten:
A_ab=6          # 3 < Aab0 < 9  (mm^2) Fester Wert der Abflußventilöffnung  (offene Querschnittsfläche)
A_tank=30       #  cm^2, Tankquerschnittfläche
c_p=2           #  (g/s)/V, Pumpenkonstante
hmax=16         #  cm, Überlauf

# Rechne in SI-Einheiten um
A_tank=1e-4*A_tank #  cm^2 in m^2
c_p=1e-3*c_p       #  (g/s)/V in (kg/s)/V
hmax=hmax*1e-2     #  cm in m
A_ab=A_ab*1e-6     #  mm^2 in m^2

#definiere physikalische Konstanten
rho=1e3         #  kg/m^3
g=9.81;         #  m/s^2

# berechne Faktoren einmalig vorab
c1=np.sqrt(2*g)/A_tank
c2=c_p/(rho*A_tank)



te=300


#definiere Simulationszeitraum
t_span = (0.0, 500.0)
t_step = 1
ts = np.arange(t_span[0], t_span[1], t_step)

#define das System
def system_tank(t, h, u_pumpe): #t ist Zeit, h ist die aktuelle Füllhöhe
    dhdt=-c1*A_ab*np.sqrt(h)+c2*u_pumpe #siehe Buch S. 63
    if h>=hmax:
        return 0
    return dhdt


v_0 = 0
#bereite die grafische Ausgabe vor

fig=plt.figure()
ax1=fig.add_subplot(311)
ax2=fig.add_subplot(312, sharex=ax1)
ax3=fig.add_subplot(313)
fig.subplots_adjust(hspace=0.5)
fig.set_figwidth(10)
fig.set_figheight(8)
fig.suptitle("Tank mit Überlauf")
ax1.set_title("Eingang - Pumpenspannung [Volt]")
ax1.grid()
ax2.set_title("Ausgang - Füllstand [m]")
ax2.grid()
ax3.set_title("Kennlinie")
ax3.grid()

final_v=[]

#iteriere über alle Möglichkeiten
for u_pumpe in np.nditer(u_pumpe_vect):
    sol = sc.integrate.solve_ivp(system_tank, t_span, [v_0], args=(u_pumpe,), max_step=1)
    u=np.linspace(u_pumpe, u_pumpe, len(sol.t))
    u[0]=0
    ax1.plot(sol.t, u)
    ax2.plot(sol.t, sol.y[0,:], label='u='+str(u_pumpe))
    final_v.append(sol.y[0,-1])
ax3.plot(u_pumpe_vect, final_v, "x-")
labelLines(ax2.get_lines(), zorder=2.5)
plt.show()