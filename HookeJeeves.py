# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
def f(x1,x2):
    return x1**2 + (x2+0.5)**4 - (x2 - 1)**3
dokladnosc = 0.0000001
eps = 0.001

x1, x2 = np.random.uniform(-10, 10, 2)

f1 = f(x1,x2)
fprev = 100000000
while True:
    if f(x1 + eps, x2) < f1:
        x1 = x1 + eps
        f1 = f(x1, x2)
    elif f(x1 - eps, x2) < f1:
        x1 = x1 - eps
        f1 = f(x1, x2)
    elif f(x1 , x2 + eps) < f1:
        x2 = x2 + eps
        f1 = f(x1, x2)
    elif f(x1 , x2 - eps) < f1:
        x2 = x2 - eps
        f1 = f(x1, x2)
    else:
        x1, x2 = np.random.uniform(-10, 10, 2)
    if np.abs(f1 - fprev) < dokladnosc:
        break
    else:
        fprev = f1
    print(x1,x2)
        

        