dict_1 = {'a': 100, 'b': 200, 'c': 300}
list_1 = []
for each in dict_1:
    list_1.append(dict_1[each])
result = sum(list_1)

print (result)


###2nd approch
count = 0
for each in dict_1:
    count += dict_1[each]
print ("Getting count using 2nd apprach", count)

####3rd approach

#for each in dict_1:
res = sum(dict_1.values())
print("using dict sum", res)
