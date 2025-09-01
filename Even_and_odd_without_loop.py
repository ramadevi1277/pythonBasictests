li = [-1, -2, 0, 1, 2, 4, -5]

even = list(filter(lambda x: x % 2 == 0, li))
odd  = list(filter(lambda x: x % 2 != 0, li))

print("Even numbers:", even)
print("Odd numbers:", odd)