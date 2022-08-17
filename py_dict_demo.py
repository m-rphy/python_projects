#!/usr/bin/env python3

# This is to demostrates my proficiency manipulating python dictionaries

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
updated_damages = []

for i in damages:
    if ('M' in i):
      i = i.replace('M','')
      updated_damages += [float(i)*conversion['M']]
    elif ('B' in i):
      i = i.replace('B','')
      updated_damages += [float(i)*conversion['B']]
    else:
      updated_damages += [i]
#print(updated_damages)

# test function by updating damages


def update_string_list(string_list):
  updated_string_list = []
  conversion = {'M': 1000000, 'B': 1000000000}
  for i in string_list:
    if ('M' in i):
      i = i.replace('M','')
      updated_string_list += [float(i)*conversion['M']]
    elif ('B' in i):
      i = i.replace('B','')
      updated_string_list += [float(i)*conversion['B']]
    else:
      updated_string_list += [i]
  return updated_string_list


# 2 
# Create a Table

# Create and view the hurricanes dictionary
hurricane = {}

def hurricane_dict_maker(name, month, year, max_sustained_wind, area_affected, death):
  for i in range(len(name)):
    hurricane[name[i]] = {'Name': name[i], 'Month': month[i], 'Year': year[i], 'Maximum Sustained Winds': max_sustained_wind[i], 'Area Affected': area_affected[i], 'Deaths': death[i]}
  return hurricane

hurricanes = hurricane_dict_maker(names, months, years, max_sustained_winds,areas_affected, deaths)
print(hurricanes)


# 3
# Organizing by Year

#this for loop takes the values for each key in hurricanes and makes a list of the dictionary values
# It also makes a list of the years that each hurricanes occured in 
years_of_hurricanes = []
hurricane_years = {}
hurricane_names_data = []
for name in hurricanes:
  hurricane_names_data.append(hurricane[name])
  years_of_hurricanes.append(hurricanes[name]['Year'])


#print(hurricane_names_data)
#print(years_of_hurricanes)


# create a new dictionary of hurricanes with year and key

# 4
# Counting Damaged Areas

def dict_by_year(hurricane_data):
  hurricanes_year = {}
  for cane in hurricanes:
      current_cane = hurricane_data[cane]
      if current_cane['Year'] not in hurricanes_year:
        hurricanes_year[current_cane['Year']] = current_cane
      elif current_cane['Year'] in hurricanes_year:
        multiple_cane = hurricanes_year[current_cane['Year']]
        hurricanes_year[current_cane['Year']] = [multiple_cane, current_cane]
  return hurricanes_year
hurricanes_year = dict_by_year(hurricanes)

#print(hurricanes_year[2005])

# create dictionary of areas to store the number of hurricanes involved in

# This loop takes in a dictionary with the names of the hurricanes as keys and the data 
# associacted with that hurricane as a dictionary value. Then it outputs a nested list 
# of the areas affected by each hurricane.

nested_list_of_affected_areas = []
for i in range(len(hurricane_names_data)-1):
  hurricane_i = hurricane_names_data[i]
  nested_list_of_affected_areas.append(hurricane_i['Area Affected'])

#this loop takes that nested list and converts it to a single list
affected_area_list = []
for areas in nested_list_of_affected_areas:
  for area in areas:
    affected_area_list.append(area)

#this loop createes a list of the affected areas
areas_affected = []
for area in affected_area_list:
  if area not in areas_affected:
    areas_affected.append(area)
#print(areas_affected)

#this function takes in a list of dictionary values associated with each hurricane and outputs 
# an other dictionary of the affected areas and the number of times it has been affected by a cat-5 hurricane
def count_affected_area(hurricane_data):
  affected_areas = []
  for i in range(len(hurricane_data)-1):
    hurricane_i = hurricane_names_data[i]
    affected_areas.append(hurricane_i['Area Affected'])
    count_affected_areas_dict = {}
    counted_area_list = []
    affected_area_list = []
  for areas in affected_areas:
    for area in areas:
      affected_area_list.append(area)
  for i in range(len(affected_area_list)):
      if affected_area_list[i] not in counted_area_list:
        count = 1
        count_affected_areas_dict[affected_area_list[i]] = count
        counted_area_list.append(str(affected_area_list[i]))
      if affected_area_list[i] in counted_area_list:
        count = affected_area_list.count(affected_area_list[i])
        count_affected_areas_dict[affected_area_list[i]] = count
  return count_affected_areas_dict

areas_affected_and_num = count_affected_area(hurricane_names_data)
#print(areas_affected_and_num)

# 5 
# Calculating Maximum Hurricane Count

#this function counts which area is affected by the most number of hurricanes
#takes in dictioanry: areas_affected_and_num and the list: affected_areas

def area_most_affected(areas_and_num):
   #assume a benchmark
  max_area_count = areas_affected_and_num[areas_affected[2]]
  most_affected_areas = {}
  for i in range(len(areas_affected)-1): #compare each entry to the benchmark
    area = areas_affected[i]
    area_count = areas_and_num[areas_affected[i]]
    if max_area_count <= area_count: #the benchmark
      max_area_count = area_count
      most_affected_areas[area] = area_count
  return most_affected_areas 


#a quick note, the above function doesn't compare quantities within a 
# dictionary and updates a dictionary it compares items of a list and 
# updates that dictionary. 

##print(areas_affected)
# find most frequently affected area and the number of hurricanes involved in

most_affected_areas_dict = area_most_affected(areas_affected_and_num)

print(most_affected_areas_dict)

# 6
# Calculating the Deadliest Hurricane

# This function sorts that hurricanes by name and deaths associated with each 
# hurricane using the list of data for each hurricane stored as a dictionary: 
# hurricane_names_data

#print(hurricane_names_data)


def name_and_death_dict_maker(hurricane_data):
  name_and_death_dict = {}
  for i in range(len(hurricane_data)-1):
    hurricane_i = hurricane_data[i]
    name_and_death_dict[hurricane_i['Name']] = hurricane_i['Deaths']
  return name_and_death_dict

name_and_death_dict = name_and_death_dict_maker(hurricane_names_data) 
#print(name_and_death_dict)



#this function makes a dictionary that includes the most deadliy hurricanes
def most_deadly_hurricane_finder(hurricane_data):
  hurricane_33 = hurricane_data[0]
  deaths_of_deadliest_cane = hurricane_0['Deaths']
  deadliest_canes = {}
  hurricane_name_list = []
  hurricane_deaths_list =[]
  for i in range(len(hurricane_data)-1):
    hurricane_i = hurricane_data[i]
    hurricane_i_names = hurricane_name_list.append(hurricane_i['Name'])
    hurricane_i_deaths = hurricane_deaths_list.append(hurricane_i['Deaths'])
    if deaths_of_deadliest_cane <= hurricane_i_deaths: 
      deaths_of_deadliest_cane = hurricane_i_deaths
      deadliest_canes[hurricane_name_list[i]] = hurricane_deaths_list[i]
  
  return deadliest_canes


deadliest_canes = most_deadly_hurricane_finder(hurricane_names_data)

print(hurricane_names_data)
print(deadliest_canes)