list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd','e','f']

dict_1 = { k : v  for k,v in zip(list1,list2)}

print(dict_1)

###Using ZIP_longest for the uneven lists.
from itertools import cycle, zip_longest

dict_1 =  {k : v for k,v in zip_longest(list2,list1, fillvalue=6)}
print(dict_1)
