import re

s = "music\sport\movie"

sp = r"sport"
mlist = re.findall(sp,s)
print(mlist)
