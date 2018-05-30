import re

s = "park 010-1234-5678 ok"

sp = r"(\w+)\s(\d{3}[-]\d{4}[-]\d{4})"

m = re.search(sp,s)
name = m.group(1)
number = m.group(2)
namespan = m.span(1)
numbspan = m.span(2)
print(name,"/",namespan)
print(number,"/",numbspan)
# print("data",st)
# name = st.split()[0]
# number = st.split()[1]
# print(name)
# print(number)
