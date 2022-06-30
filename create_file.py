#!/usr/bin/env python3

# 		This is a program that creates a file containing two 
#		user-provided strings,one per line.
#
#		Author -> Billy Murphy 12 April 2022


#This is the first prompt asking for the name of the text file
file_name = input('What would you like to name your text file: ')

#This line creates a file using the given file name and allows the program to write to it.
fname = open(str(file_name), "w")

#These next four lines of code prompt the user for the two strings
print('What is the first string?')
str_1 = input()

print('What is the second string?')
str_2 = input()

#The two strings are then saved into a list with 2 entries
#string one plus a new line character,
#and string two, with another new line character 
L = [str(str_1)+'\n', str(str_2)+'\n']

#This line writes the list of string, list L, to the text file
fname.writelines(L)

#In order to let the user confirm that the program ran properly.
#A print statement is given confirming 
print('The text file '+str(file_name)+' is now in your current working directory')

#This line closes the file
fname.close()

