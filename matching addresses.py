import re
ad= "(\d){4}\s[A-Za-z]\s[A-Za-z]+\."
m = re.match(ad,"11800 Bordeaux drive.").group()
print(m)
