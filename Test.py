import scipy.constants as sc
import matplotlib.pyplot as plt
from Spr import spread
import numpy as np
import math
import scipy.integrate as integrate

c = sc.c
m = sc.m_e
E = 250e6*sc.eV
eV = sc.eV

E = 250e6*eV
X = [1,1,1]
theta = [32.0, 35.0, 37.5, 40.0, 42.0, 44.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 54.0, 55.0, 56.0, 58.0, 60.0,
         64.0, 68.0, 72.0, 76.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 125.0]
sigma = [6.34E-1, 2.77E-1, 1.40E-1, 5.89E-2, 3.25E-2, 1.61E-2, 7.95E-3, 5.32E-3, 3.46E-3, 2.40E-3, 1.62E-3,
               1.19E-3, 8.27E-4, 5.38E-4, 4.71E-4, 4.32E-4, 4.50E-4, 4.82E-4, 4.54E-4, 3.24E-4, 2.11E-4, 1.18E-4,
               6.12E-5, 2.23E-5, 6.50E-6, 1.42E-6, 2.70E-7, 2.13E-7, 3.92E-7, 3.13E-7, 2.21E-7]
theta = np.array(theta)
theta = theta*math.pi/180
X = [6000,20000000000000000,300]
test = []

for x in range(len(theta)):
    test.append(spread(E,theta[x],X))
print(test)
plt.plot(theta,test,"o")
plt.plot(theta,sigma,"*")
plt.yscale('log')
plt.ylabel('some numbers')
plt.show()

'''
theta = 50
X = [1,1,1]
rho_ch0 = X[0]
a       = X[1]
b       = X[2]

hbar = sc.hbar
c = sc.c

v = math.sqrt(c**2-(m/E)**2*c**6)
beta = v/c
gamma = 1/math.sqrt(1-v**2/c**2)
p = m*v*gamma
#Beräkning
q = 2*p*math.sin(theta/2)
q=hbar

r = np.linspace(0,10,1000)
f = np.zeros(len(r))
for i in range(len(r)):
    f[i] = r[i]*(rho_ch0/(1+np.exp((r[i]-a)/b)))*math.sin(q*r[i]/hbar)
plt.plot(r,f)
plt.show()
f = lambda r: r*(rho_ch0/(1+np.exp((r-a)/b)))*math.sin(q*r/hbar)
Int, error = integrate.quad(f, 0,np.inf)
print(Int)
'''