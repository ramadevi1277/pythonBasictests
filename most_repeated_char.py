from collections import Counter

# List of elements
L1 = [1, 2, 2, 3, 2, 3, 4, 5]

# Use Counter to count the frequency of each element
count = Counter(L1)

# Find the most common element and its frequency
most_common_element, most_common_count = count.most_common(1)[0]
import pdb;pdb.set_trace()

# Print the result
print(f"The most repetitive element is {most_common_element}, which appears {most_common_count} times.")