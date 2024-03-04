def merger_Sort(unsortd_list):
    if len(unsortd_list) <= 1:
        return unsortd_list
    middle = len(unsortd_list) // 2
    left_part = unsortd_list[:middle]
    right_part = unsortd_list[middle:]
    left_part = merger_Sort(left_part)
    right_part = merger_Sort(right_part)

    return list(merge(left_part, right_part))

def merge(left_part, right_part):
    result = []
    import pdb;pdb.set_trace()
    while len(left_part) != 0 and len(right_part) != 0:
        if left_part[0] < right_part[0]:
            result.append(left_part[0])
            left_part.remove(left_part[0])
        else:
            result.append(right_part[0])
            right_part.remove(right_part[0])

    if len(left_part) == 0:
        result += right_part
    else:
        result += left_part

    return result

unsort_list = [1, 3, 5, 8, 1, 0, 5, 10]
print(merger_Sort(unsort_list))
