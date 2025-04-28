L1 = [1, 2, 2, 3, 2, 3, 4, 5]
dict_1 = {}
for item in L1:
    if item not in dict_1:
        dict_1[item] = L1.count(item)

Sorted_dict = sorted(dict_1.items(), key= lambda x : x[1])

print(f"most repeated element is {Sorted_dict[-1][0]} repeated {Sorted_dict[-1][1]}")
