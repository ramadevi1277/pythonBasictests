test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}
list_1 = []
for val in test_dict.values():
    for each in val:
        list_1.append(each)
res = list(set(sorted(list_1)))
print (res)

print("printing keys", test_dict.keys())


###using set comparision

res_1 = list(sorted({ele for val in test_dict.values() for ele in val}))
print ("Using set comparision", res_1)

lst_com = list(set([val for each in test_dict.values() for val in each ]))
print ("Using List Comparision", lst_com)