str1 = "Hi this is Ramadevi QA enginner"

conv_list = str1.split()

for index in range(len(conv_list)):
    if index % 2 == 1:
        conv_list[index] = conv_list[index][::-1]
print(" ".join(conv_list))
