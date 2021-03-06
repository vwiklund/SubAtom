import math
import numpy as np
from Spr import spread
from Reimann import Riemann_sum
import matplotlib.pyplot as plt
import scipy.constants as sc
from Xi2 import Xi2
import scipy.optimize as op

#Given data
theta = [32.0, 35.0, 37.5, 40.0, 42.0, 44.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 54.0, 55.0, 56.0, 58.0, 60.0, 64.0, 68.0, 72.0, 76.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 125.0]
sigma = [6.34E-1, 2.77E-1, 1.40E-1, 5.89E-2, 3.25E-2, 1.61E-2, 7.95E-3, 5.32E-3, 3.46E-3, 2.40E-3, 1.62E-3, 1.19E-3, 8.27E-4, 5.38E-4, 4.71E-4, 4.32E-4, 4.50E-4, 4.82E-4, 4.54E-4, 3.24E-4, 2.11E-4, 1.18E-4, 6.12E-5, 2.23E-5, 6.50E-6, 1.42E-6, 2.70E-7, 2.13E-7, 3.92E-7, 3.13E-7, 2.21E-7]
error = [0.45E-1, 0.20E-1, 0.10E-1, 0.35E-2, 0.30E-2, 0.10E-2, 0.80E-3, 0.50E-3, 0.25E-3, 0.25E-3, 0.15E-3, 0.10E-3, 0.40E-4, 0.40E-4, 0.50E-4, 0.30E-4, 0.45E-4, 0.30E-4, 0.30E-4, 0.25E-4, 0.15E-4, 0.10E-4, 0.40E-5, 0.15E-5, 0.45E-6, 0.10E-6, 0.35E-7, 0.25E-7, 0.45E-7, 0.55E-7, 0.30E-7]
theta = np.array(theta)
sigma = np.array(sigma)
error = np.array(error)
theta = theta*math.pi/180

#Constants
E = 250e6*sc.eV
r = 1
Z_t = 20
Intervall=[0,1000,100000000]
#Changeble variables
a = 1
b = 1
rho_0 = 1
X = np.array([a, b, rho_0])


X = [100,10,1000000]
'''
test = []
Xi = np.zeros(len(theta))
for x in range(len(theta)):
    test.append(spread(E,theta[x],X))
    Xi[x] = ((spread(E,theta[x],X)-sigma[x])/error[x])**2
#print(test)
plt.plot(theta,test,"o")
plt.plot(theta,sigma,"*")
plt.yscale('log')
plt.ylabel('some numbers')
plt.show()
'''

print(Xi2(X))
res = op.minimize(Xi2,[9,1000,1])
print(res)