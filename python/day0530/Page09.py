import re

def chfun(m):
    n = int(m.group())
    return hex(n)

data = 'call 6540 for printing, 49152 for user code.'

sp = r"\d+"

mlist = re.findall(sp, data)
print(mlist)
new_data = re.sub(sp, chfun, data)
print(new_data)
