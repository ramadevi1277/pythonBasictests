str1 = "hello tst"

str_rep = str1.replace(" ","")

for non_rep in str_rep:
    if str_rep.count(non_rep) == 1:
        print("first non repeating character:", non_rep)
        break
for fst_rep in str_rep:
    if str_rep.count(fst_rep) > 1:
        print("first repeating character:", fst_rep)
        break