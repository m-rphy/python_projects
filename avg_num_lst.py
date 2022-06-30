#!/usr/bin/env python3
#
#		A program that reads numbers from a user-specified
#		file and prints out their average
#		note - input file requires one number per line

#		Author - Billy Murphy
#				12 April 2022


import numpy as np


#Prompting the user for the name of file to operate on.

fname = input('What is the file you would like to read: ')

#Reading the text file and returning the contents as a list.
#Each item of the list represents a line of the file.

infile = open(str(fname), 'r')
lines = infile.readlines()

#Because the output of lines is has the new line character
#a for loop is used to remove it from each item of of lines and 
#and appends the cleaned string to str_lst. This allows for numbers with
#more than one digit.

str_lst = []
for line in lines:
	i = line.rstrip("\n")
	str_lst.append(i)

#Because there is no string.isdigit() method, I am using a 
#a function that can tell if a sting is float or not.
#It has a simply True or False output and is used later.
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#This for loop populates a list that can be operatored on by numpy. Within this for loop
#are some conditionals statements that handle the different types of characters that are 
#possible. Namely letters, numbers, and special characters. I included this extra bit to make
#program robust to errors within the data it is analyzing. I don't want to rely on 
#the input data to be in a perfect format for the practical reason that often times real world
#data is quite messy.

num_lst = []
for i in str_lst :
		if i.isdigit() == True:
			num_lst.append(float(i))
		elif isfloat(str(i)) == True:
			num_lst.append(float(i))
		elif isfloat(str(i)) == False:
			print('ERROR: '+str(i)+' was skipped because it is not a number.')
		
#The program prints the average of the given file.
print('The average is: '+str(np.average(num_lst)))

#As an add feature to the program I made it so that if there is a mistake 
#in the original file, the code with skip over that entry and alert the user
#that there is an entry that was skipped.

#Closing the file. This may seem like a trivial comment, though for the sake of explination I am including this time. I the program did not close the file, there is all kinds of mysterious and troublesome problems that could arise from the leaving a file open. Most likely the file would become currupted. This would obviously be a terrible thing. To write a program that corrupts files is pretty much a fail. Especially since you might not notice it right away!
infile.close()
	
