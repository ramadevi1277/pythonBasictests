def removeNthFromEnd(list, int):
    end = len(list) - int
    new_list = list[0:end]
    return new_list


list = [1,2,3,4,5,6]
print(removeNthFromEnd(list, 2))