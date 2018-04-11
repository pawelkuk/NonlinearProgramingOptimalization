# -*- coding: utf-8 -*-
import sys
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 50*(x[1]-x[0]**2)**2+(1-x[0])**2

def gradf(x, eps):
    grad = []
    for i in range(len(x)):
        epsilon = np.zeros(len(x))
        epsilon[i] = eps
        
        
        grad.append((f(x + epsilon) - f(x - epsilon))/(2*eps))
    return grad    
    
dokladnosc = 0.00000001
delta = 0.004    
eps = 0.00001
p = np.random.uniform(-1, 2, 2)
#p = np.array([1.5,1.5])
print(p)

x = []
y = []
z = []


i = 0

while True:
    x.append(p[0])
    y.append(p[1])
    z.append(7)
    grad = gradf(p, eps)
    p[i%2] = p[i%2] - grad[i%2] * delta
    i = i + 1
    if abs(np.array(grad)).sum() < dokladnosc:
        break
    
print("liczba krokow: ",i)
print(p)








# interpolate onto a 100x100 regular grid
d = 2
X, Y = np.mgrid[-d:d:100j, -d+1:d+1:100j]
Z = f(np.array([X.ravel(), Y.ravel()])).reshape(X.shape)
fig, ax = plt.subplots(1, 1)
ax.set_aspect('equal')
m = ax.contour(X, Y, Z, 30, cmap=plt.cm.Greens)
ax.scatter(x, y, s=z)#, s=60, cmap=m.cmap, vmin=m.vmin, vmax=m.vmax)
fig.tight_layout()
plt.show()