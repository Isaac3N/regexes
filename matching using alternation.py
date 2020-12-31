import re
t= "bat|hut|hit|but|hat"
m = re.match(t,"hut").group()
print(m)
