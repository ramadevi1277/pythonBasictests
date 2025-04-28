
str10 = "Java is Beautiful programming"

list1 = []
list_split = str10.split()

smallest = min(list_split, key = len)
largest = max(list_split, key=len)

for word in list_split:
    if word == smallest or word == largest:
        list1.append(word[::-1])
    else:
        list1.append(word)


print(' '.join(list1))

str10 = "Java is Beautiful programming"
print(min(str10.split()))
print(max(str10.split()))
