#This is using regex for text pattern recognition 
import re 

message = 'Call me at (234)-815-679-0029 or 234-815-889-2782'
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d-\d\d\d\d)') # d stands for a digital value 
match_object= phoneNumRegex.search(message) #to search for values that contain that text pattern 
# match_object1= phoneNumRegex.findall(message) # to get every every occurrence of the text pattern
# print(match_object1) 
print(match_object.group()) 