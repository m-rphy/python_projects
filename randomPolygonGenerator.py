#!/usr/bin/env python3

#Written for generating vector graphics

import matplotlib.pyplot as plt
import matplotlib.path as pth
import numpy as np

def angleBetweenPoints(p1, p2):
	"""
	angleBetweenPoints(p1,p2): Find the angle of the vector pointing from point p1 to p2.
	Returns: angle in radians
	p1: 2d tuple or list specifying a point (x,y)
	p2: The second point, same format.
	"""

	#Pretty much just simple trig here.
	#If slope is infinite don't use trig and just set it to avoid dividing by 0.
	if (p2[0]-p1[0] != 0):
		slope = (p2[1]-p1[1])/(p2[0]-p1[0])
		angle = np.arctan(slope)
		if (p2[0] < p1[0]):
			angle += np.pi
	else:
		angle = np.pi/2

	return angle

def getLineParameters(p1,p2):
	returnList = [0,0]
	if (p1[0] == p2[0]):
		returnList[0] = "vertical"
		returnList[1] = p1[0]
	else:
		returnList[0] = (p2[1] - p1[1])/(p2[0]-p1[0])
		returnList[1] = 0.5*((p1[1] + p2[1]) - returnList[0]*(p1[0] + p2[0]))
	return returnList

def find_outer_stroke(pointArray, lineWidth):
	lineParameters = []
	angles = []

	for i, x in enumerate(pointArray):
		if i == len(pointArray) -1:
			lineParameters.append(getLineParameters(pointArray[i],pointArray[0]))
			angles.append(angleBetweenPoints(pointArray[i],pointArray[0]))
		else:
			lineParameters.append(getLineParameters(pointArray[i], pointArray[i+1]))
			angles.append(angleBetweenPoints(pointArray[i],pointArray[i+1]))

	transformVectors = []

	transformedLineParameters = []
	for i, x in enumerate(lineParameters):
		print([-1*(lineWidth / 2) * np.cos(angles[i]),(lineWidth / 2) * np.sin(angles[i])])
		transformVectors.append([(lineWidth / 2) * np.sin(angles[i]),-1*(lineWidth / 2) * np.cos(angles[i])])
		transformedLineParameters.append(transformLine(lineParameters[i], transformVectors[i]))
	print(angles)
	intersectPoints = np.zeros((len(transformedLineParameters),2))
	for i, x in enumerate(transformedLineParameters):
		if i == len(transformedLineParameters) -1:
			intersectPoints[i] = findLineIntersection(transformedLineParameters[i], transformedLineParameters[0])
		else:
			intersectPoints[i] = findLineIntersection(transformedLineParameters[i],transformedLineParameters[i+1])

	return intersectPoints

def findInnerStroke(pointArray, lineWidth):
	lineParameters = []
	angles = []

	for i, x in enumerate(pointArray):
		if i == len(pointArray) -1:
			lineParameters.append(getLineParameters(pointArray[i],pointArray[0]))
			angles.append(angleBetweenPoints(pointArray[i],pointArray[0]))
		else:
			lineParameters.append(getLineParameters(pointArray[i], pointArray[i+1]))
			angles.append(angleBetweenPoints(pointArray[i],pointArray[i+1]))

	transformVectors = []

	transformedLineParameters = []
	for i, x in enumerate(lineParameters):
		transformVectors.append([-1*(lineWidth / 2) * np.sin(angles[i]),(lineWidth / 2) * np.cos(angles[i])])
		transformedLineParameters.append(transformLine(lineParameters[i], transformVectors[i]))

	intersectPoints = np.zeros((len(transformedLineParameters),2))
	for i, x in enumerate(transformedLineParameters):
		if i == len(transformedLineParameters) -1:
			intersectPoints[i] = findLineIntersection(transformedLineParameters[i], transformedLineParameters[0])
		else:
			intersectPoints[i] = findLineIntersection(transformedLineParameters[i],transformedLineParameters[i+1])

	return intersectPoints

def transformLine(parameters, transformVector):
	returnList = [0,0]
	if parameters[0] != "vertical":
		returnList[0] = parameters[0]
		returnList[1] = parameters[1] + transformVector[1] - parameters[0]*transformVector[0]
	else:
		returnList = ["vertical",parameters[1]+transformVector[0]]
	return returnList

def findLineIntersection(parameters1, parameters2):
	intersectPoint = np.zeros(2)
	if (parameters1[0] == "vertical"):
		intersectPoint[0] = parameters1[1]
		intersectPoint[1] = parameters2[0]*intersectPoint[0] + parameters2[1]
	elif (parameters2[0] == "vertical"):
		intersectPoint[0] = parameters2[1]
		intersectPoint[1] = parameters1[0]*intersectPoint[0] + parameters1[1]
	else:
		intersectPoint[0] = (parameters2[1] - parameters1[1])/(parameters1[0] - parameters2[0])
		intersectPoint[1] = parameters1[0] * intersectPoint[0] + parameters1[1]

	return intersectPoint


##############################################################################################################################

#Dimensions for canvas, taken from rt345.eps
X = 512
Y = 409

#Define colors
white = (0xff, 0xff, 0xff)
blue = (0x00, 0x00, 0xff)

#Array for color values. Initialize to white.
pvals = np.full((X,Y,3), 0xff, dtype='uint8')

#Points for triangle. Note that eps file defines offset of [58,58] when drawing points on line 23
#In principle this code should work for general points, although I will not be testing it thoroughly on anything but the provided.
p1 = (58, 58)
p2 = (458, 58)
p3 = (458, 358)

lineWidth = 20

scaleFactor = 0.1

pointArray = np.array([[p1[0],p1[1]],[p2[0],p2[1]],[p3[0],p3[1]]],dtype=np.int32)

outerStrokePoints = findOuterStroke(pointArray, lineWidth)

innerStrokePoints = findInnerStroke(pointArray, lineWidth)

print(outerStrokePoints)

outerPath = pth.Path(outerStrokePoints)

innerPath = pth.Path(innerStrokePoints)

for i, x in enumerate(pvals):
	for j, y in enumerate(x):
		if (outerPath.contains_point((i,j))) and not innerPath.contains_point((i,j)):
			pvals[i,j] = blue

#Transpose to proper format for drawing
plotarr = np.flipud(pvals.transpose(1,0,2))

fig, ax = plt.subplots()
picture = ax.imshow(plotarr, interpolation='none')
ax.axis('off')
fig.show()
fig.canvas.draw()
input("\nPress <Enter> to exit...\n")