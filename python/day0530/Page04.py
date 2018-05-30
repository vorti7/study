import re

s = "java testpython1 scala python test python"

sp = r"\bpython\b"
mlist = re.findall(sp, s)
print(mlist)
