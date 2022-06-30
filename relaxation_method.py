#!/usr/bin/env python3

# This program approximates a simple parallel plate capacitor
# given a static arrangement. The light portion is positive and
# the dark portion is negative. You can see the even very close to 
# the edges it approximates to an infinte parallel plate capacitor
# rather quickly

# What is most interesting about this program is that is able to 
# solve any static pototential given sufficient boundary conditions.

# WIlliam Murphy
# 01Jun22

import time
import numpy as np
import matplotlib.pyplot as plt


# Initial Parameters of the space

ITER = 60000 # Number of iteration for relaxation

GRID = 600 # number of units for square grid

P_WI = 0.05 # Plate Thickness

P_TH = 0.05 # plate width as fraction of grid size 

GAP  = 2.0 * P_WI # Plate Gap as a fraction of grid size, 
#                   and equal to plate width

VOLT = 10.0  

off_set = 17

# __Geometry of the capacitors is established__
#
# Width of Electrodes (Defined as the difference between two points)
clx = int(0.5*GRID*(1.0 - P_TH)) # Left side limit
crx = GRID - clx #Right side limit

# Gap
cap_th = (2.0* GAP) *GRID

# Left Electrode
ctT = int(0.5*(GRID - cap_th)) # The top capacitors top
cbT = int(ctT + GRID * P_WI) # The top capacitors bottom

# Bottom Elctrode
#ctB = int(0.5*(GRID + cap_th)) - off_set

ctB = int(ctT + GRID * (GAP + P_WI)) - off_set # The bottom capacitors top
#cbB = int(ctB + GRID * P_WI)

cbB = GRID - ctT - off_set # The bottom capacitors bottom

# Initial Matrix
A = np.zeros((GRID, GRID))

# Voltage is put on the plate
A[ctT:cbT, clx:crx] = -VOLT #Top capacitor is negative voltage
A[ctB:cbB, clx:crx] = VOLT #Bottom capacitor is positive voltage

#_______________________________________________

# This function computes each point by averaging the 
# points above, below and on each side via the roll() 
# method. It then redefines the boundary conditions 
# explicitly, via slicing.

#def roll_avg(A):
for i in range(ITER):
    
    # Averaging via np.roll
    A = (np.roll(A, -1, axis=0)+np.roll(A, 1, axis=0)+np.roll(A, -1, axis=1)+np.roll(A, 1, axis=1))/4

    # Reset the Boundary Conditions
#   ___________________________________________

    # The electrodes
    A[ctT:cbT, clx:crx] = +VOLT #Top 
    A[ctB:cbB, clx:crx] = -VOLT*3 #Bottom

    # The edges
    A[0] = 0
    A[GRID-1] = 0
    A[:,0] = 0
    A[:,GRID - 1] = 0 

#    return b

# For loop that implements the relaxation method

#for i in range(ITER):
#    A = roll_avg(A)


# _______Plotting_______
fig, ax = plt.subplots()

x = 0.3 * GRID
y = 0.94 * GRID

ax.set_title('Approximation of a Dipole')
ax.axis('off')
ax.text(x, y,'''-Orange is 0 voltage
    -Light is positive
    -Dark is negative''')
ax.imshow(A, interpolation='none', cmap='CMRmap')
plt.show()


