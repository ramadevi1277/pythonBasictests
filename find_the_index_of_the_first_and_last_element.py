str1= "aafgsfhfaaad"
found_element = "a"

def findindex(str1, found_element):
    index = []
    index.append(str1.index(found_element))  ###--> Index command alway return the index of the first occurence
    for i in range(len(str1)-1, -1, -1):
        if str1[i] == found_element:
            index.append(i)
            break

    print(index)


findindex(str1, found_element)
