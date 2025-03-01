l1 = [1,2,3,4,5]
l2 = [2,3,4,6,7]

l2_diff = set(l1) - set(l2)
l1_diff = set(l2) -set(l1)
print(list(l2_diff))
print(list(l1_diff))

