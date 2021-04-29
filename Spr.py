import math
import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt


def spread(E, theta, X):
    #Input
    rh0_ch0 = X[0]
    a       = X[1]
    b       = X[2]

    # Fysikaliska konstanter
    alpha = sc.alpha
    hbar = sc.hbar
    c = sc.c


    v = math.sqrt(c2-(m/E)2c**6)
    beta = v/c

    #Givet från PM
    Zp=1
    Zt=20

    #Beräkning
    rho_ch = rho_ch0/(1+np.exp((r-a)/b)
    f = lambda r: rrho_chsin(qr/hbar)
    Int, error = integrate.quad(f, 0,np.inf)
    F = 4np.pihbar/(Zeq)Int
    dSigmadOmega = (Zp**2Zt2*alpha2(hbarc)2)/(4*beta2E**2math.sin(theta/2)4)*(1-beta2math.sin(theta/2)**2)
    print("beta = ", beta)
    return dSigmadOmega
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

for x in range(31):
  print("theta = ", theta[x], "\t \t \t sigma = ", sigma[x], "\t \t \t spr = ", spread(E,theta[x],X),"\t \t \t Procent", spread(E,theta[x],X)/sigma[x])


#plt.plot(theta,sigma,"*")
plt.yscale('log')
plt.ylabel('some numbers')
plt.show()

