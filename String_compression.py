str = "aabcccccaaa"

result = []

for each in set(str):
    count_ltr = 0
    count_ltr = str.count(each)
    result.extend([each,count_ltr])

print(result)