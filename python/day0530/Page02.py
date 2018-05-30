import re


data = """python one
life is too short
python two
you need python
python three
python4 last"""

sp = "^python"
# sp = "python$"
mlist = re.findall(sp, data, re.M)
print(mlist)
