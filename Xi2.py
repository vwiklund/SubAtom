from Spr import spread
import numpy as np
import math
import scipy.constants as sc
from Reimann import Riemann_sum

theta = [32.0, 35.0, 37.5, 40.0, 42.0, 44.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 54.0, 55.0, 56.0, 58.0, 60.0, 64.0, 68.0, 72.0, 76.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 125.0]
sigma = [6.34E-1, 2.77E-1, 1.40E-1, 5.89E-2, 3.25E-2, 1.61E-2, 7.95E-3, 5.32E-3, 3.46E-3, 2.40E-3, 1.62E-3, 1.19E-3, 8.27E-4, 5.38E-4, 4.71E-4, 4.32E-4, 4.50E-4, 4.82E-4, 4.54E-4, 3.24E-4, 2.11E-4, 1.18E-4, 6.12E-5, 2.23E-5, 6.50E-6, 1.42E-6, 2.70E-7, 2.13E-7, 3.92E-7, 3.13E-7, 2.21E-7]
error = [0.45E-1, 0.20E-1, 0.10E-1, 0.35E-2, 0.30E-2, 0.10E-2, 0.80E-3, 0.50E-3, 0.25E-3, 0.25E-3, 0.15E-3, 0.10E-3, 0.40E-4, 0.40E-4, 0.50E-4, 0.30E-4, 0.45E-4, 0.30E-4, 0.30E-4, 0.25E-4, 0.15E-4, 0.10E-4, 0.40E-5, 0.15E-5, 0.45E-6, 0.10E-6, 0.35E-7, 0.25E-7, 0.45E-7, 0.55E-7, 0.30E-7]
theta = np.array(theta)
sigma = np.array(sigma)
error = np.array(error)
theta = theta*math.pi/180
E = 250e6*sc.eV
def Xi2(X):
    Sum = 0
    Intervall = [0, 50, 100]

    Z_t = 20
    eps = 1e-6
    f = lambda r: r ** 2 * (X[0] / (1 + np.exp((r - X[1]) / X[2])))
    Int = Riemann_sum(f, Intervall[0], Intervall[1], Intervall[2])
    Condition = ((Z_t - 4 * np.pi * Int / eps) / eps) ** 2

    for x in range(len(theta)):
        Sum = Sum + ((spread(E,theta[x],X)-sigma[x])/error[x])**2
    return Sum+Condition