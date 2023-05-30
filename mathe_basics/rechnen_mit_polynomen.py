from numpy.polynomial import Polynomial
from numpy.polynomial import polynomial as P
import numpy as np
import matplotlib.pyplot as plt
import cmath;

p1=Polynomial.fromroots([complex(1, 2), complex(1,-2)])

aufgabe2_1_a=Polynomial([200, 2, 2])
print("Nullstellen A2_1_a: ", aufgabe2_1_a.roots())
print("Nullstellen A2_1_b: ", Polynomial([-25, 31,-7,1]).roots())