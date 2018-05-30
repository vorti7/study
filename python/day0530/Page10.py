import re

s = '<html><head><title>Title</title>'

sp = r"<.*>"
# sp = r"<.*?>"
m = re.search(sp,s)
print(m)
