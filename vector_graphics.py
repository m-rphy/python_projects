#!/usr/bin/env python3


# This is a program that draws an isosceles triangle
# with vector graphics

import numpy as np
import matplotlib.pyplot as plt

# NOTE- These two lines set up two arrays
# pvals is -512 wide for the width of the plot
#		   -409 high for the heigth of the plot
#		   -3 cells deep for RGB values


#blue is an array that is sets the RGB to blue
pvals = np.ones((512, 409, 3), dtype='uint8')*255
blue = np.array([0,0,255], dtype='unit8')


# top-> outer edge
# bottom -> inner edge
 
def top_hyp(x):
	return((3/4)*x+32)

def bottom_hyp(x):
	return((3/4)*x+2)

#Conditionals set each pixel blue or it remains white
for i in range(len(pvals)):
	for j in range(len(pvals[0])):
		if 28 <= i <= 88 and 48 <= j <= top_hyp(i):
			pvals[i,j,:] = blue
		if 88 < i <= 448 and 48 <= j <= 68:
			pvals[i,j,:] = blue
		if 448 < i <= 468 and 48 <= j <= top_hyp(i):
			pvals[i,j,:] = blue
		if 88 < i <= 448 and bottom_hyp(i) <= j <= top_hyp(i):
			pvals[i,j,:] = blue

#rotating the array so it is in the correct orientation

np.flipud(pvals.transpose(1,0,2))
p = np.rot90(pvals, 1)


f1, ax1 = plt.subplots()
ax1.imshow(p, interpolation='none')
ax1.axis('off')
plt.show()
