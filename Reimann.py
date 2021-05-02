import numpy as np
def Riemann_sum(f, a, b, N):
    dx = (b-a)/N
    x = np.linspace(a, b, N)
    x_mid = (x[:-1] + x[1:]) / 2
    Int = np.sum(f(x_mid)*dx)
    return Int