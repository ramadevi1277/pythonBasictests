import re

###Method1
#def find_sum(str1):
 #   return sum(map(int, re.findall('\d+', str1)))

#str1 = "Rama123devi15"
str1 = "geeks4geeks25"

#print(find_sum(str1))

####Method2

def find_sum(str1):
    temp = ""
    result = 0
    for each in str1:
        if each.isdigit():
            temp += each
        else:
            if temp != "":
                result += int(temp)
                temp = ""
    if temp != "":
        result += int(temp)
    return result
print(find_sum(str1))


