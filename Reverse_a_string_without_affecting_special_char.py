def revere_string_without_Special_char(str1):
    list_1 = list(str1)
    print(list_1)
    left,right = 0, len(list_1) - 1

    while left < right:
        if not list_1[left].isalpha():
            left += 1
        elif not list_1[right].isalpha():
            right -= 1

        else:
            list_1[left], list_1[right] = list_1[right], list_1[left]
            left += 1
            right -= 1
    print("".join(list_1))



str1 = "c,.ad&gh^"
revere_string_without_Special_char(str1)

