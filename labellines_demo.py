import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import loglaplace,chi2

from labellines import labelLine, labelLines
X = np.linspace(0, 1, 500)
A = [1, 2, 5, 10, 20]
funcs = [np.arctan, np.sin, loglaplace(4).pdf, chi2(5).pdf]
for a in A:
    plt.plot(X, np.arctan(a*X), label=str(a))

labelLines(plt.gca().get_lines(), zorder=2.5)
plt.show()