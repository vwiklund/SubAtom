import math
import numpy as np
import scipy.constants as sc

def spread(E, theta, X):
    # Fysikaliska konstanter
    alpha = sc.alpha
    hbar = sc.hbar
    c = sc.c

    #input
    E = E
    theta = theta
    X = X
    v = math.sqrt(-(m/E)**2*c**6+c**2)
    beta = v/sc.c

    #Givet från PM
    Zp=1
    Zt=20

    #Beräkning
    dSigmadOmega = (Zp**2*Zt**2*alpha**2*(hbar*c)**2)/(4*beta**2*E**2*math.sin(theta/2)**4)
    return dSigmadOmega
c = sc.c
m = sc.m_e
E = 250e6*sc.eV
eV = sc.eV
print(E)
print(m*c**2)
print(math.sqrt(E-m*c**2)*2/m)
print(c)
print(math.sqrt(-(m/E)**2*c**6+c**2))
print(spread(250e6*eV,50,1))
