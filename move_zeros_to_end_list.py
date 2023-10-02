lst = [3, 0, 5, 6, 0, 2, 0, 1, 0, 6]
# k = 0
# for i in range(len(lst)):
#     if lst[i] != 0:
#         lst[k] = lst[i]
#         k += 1
# for j in range(k, len(lst)):
#     lst[j] = 0
#
# print("modified list is :", lst)



lst1 = [23, 56, 78, 0, 66, 0, 100, 0, 1, 50]
lst2 = sorted(lst1, reverse=True)
#
print("Moved zeros with sorted method: ", lst2)

###using with list pop
def moveZeroes(nums):
    for each in nums:
        if each == 0:
            pop = nums.pop(nums.index(each))
            nums.append(pop)
    print(nums)


moveZeroes([1, 4, 5, 0, 0, 4, 6, 7])

