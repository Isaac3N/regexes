import re
domain = "www\.\w+\.(com|net|edu)"
m = re.match(domain, "www.g332le.edu").group()
print(m)
