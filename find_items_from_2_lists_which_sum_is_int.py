list1 = [4,5,8,0,6]
list2 = [6,7,0,4,2]
result = []
set_list2 = set(list2)
for num in list1:
  if num - 8 in list2:
    print(num, 8 - num)
    result.append(num,8-num)
print(result)    
    
    
