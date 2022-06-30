#!/usr/bin/env python3



#       This is program that does a few different things



#       a. Prompts the user for a non-zero angle in degrees

#       b. Continues to reprompt the user unless the input is acceptable

#       c. Prompts the user for a number, ≤ 25, of terms to sum in a series

#       d. Continues to reprompt the user unless the input is acceptable

#       e. Calculates, using a function you have defined called sind(), the sine of the angle

#       provided by the user. This function must sum a series to the number of terms

#       requested, and may not use any predefined Python math functions.

#       f. Calculates the sine of the angle using math.sin()

#       g. Prints out a quantitative comparison between the two answers including the ratio

#       and the absolute difference.


import math as m

#This is a function that can tell if a string is a float or not.

def isfloat(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

#A while loop that continues the prompt the users, unless they put in a 
#data type that can be turned into a float.
#I called the above function here to make the code easier to read.
#Further, within this while loop, I calculated the degrees into radians as
#soon as I could since I would be needed to work in them for the rest of the 
#the program. 

while True:
	prompt_1 = input('Please enter an angle in degrees you are interested in: ')
	q = isfloat(prompt_1)
	if q == True:
		radians = float(prompt_1)/180 * m.pi
		break

#I used the same structure of a while loop plus a conditional here as well,
#to get the user to input an integer for the length of the series.

while True:
	prompt_2 = input('Please enter a non-zero integer less than or equal to 25: ')
	if prompt_2.isdigit() == True:
		if int(prompt_2) <= 25:
			series_len = abs(int(prompt_2))
			break

#Since we are not using any pre built functions from python, I built my own 
#factorial function. Strictly speaking, if I was building a more general purpose
#factorial function I would disqualify negative number, but I already did this 
#in this while loop above. Ii did however define 0! = 1 though, to avoid a zero
#division error

def factorial(num):
	f = 1
	if num == 0:
		f == 1
	else:
		for i in range(1, num + 1):
			f = f * i
	return f

#This is the requested sind() function. It takes the users inputs and computes 
#the first 'prompt_2' terms of the sin(prompt_1) taylor series. It calls the 
#factorial function that was created above to keep the code cleaner 

def sind(rad, series_len):
	sin = 0
	for i in range(0, series_len, 1):
		n = 2*i+1
		sin = sin + (((-1)**(i))*(rad**(n))/(factorial(n)))
		print(sin)
	return sin


#Outputs


sin_me = sind(radians, series_len)
sin_math = m.sin(radians)

print("My sine function's output is "+str(sin_me))
print('\n')

print("Python's math module output is "+str(sin_math))
print('\n')

print("The ratio of my function's output over python's math module's is "+str(sin_me/sin_math))
print('\n')

abs_dif = abs(sin_me - sin_math)

print('The absolute difference between the two is '+str(abs_dif))
print('\n')

