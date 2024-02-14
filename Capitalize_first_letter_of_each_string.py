str1 = "i love automation"

list_1=[]
def capitalize_each_letter_of_string(str1):
    for each in str1.split():
        #import pdb;pdb.set_trace()
        list_1.append(each.title())

    print(list_1)
    print(" ".join(list_1))


capitalize_each_letter_of_string(str1)