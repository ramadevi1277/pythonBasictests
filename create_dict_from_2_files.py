list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd','e','f']

dict_1 = { k : v  for k,v in zip(list1,list2)}

print(dict_1)

###Using ZIP_longest for the uneven lists.
from itertools import cycle, zip_longest

dict_1 =  {k : v for k,v in zip_longest(list2,list1, fillvalue=6)}
print(dict_1)



####Using Cycle for the uneven lists.

from itertools import cycle
from collections import defaultdict

dict_2 = defaultdict(list)
for k,v in zip(list1, list2):
    dict_2[k].append(v)


dict_1 = {k : v for k,v in zip(cycle(list1), list2)}

print(dict_2)

#dict_1 = {}
