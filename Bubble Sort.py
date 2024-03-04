##Bubble Sort is a simple sorting algorithm. This sorting algorithm repeatedly compares two adjacent elements and swaps them if they are in the wrong order.

def bubbleSort(arr):
    n = len(arr)
    # For loop to traverse through all
    # element in an array
    for i in range(n):
        #### set falg to come out if there the list is already sorted
        already_sorted = True
        import pdb;pdb.set_trace()
        for j in range(0, n - i - 1):

            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found
            # is greater than the adjacent element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False
        if already_sorted:
           break

    print(arr)

# Driver code

# Example to test the above code
#arr = [2, 1, 10, 23]
arr = [1,2,10,23]

bubbleSort(arr)

