str1 = "adfgeo$pw%w^e&u*"

###Move vowels to first special char to middle consonants to alst

def arrange_character(str1):
    vow = []
    sp = []
    cons = []
    for each in str1:
        if each.isalpha():
            if each.lower() in ['a','e','i','o','u']:
                vow.append(each)
            else:
                cons.append(each)
        else:
            sp.append(each)

    print(''.join(vow+sp+cons))

arrange_character(str1)