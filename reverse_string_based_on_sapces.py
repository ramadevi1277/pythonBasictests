
input_str = "write test cases in java"

# Step 1: split words
reverse_string = input_str[::-1]

join_reverse_string = ''.join(input_str[::-1].split())
result_list = []
i = 0
for item in input_str.split():
    #import pdb;pdb.set_trace()
    len_of_item = len(item)
    result_list.append(join_reverse_string[i:i+len_of_item])
    i += len_of_item

print(' '.join(result_list))