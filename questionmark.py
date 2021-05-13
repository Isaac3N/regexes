#the question mark character in regex allows you to match a preceeding character zero or 1 times 

import re 
bat_regex =  re.compile(r'Bat(wo)?man')
match_object = bat_regex.search('The adventures of Batwoman')
print(match_object.group())

