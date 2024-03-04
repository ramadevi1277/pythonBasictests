def Selectio_Sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(arr)

arr = [19, 2, 31, 45, 30, 11, 121, 27]
Selectio_Sort(arr)