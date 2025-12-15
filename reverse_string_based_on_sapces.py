
input_str = "write test cases in java"

# Step 1: split words
reverse_string = input_str[::-1]

#join_reverse_string = ''.join(input_str[::-1].split())
join_reverse_string = input_str.replace(" ",'')[::-1]
len_of_input_word = [len(each) for each in input_str.split()]
result_list = []
i = 0
for item in len_of_input_word:
    result_list.append(join_reverse_string[i:i+item])
    i += item

print(' '.join(result_list))