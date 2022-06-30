#!/usr/bin/env python3


#	This program does...
#
#	a. Prompts the user for a date in the form DDMmmYYYY. For example, 26Apr2016.
#
#	b. Computes and prints the Julian day number corresponding to 0 h universal time
#	on the selected date
#
#	c. Computes and prints the day of the week on which the selected date falls.
#
#	---Also, there are functions that are defined for each of the following tasks.
#	
#	a. Prompt the user and return his/her input string
#
#	b. Parses the input string and returns a list containing the year,
#		month (1-12), and the day of the month.
#	
#	c. Compute the Julian day number using the list returned by the function from 
#		the previous functions output	
#
#	d. Computes the day of the week given the julian day number
#
#

#These are refrence lists and dictionaries for various parts of the code.

month_abb = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days_of_week_dict = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
month_code_dict = {'Jan':0,'Feb':3,'Mar':3,'Apr':6,'May':1,'Jun':4,'Jul':6,'Aug':2,'Sep':5,'Oct':0,'Nov':3,'Dec':5}
cent_code_dict = {'17':4,'18':2,'19':0,'20':6,'21':4,'22':2,'23':0}
leap_years = [i for i in range(0,2404,4)]

#This function prompts the user, until the correct format is acheived.
#I used a while loop and a conditional to break the while loop
#The example provided provides clarity for any ambiguity for how to treate
#single digit days and the month of September (Sep vs Sept)

def prompt_user():
	while True:
		print('Please enter a date of the form, DDMmmYYYY')
		print('An example is: 02Sep2022')
		print('\n')
		prompt = input('Enter your date here: ') 
		print('\n')
		date_str = list(prompt)
		month_str = ''.join(date_str[2:5])	
		if month_str in month_abb and len(prompt) == 9:
			print(prompt)
			break
	return prompt

#This function parses the strings with join() and string indexing.
#This is why the above function keeps asking for a date given in the 
#correct format, since any other format would break this function.
#I output string versions of the year and month for another function that
#computes the days of the week in a different manner, not dependent on the julian day

def string_parser(prompt):
	date_str = list(prompt)
	day = int(''.join(date_str[:2]))
	month_str = ''.join(date_str[2:5])
	month_num = month_abb.index(month_str) + 1
	year_str = ''.join(date_str[5:])
	year = int(year_str)
	date_lst = [year, month_num, day]
	print(date_lst)
	return month_str, year_str, date_lst

#This is a function that computes the julian day with a formula.
#It takes the prompt to simply print it out next to the output
#of the computation so it is easier to read.

def JD_calc(date_lst, prompt):
	D = date_lst[2]
	if date_lst[1] > 2:
		M = date_lst[1]
		Y = date_lst[0]
		JD = int(365.25*(Y + 4716)) + int(30.6001*(M + 1)) + D -1524.5
	elif date_lst[1] <=2:
		M = date_lst[1] + 12
		Y = year-1
		JD = int(365.25*(Y + 4716)) + int(30.6001*(M + 1)) + D -1524.5
	print('The Julian Day of '+ prompt +' is: '+ str(JD))
	return JD

#This is a function that computes what day of the week it is,
#when given the julian day.

#-note, it is much easier to calculate the day of the week given the julian day
#than directly from the gregorian date

def what_day_jd(JD):
	day_code = (JD +1.5)%7
	week_day = days_of_week_dict.get(day_code)
	print('This is a '+str(week_day)+ '!')
	return

#This function calculates the day of a week given a specific gregorian date.
#I made reference dictionaries that are commented out at the top of this program.
#A nice thing about this function is that it does not depend on where you are in the
#in the world. If you know what the gregorian date of you are interested, it gives
#that date. It works too! The julian date calculator is a day early since it's
#relative to the time in England.

def what_day(day, month_str, year_str):
	YY = int(year_str[-2:])
	y_code = (YY+(YY//4))%7
	m_code = int(month_code_dict.get(month_str))
	yy = year_str[:2]
	yy_int = int(yy)
	if yy_int >= 17 or yy_int <=23:
		cent_code = int(cent_code_dict.get(yy))
	else:
		cent_code = 0
		print('Cannot Compute the day of this date. Sorry : (')
	if int(year_str) in leap_years and month_str in ['Jan', 'Feb']:
		ly_code = -1
	else:
		ly_code = 0
	day_code = (y_code + m_code + cent_code + ly_code + day)%7
	week_day = days_of_week_dict.get(day_code)
	return(print('This is a '+str(week_day)+ '!'))
	

#This is all the functions being called.

prompt = prompt_user()

month_str, year_str, date_lst = string_parser(prompt)

JD = JD_calc(date_lst, prompt)

#what_day(date_lst[2], month_str, year_str)

what_day_jd(JD)
