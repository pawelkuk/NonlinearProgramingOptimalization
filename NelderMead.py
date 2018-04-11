# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x[0]**2 +x[1] ** 2 - x[1]**3 + (x[1]-2)**4

history = []


dokladnosc = 0.000000001
eps = 0.001

alpha = 0.5
beta = np.linspace(0.9, -0.9, 10)

points = np.random.uniform(-10, 10, (3,2))
minpoint = [10000,10000]
maxpoint = [-10000,-10000]

history.append(points[1])
history.append(points[2])
history.append(points[0])

step = 0
print(points)

while True:
   step = step + 1
   maxval = max(f(points[0]),f(points[1]),f(points[2]))
   minval = min(f(points[0]),f(points[1]),f(points[2]))
   for i in range(3):
       if maxval == f(points[i]):
           c = (points[(i+1)%3] + points[(i+2)%3])/2
           for b in beta:
               if f(points[i]) > f(c + b*(c-points[i])):
                   points[i] = c + b*(c-points[i])
                   
                   history.append(points[i])
                   break
   cc = (points[0] + points[1] + points[2])/3
   odl0 = (points[0][0]-cc[0])**2 +(points[0][1]-cc[1])**2 
   odl2 = (points[2][0]-cc[0])**2 +(points[2][1]-cc[1])**2 
   odl1 = (points[1][0]-cc[0])**2 +(points[1][1]-cc[1])**2 
   if max(odl1,odl2,odl0) < dokladnosc:
       break
print(step)
print((points[0] + points[1] + points[2])/3)
his = np.array(history).T
plt.plot(his, 'r.')