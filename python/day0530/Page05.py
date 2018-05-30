import re

s = "python ABCABCABC ok"

sp = "(ABC)+"
mlist = re.search(sp, s)
print(mlist)
