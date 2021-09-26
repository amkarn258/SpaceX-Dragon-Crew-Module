# -*- coding: utf-8 -*-
"""ex4_code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fvh8lrsykTlZxXZSv5Mbhke4OAWfpNNx
"""

import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from scipy.optimize import *

l2=10
l1=5
l3=7
k=7
L=8
l21=10
m2=6
m3=9
m4=7
M=20
x4=list()
x2=list()
x3=list()
x4dot=list()
x2dot=list()
x3dot=list()
x4ddot=list()
x2ddot=list()
x3ddot=list()
l4=[]
y4=list()
y2=list()
y3=list()
y4dot=list()
y2dot=list()
y3dot=list()
y4ddot=list()
y2ddot=list()
y3ddot=list()
theta=list()
theta2=list()
theta3=list()
theta4=list()
theta2d=list()
theta3d=list()
theta4d=list()
theta2dd=list()
theta3dd=list()
theta4dd=list()
t=np.linspace(0.1,20,200)

for i in range(0,len(t)):
  theta2.append(k*t[i])
  theta2d.append(k)
  theta4.append(k*t[i])
  theta4d.append(k)
  theta4dd.append(0)
  theta2dd.append(0)
  theta.append(k)

for i in range(0,len(t)):
  theta3.append(theta2[i]-np.arcsin((l1/l3)*np.sin(theta2[i])))
  l4.append(l2+l3*np.sin(theta3[i])/np.sin(theta2[i]))
  theta3d.append((l2-l4[i])*np.cos(2*theta2[i])*k/(l3*np.cos(theta3[i]-theta2[i]))) 
  theta3dd.append((l2-l4[i])*((2*np.cos(theta2[i])**2-1)/2*(k)*l3*np.sin(theta3[i]-theta2[i])*(theta3d[i]-k)))

x3ddot=[]
for i in range(0,len(t)):
  x2.append(l2/2*np.cos(theta2[i]))
  x2dot.append(-l2/2*theta2d[i]*np.sin(theta2[i]))
  y2.append(l2/2*np.sin(theta2[i]))
  y2dot.append(l2/2*theta2d[i]*np.cos(theta2[i]))
  x3.append(l2*np.cos(theta2[i])+l3/2*np.cos(theta3[i]))
  x3dot.append(-l2*theta2d[i]*np.sin(theta2[i])-l3/2*theta3d[i]*np.sin(theta3[i]))
  y3.append(l2*np.sin(theta2[i])+l3/2*np.sin(theta3[i]))
  y3dot.append(l2*theta2d[i]*np.cos(theta2[i])+l3/2*theta3d[i]*np.cos(theta3[i]))
  x4.append(l2*np.cos(theta2[i])+l3*np.cos(theta3[i])+L/2*np.cos(theta4[i]))
  y4.append(l2*np.sin(theta[i])+l3*np.sin(theta3[i])+L/2*np.sin(theta4[i]))
  x2ddot.append(-l2/2*(np.cos(theta2[i])*(theta2d[i]**2)+np.sin(theta2[i])*theta2dd[i]))
  y2ddot.append(l2/2*(-np.sin(theta2[i])*(theta2d[i]**2)+np.cos(theta2[i])*theta2dd[i])
  x3ddot.append(-l2*(np.cos(theta2[i])*(theta2d[i]**2)+np.sin(theta2[i])*theta2dd[i])-l3/2*(np.cos(theta3[i])*(theta3d[i]**2)+np.sin(theta3[i])*theta3dd[i]))
  y3ddot.append(l2*(-np.sin(theta2[i])*(theta2d[i]**2)+np.cos(theta2[i])*theta2dd[i])+l3/2*(-np.sin(theta3[i])*(theta3d[i]**2)+np.cos(theta3[i])*theta3dd[i]))
  x4ddot.append(-l2*(np.cos(theta2[i])*(theta2d[i]**2)+np.sin(theta2[i])*theta2dd[i])-l3*(np.cos(theta3[i])*(theta3d[i]**2)+np.sin(theta3[i])*theta3dd[i])-L/2*(np.cos(theta4[i])*(theta4d[i]**2)+np.sin(theta4[i])*theta4dd[i]))
  y4ddot.append(l2*(-np.sin(theta2[i])*(theta2d[i]**2)+np.cos(theta2[i])*theta2dd[i])+l3*(-np.sin(theta3[i])*(theta3d[i]**2)+np.cos(theta3[i])*theta3dd[i])+L/2*(-np.sin(theta4[i])*(theta4d[i]**2)+np.cos(theta4[i])*theta4dd[i]))

for x in range(0,len(t)):
  A1=[1,0,np.sin(theta2[x]),0,0,0,0,0,0]
  A2=[0,1,-np.cos(theta2[x]),0,0,0,0,0,0]
  A3=[1,0,-np.sin(theta2[x]),-1,0,-np.sin(theta2[x]),0,0,0]
  A4=[0,1,np.cos(theta2[x]),0,-1,np.cos(theta3[x]),0,0,0]
  A5=[0,0,0,1,0,-np.sin(theta3[x]),-1,0,(l4-L/2)*np.sin(theta4[x])]
  A6=[0,0,0,0,1,np.cos(theta3[x]),0,-1,-(l4-L/2)*np.cos(theta4[x])]
  A7=[0,0,0,0,0,0,1,0,L/2]
  A8=[0,0,0,0,0,0,0,1,-L/2]
  A9=[np.cos(theta[x]),np.sin(theta[x]),(1-2*l21/l2)*np.cos(theta[x])(np.sin(theta2[x])-np.cos(theta2[x])),0,0,0,0,0,0]
  B=[m2*x2dot[x],m2*(y2ddot[x]+g),m2*l2/6*theta2dd[x],m3*x3ddot[x],m3*(y3ddot[x]+g),m3*l3/6*theta3dd[x],m4*x4ddot[x],m4*x4ddot[x]+(M+m4)*g,m4*(L**2)/12*theta4dd[x]+m*g*L/2*np.cos(theta4[x])]
  A=[A1,A2,A3,A4,A5,A6,A7,A8,A9]
  X=np.linalg.inv(A)
  R=np.dot(B,X)

plt.plot(R[0],t)
plt.show()

