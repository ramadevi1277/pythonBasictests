def insert_list(intervals, newInterval):
    n = len(intervals)
    ans = []
    i = 0

    while i < n and intervals[i][1] < newInterval[0]:
        ans.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
        print(newInterval)
    print(ans)
    ans.append(newInterval)

    while i < n:
        ans.append(intervals[i])
        i += 1

    return ans


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
insert = [4, 8]

print(insert_list(intervals, insert))
