def max_number(list, val):
    new_list = []
    for each in list:
        convert_str = str(each)
        if str(val) in convert_str:
            new_list.append(each)

    print(max(new_list))



max_number([1,2,33,35,36,37,44,94,104,467,43], 4)