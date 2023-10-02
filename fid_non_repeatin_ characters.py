str_1 = "aaffggedafkolpcvmn"
result = ""
for i in str_1:
    count = 0
    count = str_1.count(i)
    if count == 1:
        result += i
print(result)


lst_cmp = [x for x in str_1 if str_1.count(x) == 1]
print (''.join(lst_cmp))