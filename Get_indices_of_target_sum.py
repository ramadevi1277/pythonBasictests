def two_sum_indices(arr, target):
    # Dictionary to store value -> index
    value_to_index = {}

    for i, num in enumerate(arr):
        complement = target - num
        import pdb;pdb.set_trace()
        if complement in value_to_index:
            return (value_to_index[complement], i)
        value_to_index[num] = i

    return None


arr = [6, 8, 11, 6, 7, 18]
target = 17

result = two_sum_indices(arr, target)
if result:
    print(f"Indices of elements that sum to {target}: {result}")
else:
    print("No two elements sum to the target.")