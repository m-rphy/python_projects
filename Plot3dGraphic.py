#!/usr/bin/env python3

# Author -- William Murphy
# Date   -- 04May2022


# Plotting the function z(x,y) = sin(x)cos(y)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# Compute z_func to make the surface.
def func_z(x,y):
	 return np.sin(x)*np.cos(y)

#Define the space we are solving for z
x = np.linspace(0, 5*np.pi, 900)
y = np.linspace(0, 5*np.pi, 900)

#Creating amesh grid for the points in the set z
X, Y = np.meshgrid(x, y)
Z = func_z(X, Y)


#Making the 3D space
fig = plt.figure()
ax = plt.axes(projection="3d")

#Setting labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('z(x,y)=sin(x)cos(y)')

#The requested method - plot_surface()
ax.plot_surface(X,Y,Z, cmap='cividis')

plt.show()

