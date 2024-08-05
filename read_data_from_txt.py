

file = open("C:/Users/rcheepurupalli/PycharmProjects/pythonBasictests/example.txt", 'r')
content = file.readlines()
for each in content:
    if 'TXT' in each:
        print(each.split()[2])
        break
file.close()