import math
import numpy as np
import scipy.constants as sc
from Reimann import Riemann_sum
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def spread(E, theta, X):
    #Input
    rho_ch0 = X[0]
    a       = X[1]
    b       = X[2]

    # Givet från PM
    Zp = 1
    Zt = 20

    # Fysikaliska konstanter
    alpha = sc.alpha
    hbar = sc.hbar
    c = sc.c
    e = sc.e
    m = sc.m_e

    v = math.sqrt(c**2-(m/E)**2*c**6)
    beta = v/c
    gamma = 1/math.sqrt(1-v**2/c**2)
    p = m*v*gamma
    #Beräkning
    Intervall = [0, 1000, 100000000]
    q = 2*p*math.sin(theta/2)
    f = lambda r: r*(rho_ch0/(1+np.exp((r-a)/b)))*math.sin(q*r/hbar)
    Int = Riemann_sum(f,Intervall[0],Intervall[1],Intervall[2])
    #Int, error = integrate.quad(f, 0,np.inf)
    F = 4*np.pi*hbar/(Zt*e*q)*Int
    dSigmadOmega = (Zp**2*Zt**2*alpha**2*(hbar*c)**2)/(4*beta**4*E**2*math.sin(theta/2)**4)*(1-beta**2*math.sin(theta/2)**2)*abs(F)**2
    print(dSigmadOmega)
    #print("beta = ", beta,"dSigmadOmega = " ,dSigmadOmega, "Error integral", error)
    return dSigmadOmega
