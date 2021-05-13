import re 
manRegex = re.compile(r'Man(kind|hood|ly|chester|y)')
match_object = manRegex.search('My Mankind was taken away from me from Manchester city. Now I do not Feel Manly anymore')
print(match_object.group(0))