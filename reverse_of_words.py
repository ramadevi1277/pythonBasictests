def reverseWords(s):
    str1 = s.split()
    return " ".join(str1[::-1])


print(reverseWords("My name is Ramadevi"))