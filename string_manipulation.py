#!/usr/bin/env python3

#
#		This is a program with several objectives
#
# a. Prompts the user for a string with at least 3 words
# b. Rejects the string and reprompts if the string has fewer than three words
# c. Prints the words in the string, one per line
# d. Prints the first three characters of the string
# e. Prints the last three characters of the string 
#		(not counting the newline character)
# f. Prints the first half of the string 
#		(include any characters on the boundary)
# g. Prints the last half of the string 
#		(include any characters on the boundary)
# h. Prints the string with the words in reverse order
# i. Prints the string with the words alphabetized
# j. Prints each character in the string, one per line
# k. Prints hexadecimal values for each character in the string,
#	 one line per character
#
#		Author - Billy Murphy 12 April 22
#

# This while loop is both objective a & b
while True:
	word_str = input('Please enter a string that is at least 3 words long: ')
	i_lst = word_str.rsplit(' ') 
	if len(i_lst) >= 2:
		word_lst = word_str.rsplit(' ')
		break

#Objectives a and b are intimately linked since b depends on a reprompting. I chose to not 
#change the prompt after it was rejected, since the directions for the kind of string the
#the program is asking is already quite clearly stated in the opening prompt. I chose two 
#to use the split method since words are seperated by a space. This seems like a simple and
#clear way of solving the problem and sets up the string in a useful data type for the later 
# objectives.


#Side note -- These print statements are used for debugging and making the output more easily
#understood by however is running the program. Hope it helps you too!

print('\n')
print('The prompt was Objective A & B')
print('\n')
print('Objecive C'+'\n')



# Objective c
for word in word_lst:
	print(str(word))

#The new line character is automatically adding when using a for loop

print('\n')

# Objective d - The 3 is exclusive where as the 0 is inclusive

print('Objective D'+'\n')
print(word_str[0:3])

#I used string parsing with the original string. The 3 is exclusive and the 0 is inclusive.

print('\n')

# Objective e

print('Objective E'+'\n')
print(word_str[-3:])

#I used string parsing on the original string again, not saying start from the negative 3 position

print('\n')
print('Objective F'+'\n')

# Objective f
first_half = int((len(word_str)/2))
print(word_str[:first_half])

# Using string parsing on the orginal string again, only now calculating the middle of the string
#before parsing. I am including the spaces as part of the string. 

print('\n')
print('Objective G'+'\n')

# Objective g
last_half = int((len(word_str)/2))
print(word_str[last_half:])

#This is almost the same as the objective above, only where we start and stop has changed

print('\n')
print('Objective H'+'\n')

# Objective h
reverse_lst = word_lst[::-1]
for i in reverse_lst:
	print(i)

#I made a new list and used the reverse order syntax --> lst[::-1] and then printed the new list 
#with a for loop.

print('\n')
print('Objective J'+'\n')

# Objective j

for word in word_lst:
	for char in word:
		print(char)
#using a nested loop to loop through each character in each word and printing it to a new line. 
#Omitting the spaces, though I could of just of easily used a single for loop to loop through each
#character of the string as well.

print('\n')
print('Objective K'+'\n')

# Objective k
for word in word_lst:
    for char in word:
        print(ord(char))

#Using the built in function of ord(), i looped through the list of words and printed out the 
#hexidecimal value for each word. Again I could of looped through a list of each character
#and dones the same,though there was some ambiguity as to what was correct and I chose this method.







