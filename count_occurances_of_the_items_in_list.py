lst = [1, 2, 1, 4, 5, 6, 4, 3, 7, 1]

# count = 0
# dict_1 = {}
#
# for i in range(0, len(lst)):
#     if lst[i] not in dict_1:
#         for j in range(0, len(lst)):
#             if lst[i] == lst[j]:
#                 count += 1
#             dict_1[lst[i]] = count
#     count = 0
# print (dict_1)

# dict_1 = {}
# for i in set(lst):
#     if i not in dict_1:
#         count = lst.count(i)
#         dict_1[i] = count
#
# print (dict_1)


print ([[x, lst.count(x)] for x in set(lst)])

from collections import Counter

list_1 = Counter(lst)

print(list_1)



