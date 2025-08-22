
input_str = "write test cases in java"

# Step 1: split words
reverse_string = input_str[::-1]

join_reverse_string = ''.join(input_str[::-1].split())
result_list = []
i = 0
for item in input_str.split():
    #import pdb;pdb.set_trace()
    index_1 = len(item)
    result_list.append(join_reverse_string[i:i+index_1])
    i += index_1

print(join_reverse_string)
print(result_list)