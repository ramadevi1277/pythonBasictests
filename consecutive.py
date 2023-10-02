listB = [6, 1, 4, 6, 3, 2, 7, 4]
sorted_list = list(set(sorted(listB)))
#sorted(l) ==
import pdb;pdb.set_trace()
range_list = list(range(min(listB), max(listB)+1))
if sorted_list == range_list:
   print("ListB has consecutive numbers")
else:
   print("ListB has no consecutive numbers")