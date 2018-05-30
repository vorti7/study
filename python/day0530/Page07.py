import re

s = "Paris in the the spring python is very very good language"

# sp = r"(\b\w+\b)\s(\b\w+\b)"
sp = r"(\b\w+)\s\1"

mlist = re.findall(sp,s)
print(mlist);
