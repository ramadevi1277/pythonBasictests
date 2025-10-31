arr = [34, 0, 9, 5, 7, 4, 0, 4, 0, 23]

n = len(arr)
pos = n - 1  # position to place non-zero numbers (from end)

# Traverse from end and move non-zero elements backward
for i in range(n - 1, -1, -1):
    #import pdb;pdb.set_trace()
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos -= 1
print(arr)
print(pos)
while pos >= 0:
    arr[pos] = 0
    pos -= 1
print("Moving zeros to start:", arr)

arr = [34, 0, 9, 5, 7, 4, 0, 4, 0, 23]
n = len(arr)
pos = 0
for i in range(0,n):
    if arr[i] != 0 and pos <= n:
        arr[pos] = arr[i]
        pos += 1

while pos <= n-1:
    arr[pos] = 0
    pos += 1

print("Moving zeros to end:", arr)


