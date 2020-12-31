import re
match = "\w+,\s(\w)?"
m = re.match(match, "Ndubuisi, I",re.I).group()
print(m)
