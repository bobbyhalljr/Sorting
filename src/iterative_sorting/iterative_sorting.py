arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                j += 1
        # swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

print(selection_sort(arr1))



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    lst = len(arr)
    # loop through array
    for num1 in range(lst):
        for num2 in range(lst-num1-1):
            if arr[num1] < arr[num2]:
                arr[num1], arr[num2] = arr[num2], arr[num1]

    return arr
print(bubble_sort(arr1))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr