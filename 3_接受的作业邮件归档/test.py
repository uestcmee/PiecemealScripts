import re

list=['fe','dioa','abc']
a='nihoa1244567dioawue123'
for l in list:
    name=re.search(l,a)
    if name!=None:
        print(name.group())
        break
    else:
        pass
