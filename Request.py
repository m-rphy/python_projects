#!/usr/bin/env python3


import requests

r = requests.get('https://web.physics.ucsb.edu/~phys129/lipman/', auth=('user', 'pass'), headers={'Connection':'close'})

#Makng the html text a string
html_txt = str(r.text)

#Finding parsing the string for the desired line
begin_where = html_txt.find('Latest update')
end_where = html_txt.find('</p>')-7
update_str = html_txt[begin_where:end_where]

#Deleting the undesired text form the desired line
last_update = update_str.replace('<span class="greenss">','').replace('&nbsp;',' ')

print('')
print('Physics 129L '+last_update)
print('')
