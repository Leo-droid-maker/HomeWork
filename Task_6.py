from itertools import count, cycle

LIST = []
for i in count(3):
    if i > 10:
        break
    else:
        LIST.append(i)

print(LIST)

count = 1
for el in cycle(LIST):
    if count > len(LIST):
        break
    else:
        print(el)
        count += 1
# ==============================================

my_new_list = LIST.__iter__()

for i in range(len(LIST)):
    print(my_new_list.__next__())

