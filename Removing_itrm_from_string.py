def remove(string, i):
    for j in range(len(string)):
        if j == i:
            string = string.replace(string[i], "", 2) # 1-->how many items need to replace.
    print(string)

remove("geeksFORgeeks", 1)