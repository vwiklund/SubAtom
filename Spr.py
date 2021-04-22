import math
import numpy as np
import scipy.constants as sc

def spread(E, theta, X):
    #input
    E = E
    theta = theta
    alpha = 1
    beta = 1

    #Givet från PM
    Zp=1
    Zt=20

    #Fysikaliska konstanter
    hbar = sc.hbar
    c = sc.c
    dSigmadOmega = (Zp**2*Zt**2*alpha**2*(hbar*c)**2)/(4*beta**2*E**2*math.sin(theta/2)**4)
    return dSigmadOmega
