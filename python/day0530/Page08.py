import re

def fun(m):
    str = {"kim":"김","park":"박","lee":"이","kang":"강"}
    key = m.group().lower()
    try:
        s = str[key]
    except KeyError:
        s = key
    return s

data = """
park 010-1231-4213
kim 019-1523-3213
lee 017-5123-8982
ko 012-1123-1232
kang 018-373-2145
KIM 011-433-6632
"""

# sp = r"(\w)(\w+)\s(\d+)[-](\d+)[-](\d+)"

# mlist = re.findall(sp,data)
# print(mlist)

# new_data = re.sub(sp, "\g<1>*** \g<2>-xxxx-\g<4>", data)
# print(new_data)

sp = r"[a-z]+"
# mlist = re.findall(sp, data, re.I)
# print(mlist)

p = re.compile(sp, re.I)
new_data = p.sub(fun,data)
# new_data = re.sub(sp,"kkk",data,re.I)
print(new_data)
