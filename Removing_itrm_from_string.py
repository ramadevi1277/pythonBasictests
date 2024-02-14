def remove(string, i):
    for j in range(len(string)):
        if j == i:
            string = string.replace(string[i], "")
    print(string)

remove("geeksFORgeeks", 1)