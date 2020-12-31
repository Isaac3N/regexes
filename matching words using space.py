import re
words ="(\w+)\s(\w+)"
m = re.match(words, "Ndubuisi Chukwuemeka",re.I).group()
print(m)

