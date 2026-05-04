list1 = [123,456,789]
result = []
for i in list1:
  dif_sum = sum(int(j) for j in str(i))
  result.append(dif_sum)
print(result)  
  
  
