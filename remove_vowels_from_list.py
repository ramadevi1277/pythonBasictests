str_1 = input("Enter a string :   ")

result = ""
for i in str_1:
    if i not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        #print("%s is a vowel" %(i))
        #i = ""
        result += i
print(result)


#List Comprehensition
#print (i for i in str_1 if i not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])