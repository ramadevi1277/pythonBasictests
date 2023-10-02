def removeElement(nums, val):
    count_of_val = nums.count(val)
    new_liat = []
    for each in nums:
        if each != val:
            new_liat.append(each)
    for each_1 in range(count_of_val):
        new_liat.append("-")
        import pdb;pdb.set_trace()
    und = _    
    list_with_und = [_] * 3
    new_liat.extend(list_with_und)

    print(new_liat)

removeElement([1, 2, 3, 0, 0, 3, 3, 3], 3)