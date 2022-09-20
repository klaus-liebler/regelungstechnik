from numpy.polynomial import Polynomial
from numpy.polynomial import polynomial as P
import numpy as np
import matplotlib.pyplot as plt
import cmath;

p1=Polynomial.fromroots([complex(1, 2), complex(1,-2)])

p2=Polynomial([-25,31,-7,1])

print(p2.roots())
p3 = Polynomial([-1, 1])
p4=P.polydiv(p2.coef, p3.coef)
print(p4)