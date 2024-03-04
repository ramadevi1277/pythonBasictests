###Like bubble sort, the insertion sort algorithm is straightforward to implement and understand. But unlike bubble sort,
# it builds the sorted list one element at a time by comparing each item with the rest of the list and inserting it into its correct position.
# It will compare values with left side

def insert_sort(arr):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j+1] = arr[j]
            j -= 1


        arr[j+1] = key_item
    print(arr)

arr = [2, 6, 0, 9, 1]
insert_sort(arr)