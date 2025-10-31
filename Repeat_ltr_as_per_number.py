str_1 = "a2b3c2d4"

result = []
i = 0

while i < len(str_1):
    if str_1[i].isalpha():
        char = str_1[i]
    if i + 1 < len(str_1) and str_1[i+1].isdigit():
        result.append(char * int(str_1[i+1]))
        i += 2
    else:
        result.append(char)
        i += 1


print("".join(result))
