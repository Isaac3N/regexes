#This is using regex for text pattern recognition 
import re 

message = 'Call me at 234-815-679-0029'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d-\d\d\d\d') # d stands for a digital value 
match_object= phoneNumRegex.search(message) #to search for values that contain that text pattern 
print(match_object.group()) 