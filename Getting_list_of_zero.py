li = [-1, -2, 0, 1, 2, 4, -5]
result = []

def find_subsets(index, current):
    if sum(current) == 0 and current:
        result.append(tuple(current))
    for i in range(index, len(li)):
        print(index,current)
        print(result)
        find_subsets(i+1, current + [li[i]])

find_subsets(0, [])
print("All subsets summing to 0:", set(result))  # set to avoid du

